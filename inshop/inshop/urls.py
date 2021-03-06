"""inshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from app1.forms import CustomUserForm
from api.views import ProductView, BasketViewAlt
from django_registration.backends.one_step.views import RegistrationView
from django.conf.urls.static import static
from rest_framework import routers

from . import settings

router = routers.DefaultRouter()
router.register('basket/', BasketViewAlt)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('accounts/register/',
         RegistrationView.as_view(form_class=CustomUserForm),
         name='django_registration_register',),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router.urls)),
    # path('api/v1/basket/', BasketView.as_view()),
    path('api/v1/products/', ProductView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
