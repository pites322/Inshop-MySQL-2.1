from django.http import QueryDict, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from django.views.generic import FormView
from django.db.models import F
from .models import Product, ShoppingList, User, Image
from .forms import AddBuy, ChangeWarranty, ChangeUserInformation
from django.utils import timezone
from django.views.generic.base import TemplateView
from functools import wraps


class HomePage(TemplateView):

    template_name = "app1/Main.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        products = Product.objects.prefetch_related('image_set').all()
        current_page = Paginator(products, 10)
        page = self.request.GET.get('page', 1)
        image_dict = {}
        for elem in current_page.object_list:
            try:
                image = elem.image_set.all()[0]
                image_dict.update({image.photo.url: image.product_photo_connect_id})
            except IndexError:
                pass
        context['Images'] = image_dict
        try:
            context['Products'] = current_page.page(page)
        except PageNotAnInteger:
            context['Products'] = current_page.page(1)
        except EmptyPage:
            context['Products'] = current_page.page(current_page.num_pages)
        return context


class Search(HomePage):

    template_name = "app1/search.html"

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        question = self.request.GET.get('search')
        if question is not None:
            products = Product.objects.prefetch_related('image_set').filter(name__contains=question)
            context['last_question'] = '?search=%s' % question
            current_page = Paginator(products, 10)
            page = self.request.GET.get('page', 1)
            image_dict = {}
            for elem in current_page.object_list:
                try:
                    image = elem.image_set.all()[0]
                    image_dict.update({image.photo.url: image.product_photo_connect_id})
                except IndexError:
                    pass
            context['Images'] = image_dict
            # try:
            #     indexlist = [page.pk for page in current_page.object_list]
            #     start, end = indexlist[0], indexlist[-1]
            #     images = Image.objects.raw(f'SELECT * FROM app1_image WHERE product_photo_connect_id '
            #                                f'BETWEEN {start} AND {end}')
            #     image_dict = {}
            #     for index in indexlist:
            #         for image in images:
            #             if index == image.product_photo_connect_id and index in indexlist:
            #                 image_dict.update({image.photo.url: image.product_photo_connect_id})
            #                 index = 0
            #     context['photos'] = image_dict
            # except IndexError:
            #     context['photos'] = {}
            try:
                context['products_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['products_lists'] = current_page.page(1)
            except EmptyPage:
                context['products_lists'] = current_page.page(current_page.num_pages)

        return context


class Profile(TemplateView):

    template_name = "app1/profile.html"

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        pk = self.request.user.id
        user_data = get_object_or_404(User, pk=pk)
        context['first_name'] = user_data.first_name
        context['last_name'] = user_data.last_name
        context['region'] = user_data.region
        context['city'] = user_data.city
        context['address'] = user_data.address
        context['delivery'] = user_data.delivery
        return context


class ProductDetails(TemplateView):

    template_name = 'app1/prod_detail.html'

    def get_context_data(self, pk, **kwargs,):
        context = super(ProductDetails, self).get_context_data(**kwargs)
        prod = get_object_or_404(Product, pk=pk)
        context['prod'] = prod
        context['photos'] = Image.objects.filter(product_photo_connect_id=pk)
        context['price'] = int(prod.price * 100)
        return context

    def post(self, request, pk):
        prod = get_object_or_404(Product, pk=pk)
        price = int(prod.price * 100)
        try:
            import stripe
            stripe.api_key = "sk_test_KoPBXsif8wO9pa9GPKU9qsz6"
            stripe.Charge.create(
                amount=price,
                currency="usd",
                source=request.POST['stripeToken'],
                description="Test payment",
            )
            ShoppingList.objects.create(buyer=request.user, product=prod, price=prod.price, product_name=prod.name,
                                        payed_or_not=1)
        except:
            ShoppingList.objects.create(buyer=request.user, product=prod, price=prod.price, product_name=prod.name)
        prod.warranty -= 1
        prod.save()
        return redirect('bits in bytes')


class UserChangeInfo(FormView):
    template_name ='app1/profile_correct.html'
    form_class = ChangeUserInformation

    def get_form_kwargs(self):
        kwargs = super(UserChangeInfo, self).get_form_kwargs()
        kwargs['instance'] = User.objects.get(id=self.request.user.id)
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect('profile')


class Basket(TemplateView):

    template_name = 'app1/basket.html'

    def get_context_data(self, **kwargs,):
        context = super(Basket, self).get_context_data(**kwargs)
        context['prod_in_bask'] = ShoppingList.objects.filter(buyer_id=self.request.user.id).order_by('-data_of_buy')
        context['price'] = int(self.request.user.basket_state) * 100
        return context

    def post(self, request):
        prod_in_bask = ShoppingList.objects.filter(buyer_id=request.user.id)
        price = int(request.user.basket_state) * 100
        try:
            import stripe
            stripe.api_key = "sk_test_KoPBXsif8wO9pa9GPKU9qsz6"
            stripe.Charge.create(
                amount=price,
                currency="usd",
                source=request.POST['stripeToken'],
                description="Test payment",
            )
            for prod in prod_in_bask:
                if not prod.payed_or_not:
                    prod.payed_or_not = 1
                    prod.save()
            return redirect('basket')
        except:
            return redirect('basket')


class BasketActions(View):

    def post(self, request):
        request_data = QueryDict(request.body)
        prod_id, buyer_id = request_data.get('prod_id'), request_data.get('buyer_id')
        buy = Product.objects.get(pk=prod_id)
        buyer = User.objects.get(pk=buyer_id)
        ShoppingList.objects.create(buyer=buyer, product=buy, price=buy.price, product_name=buy.name)
        buy.warranty -= 1
        buy.save()
        return JsonResponse({'status': 'success'})

    def delete(self, request):
        request_data = QueryDict(request.body)
        if 'pk' in request_data:
            pk = request_data.get('pk')
            dell_prod = ShoppingList.objects.get(pk=pk)
            dell_prod.product.warranty += 1
            dell_prod.product.save()
            dell_prod.delete()
            return JsonResponse({'status': 'success'})
        else:
            user_id = request_data.get('userId')
            clear_list = [int(elem) for elem in request_data.getlist('list[]') if elem != '']
            purchases = User.objects.get(id=user_id).shoppinglist_set.all()
            for elem in purchases:
                if elem.pk in clear_list:
                    elem.delete()
        return JsonResponse({'status': 'success'})


class BuyOneProduct(TemplateView):

    template_name = 'app1/buy_one.html'

    def get_context_data(self, pk, **kwargs):
        print(self.request)
        context = super(BuyOneProduct, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(ShoppingList, pk=pk)
        context['prod'] = context['product'].product
        context['photos'] = Image.objects.filter(product_photo_connect_id=context['prod'].pk)
        context['price'] = int(context['prod'].price * 100)
        return context

    def post(self, request, pk):
        buy = get_object_or_404(ShoppingList, pk=pk)
        price = int(buy.product.price * 100)
        import stripe
        stripe.api_key = "sk_test_KoPBXsif8wO9pa9GPKU9qsz6"
        try:
            stripe.Charge.create(
                amount=price,
                currency="usd",
                source=request.POST['stripeToken'],
                description="Test payment",
            )
            buy.payed_or_not = 1
            buy.save()
            return redirect('basket')
        except:
            return redirect('product_buy_one')


