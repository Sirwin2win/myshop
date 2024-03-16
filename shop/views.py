from django.shortcuts import render,get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.contrib import messages
from cart.forms import CartAddProductForm
# Create your views here.



def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('shop:category_list')
    else:
        form = CategoryForm()
    return render(request, 'shop/category/create_category.html', {'form': form})


def category_list(request):
    category = Category.objects.all()
    return render(request, 'shop/category/category_list.html', {'category':category})
def update_category(request, id):
    # Fetch the object related to the passed id
    categories = get_object_or_404(Category, id = id)
    name = request.POST.get('name')
    # Pass the object as instance in form
    form = CategoryForm(request.POST or None, instance = categories) 
    # save the data from the form and redirect
    if form.is_valid():
        # slug = form.save(commit=False)
        # slug.slug = name
        form.save()
        return redirect("shop:category_list")
    return render(request, 'shop/category/update_category.html', {'form':form})


def delete_category(request, id):
    # Fetch the object related to passed id
    categories = get_object_or_404(Category, id = id)
    if request.method == 'POST':
        # delete object
        categories.delete()
        # After deleting, redirect to category listing page
        return redirect("shop:category_list")
    return render(request, 'shop/category/delete_category.html')




def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("shop:prod_list")
    else:
        form = ProductForm()
    return render(request, 'shop/products/create_product.html', {'form': form})



def product_list(request ,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/products/list.html', {'category': category,'categories': categories,'products': products} )

def product_detail(request,   id, slug):
    products = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/products/detail.html',{'products': products ,'cart_product_form': cart_product_form})



def about(request):
    return render(request,'shop/products/about.html')


def contact(request):
    return render(request,'shop/products/contact.html')


def portal(request):
    return render(request,'shop/products/portal.html')

def prod_list(request ,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/products/prod_list.html', {'category': category,'categories': categories,'products': products})


def update_product(request, id):
    # Fetch the object related to the passed id
    tutorials = get_object_or_404(Product, id = id)
    name = request.POST.get('name')
    # Pass the object as instance in form
    form = ProductForm(request.POST or None, instance = tutorials) 
    # save the data from the form and redirect
    if form.is_valid():
        # slug = form.save(commit=False)
        # slug.slug = name
        form.save()
        return redirect("shop:prod_list")
    return render(request, 'shop/products/update_product.html', {'form':form})


def delete_product(request, id):
    # Fetch the object related to passed id
    tutorials = get_object_or_404(Product, id = id)
    if request.method == 'POST':
        # delete object
        tutorials.delete()
        # After deleting, redirect to category listing page
        return redirect("shop:prod_list")
    return render(request, 'shop/products/delete_product.html')

