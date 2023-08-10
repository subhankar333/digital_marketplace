from django.shortcuts import render,redirect
from .models import Product,Order_detail
from .forms import ProductForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    products = Product.objects.all()
    return render(request,'myapp/index.html',{'products':products})


def detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'myapp/detail.html',{'product':product})


def checkout(request,id):
    product = Product.objects.get(id=id)
    order = Order_detail()
    order.product = product
    order.amount = int(product.price)
    product = Product.objects.get(id=order.product.id)
    product.total_sales_amount = product.total_sales_amount + int(product.price)
    product.total_sales = product.total_sales + 1
    order.save()

    return render(request,'myapp/checkout.html',{'checkout':checkout})


def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            new_form = product_form.save(commit=False)
            new_form.seller = request.user
            new_form.save()
            return redirect('index')

    product_form = ProductForm()
    return render(request,'myapp/create_product.html',{'product_form':product_form})



def edit_product(request,id):
    product = Product.objects.get(id=id)
    if product.seller != request.user:
        return redirect('invalid')

    product_form = ProductForm(request.POST or None,request.FILES or None,instance=product)
    if request.method == 'POST':
        if product_form.is_valid():
            product_form.save()
            return redirect('index')
        
    return render(request,'myapp/edit_product.html',{'product_form':product_form,'product':product})


def delete_product(request,id):
    product = Product.objects.get(id=id)
    if product.seller != request.user:
        return redirect('invalid')
    
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    
    return render(request,'myapp/delete_product.html',{'product':product})


def dashboard(request):
    products = Product.objects.filter(seller=request.user)
    return render(request,'myapp/dashboard.html',{'products':products})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return redirect('index')
    user_form = UserRegistrationForm()
    return render(request,'myapp/register.html',{'user_form':user_form})


def invalid(request):
    return render(request,'myapp/invalid.html')



def my_purchases(request):
    orders = Order_detail.objects.all()
    return render(request,'myapp/purchases.html',{'orders':orders})



def sales(request):
    return render(request,'myapp/sales.html')