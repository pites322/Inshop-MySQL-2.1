from django.contrib import admin
from .models import Product, User, Image, Color
from django.contrib.auth.admin import UserAdmin


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class ProductAddAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    filter_horizontal = ['color']

class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_editable = ('name', )
    list_display_links = None


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAddAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Image)

