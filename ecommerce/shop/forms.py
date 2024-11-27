from django import forms
from .models import Kategori, Product

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['name', 'description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'stock_produk','merek_produk','stock_diskon', 'bahan', 'image','is_active']
