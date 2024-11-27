from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Kategori, Product, Cart, CartItem, Order
from .forms import ProductForm
from django.shortcuts import redirect
from django.contrib import messages


# Daftar produk
def product_list(request):
    categories = Kategori.objects.all()
    products = Product.objects.filter(is_active=True)

    # Debugging output
    print("Categories:", categories)
    print("Products:", products)

    return render(request, 'shop/product_list.html', {
        'categories': categories,
        'products': products
    })
# Detail produk
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = Kategori.objects.all()  # Mengambil semua kategori
    return render(request, 'shop/product_detail.html', {
        'product': product, 
        'categories': categories})

def category_detail(request, slug):
    print(f"Slug diterima: {slug}")  # Log slug

    try:
        category = get_object_or_404(Kategori, slug=slug)
        print(f"Kategori ditemukan: {category.name}")  # Log kategori
    except Exception as e:
        print(f"Error: {e}")
        return render(request, '404.html')  # Atau tampilkan halaman error

    products = Product.objects.filter(category=category, is_active=True)
    print(f"Produk dalam kategori: {products.count()}")  # Log jumlah produk

    categories = Kategori.objects.all()
    return render(request, 'shop/category_detail.html', {
        'category': category,
        'products': products,
        'categories': categories,
    })


# Tambah ke keranjang
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': 1})
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

# Detail keranjang
@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'shop/cart_detail.html', {'cart': cart})

# Checkout
@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    order = Order.objects.create(
        user=request.user,
        total_amount=cart.total_price(),  # Pastikan metode ini ditambahkan di Cart
        status='PENDING'
    )
    for item in cart.cartitem_set.all():
        order.products.add(item.product)
        # Jika menggunakan OrderItem:
        # OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
    cart.cartitem_set.all().delete()  # Kosongkan keranjang
    return render(request, 'shop/order_confirmation.html', {'order': order})

# Tambah ulasan
@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        # Tambahkan model Review jika belum ada
        # Review.objects.create(product=product, user=request.user, rating=rating, comment=comment)
    return redirect('product_detail', slug=product.slug)

# Detail pesanan
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/order_detail.html', {'order': order})

# Tambah produk (admin atau pengguna tertentu)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Ganti dengan URL tujuan
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

def save_category(request):
    if request.method == 'POST':
        category_slug = request.POST.get('category_slug')
        if category_slug:
            try:
                category = Kategori.objects.get(slug=category_slug)
                # Tambahkan logika penyimpanan data kategori
                messages.success(request, 'Kategori berhasil disimpan.')
                return redirect('some_view_name')  # Ganti dengan nama view tujuan
            except Kategori.DoesNotExist:
                messages.error(request, 'Kategori tidak ditemukan.')
        else:
            messages.error(request, 'Slug kategori tidak ditemukan.')
    else:
        messages.error(request, 'Metode tidak diizinkan.')

    return redirect('some_view_name')