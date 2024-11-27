from django.contrib import admin
from .models import Kategori, Product, Cart, CartItem, Order, OrderItem

# Gunakan dekorator untuk pendaftaran model Kategori
@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'price', 'stock_produk', 'is_active', 'category', 'created_at')
    list_filter = ('is_active', 'category')

# Model lain tetap menggunakan admin.site.register
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
