from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.datastructures import MultiValueDictKeyError
from .models import Product, ShoppingList, User
from .forms import AddBuy, ChangeWarranty, ChangeUserInformation
from django.utils import timezone
from django.views.generic.base import TemplateView
from functools import wraps


class HomePage(TemplateView):

    template_name = "app1/Main.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        productrs = Product.objects.all()
        current_page = Paginator(productrs, 10)
        page = self.request.GET.get('page', 1)
        try:
            context['Products'] = current_page.page(page)
        except PageNotAnInteger:
            context['Products'] = current_page.page(1)
        except EmptyPage:
            context['Products'] = current_page.page(current_page.num_pages)
        return context


class Search(TemplateView):

    template_name = "app1/search.html"

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        question = self.request.GET.get('search')
        if question is not None:
            search_products = Product.objects.filter(name__contains=question)
            context['last_question'] = '?search=%s' % question
            print(context['last_question'])
            current_page = Paginator(search_products, 10)
            page = self.request.GET.get('page', 1)
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


def product_details(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    form = AddBuy()
    photo = str(prod.photo)
    price = int(prod.price * 100)
    warr = ChangeWarranty(request.POST, instance=prod)
    if request.method == 'POST':
        form = form.save(commit=False)
        form.buyer = request.user
        form.buyer_id = request.user.id
        form.product_id = prod.id
        form.price = prod.price
        form.data_of_buy = timezone.now()
        form.product_name = prod.name
        try:
            import stripe
            stripe.api_key = "sk_test_KoPBXsif8wO9pa9GPKU9qsz6"
            stripe.Charge.create(
                amount=price,
                currency="usd",
                source=request.POST['stripeToken'],
                description="Test payment",
            )
            form.payed_or_not = 'Yes'
        except MultiValueDictKeyError:
            form.payed_or_not = 'No'
        form.save()
        warr = warr.save()
        warr.warranty = prod.warranty - 1
        warr.save()
        return redirect('bits in bytes')
    else:
        pass
    return render(request, 'app1/prod_detail.html', {'prod': prod, 'warr': warr, 'photo': photo, 'price': price})


def user_change_info(request):
    user = request.user
    if request.method == 'POST':
        form = ChangeUserInformation(request.POST, instance=user)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return redirect('profile')
    else:
        form = ChangeUserInformation(instance=user)
    return render(request, 'app1/profile_correct.html', {'form': form})


def basket(request, pk=None):
    prod_in_bask = ShoppingList.objects.filter(buyer_id=request.user.id, payed_or_not='No')
    story_of_buy = ShoppingList.objects.filter(buyer_id=request.user.id, payed_or_not='Yes')
    price = 0
    for prod in prod_in_bask:
        price = price + prod.price
    price = int(price * 100)
    if pk is not None:
        dell_pod = ShoppingList.objects.filter(id=pk)
        del_prod_obj = dell_pod.get()
        prod = get_object_or_404(Product, pk=del_prod_obj.product_id)
        dell_pod.delete()
        warr = ChangeWarranty(request.POST, instance=prod)
        warr = warr.save()
        warr.warranty = prod.warranty + 1
        warr.save()
        return redirect('basket')
    elif request.method == 'POST':
        import stripe
        stripe.api_key = "sk_test_KoPBXsif8wO9pa9GPKU9qsz6"
        if request.method == 'POST':
            stripe.Charge.create(
                amount=price,
                currency="usd",
                source=request.POST['stripeToken'],
                description="Test payment",
            )
        for prod in prod_in_bask:
            form = AddBuy(request.POST, instance=prod)
            if form.is_valid():
                form = form.save(commit=False)
                form.payed_or_not = "Yes"
                form.data_of_buy = timezone.now()
                form.save()
        return redirect('basket')
    else:
        pass
    return render(request, 'app1/basket.html', {'prod_in_bask': prod_in_bask, 'price': price, 'story': story_of_buy,})


def buy_one_product(request, pk):
    product = get_object_or_404(ShoppingList, pk=pk)
    product_data = get_object_or_404(Product, pk=product.product_id)
    form = AddBuy(request.POST, instance=product)
    price = int(product_data.price * 100)
    import stripe
    stripe.api_key = "sk_test_KoPBXsif8wO9pa9GPKU9qsz6"
    if request.method == 'POST':
        stripe.Charge.create(
            amount=price,
            currency="usd",
            source=request.POST['stripeToken'],
            description="Test payment",
        )
        if form.is_valid():
            form = form.save(commit=False)
            form.payed_or_not = "Yes"
            form.data_of_buy = timezone.now()
            form.save()
        return redirect('basket')
    return render(request, 'app1/buy_one.html', {'form': form, 'product': product,
                                                         'prod': product_data, 'price': price})