from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.HomePage.as_view(), name="bits in bytes"),
    path('product/(<pk>)/', views.product_details, name="product_details"),
    path('account/profile/', views.Profile.as_view(), name="profile"),
    path('account/profile/change_data', views.user_change_info, name="profile_correct"),
    path('account/basket', views.basket, name="basket"),
    path('account/basket/(<pk>)', views.basket, name="basket"),
    path('search/', views.Search.as_view(), name="searching"),
    path('account/basket/buy_one/(<pk>)', views.buy_one_product, name="product_buy_one"),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
       path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
