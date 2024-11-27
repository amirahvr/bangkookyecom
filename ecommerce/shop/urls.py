from django.urls import path
from . import views

urlpatterns = [
    # Halaman daftar produk
    path('', views.product_list, name='product_list'),

    # Halaman daftar produk berdasarkan kategori
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),

    # Halaman detail produk
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('save-category/', views.save_category, name='save_category'),
    # Menambahkan produk ke keranjang
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # Menampilkan keranjang
    path('cart/', views.cart_detail, name='cart_detail'),

    # Checkout
    path('checkout/', views.checkout, name='checkout'),

    # Menambahkan ulasan pada produk
    path('product/<int:product_id>/review/', views.add_review, name='add_review'),

    # Halaman detail pesanan
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),

    # Menambahkan produk (admin atau pengguna tertentu)
    path('add-product/', views.add_product, name='add_product'),
]
