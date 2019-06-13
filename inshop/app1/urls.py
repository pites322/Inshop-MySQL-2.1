from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.HomePage.as_view(), name="bits in bytes"),
    path('product/(<int:pk>)', views.ProductDetails.as_view(), name="product_details"),
    path('account/profile/', views.Profile.as_view(), name="profile"),
    path('account/profile/change_data', views.UserChangeInfo.as_view(), name="profile_correct"),
    path('account/basket', views.Basket.as_view(), name="basket"),
    path('account/basket/(<int:pk>)', views.Basket.as_view(), name="basket"),
    path('search/', views.Search.as_view(), name="searching"),
    path('account/basket/buy_one/(<int:pk>)', views.BuyOneProduct.as_view(), name="product_buy_one"),
    path('basketdell/', views.BasketActions.as_view(), name="basket_actions"),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
       path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
