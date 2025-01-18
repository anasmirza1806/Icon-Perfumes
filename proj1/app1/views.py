from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout , login , authenticate
from django.contrib.auth.models import User, auth
from django.views import View
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

# class ProductView(View):
#     def get(self, request):
#         Attar = Product.objects.filter(category_id=1)
#         Limesticks = Product.objects.filter(category_id=2)
#         Perfumes = Product.objects.filter(category_id=3)
#         return render(request, 'products.html',{'Attar':Attar,'Limsticks':Limesticks,'Perfumes':Perfumes})


def index(request):
    categorys = Category.objects.all()
    #new_arrivals = Product.objects.filter(id=2)
    new_arrivals = Product.objects.filter(new_arrival='yes')
    products = Product.objects.all()
    popular_products = Product.objects.filter(popular_products='yes')
    return render(request, 'index.html',{'categorys':categorys,'new_arrivals':new_arrivals,'products':products,'popular_products':popular_products})

def products(request):
    products = Product.objects.all()
    sort_by = request.GET.get('sort')
    category_name = request.GET.get('category')

    price_range = request.GET.get("price")

    # category = request.GET.get("category")
    if category_name:
        products = Product.objects.filter(category_id__category_name=category_name)
    # try:
        
    #     # print(category)
    #     # category = str(category.capitalize())
    #     # print(category)
        
    #     # print(products)
    # except:
    #     print("error")
    
    # items_per_page = 9     
    # paginator = Paginator(products,items_per_page )
    # page_number = request.GET.get("page")
    # page = paginator.get_page(page_number)

    # category = Category.objects.all()
    # subcategory = Subcategory.objects.all()
    

    context = {
        'products': products,
        # 'category': category,
        # 'subcategory':subcategory,
        # 'category_name':category_name,
        'sort_by':sort_by,
        # 'subcategory_id':subcategory_id,
        'price_range':price_range,
    }
    return render(request, 'products.html',context)

def about(request):
    return render(request, 'about.html')
    
def contact(request):
    return render(request, 'contact.html')

def product_details(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'product_details.html',{'product':product})

def whishlist(request):
    return render(request, 'whishlist.html')

def cart(request):
    # cart_id = request.GET.get('cart_id')
    # customer_id = request.GET.get('customer_id')
    # product_id = request.GET.get('product_id')
    # product_name = Product.objects.get(product_name=product_name)
    # product = Product.objects.filter(id=product_id)
    # for p in product:
    #     image=p.image
    #     price=p.price
    #     Cart(customer_id=customer_id, product=product_name,image=image,price=price).save()
    #     return redirect('index')
    cart = Cart.objects.all()
    total_amount = 0
    subtotal = 0
    gst = 0
    for item in cart:
        subtotal += float((item.product_id.price) * (item.quantity))
    gst = round(float((subtotal) * 0.18))
    total_amount = round(float(gst + subtotal))
    return render(request, 'cart.html',{'cart_items':cart,"subtotal":subtotal, 'total_amount':total_amount,"gst":gst})

@login_required
def checkout(request, source):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    if source == 'cart':
        user = request.user
        carts = Cart.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        total_items = len(cart_items)
        amount = 0.0
        # shipping_charges = 100
        for c in cart_items:
            temp_amount = float(c.product_id.price) * int(c.quantity)
            amount += temp_amount
        amount = (amount)
        gst = float(amount * 0.18)
        total_amount = amount + gst
        return render(request, 'checkout.html',{'total_amount':total_amount,'subtotal':amount,"gst":gst,'total_items':total_items,'cart_items':cart_items,"cart_count":cart_count,"carts":carts})
    elif source == "buy" and request.method == "GET":
        prod_id = request.GET["product"]
        product = Product.objects.get(id=prod_id)
        user = request.user
        price = product.price
        gst = float(price) * 0.18
        total_amount = round(float(price) + (gst))
        return render(request, 'checkout.html',{"product":product,"gst":gst,"total_amount":total_amount})
    return render(request, 'checkout.html')


def error_page(request):
    return render(request, 'error_page.html')

# def sign_up(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']

    # data = User.objects.create_user(username=username,email=email, password=password)
    # data.save()

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Customer(customer_name=username, customer_email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'sign_up.html')

def cus_login(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']

    #     user = auth.authenticate(username=username, password=password)

    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect('index')
    #     return redirect('login')

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = Customer.objects.filter(customer_name=request.POST['username'],password=request.POST['password'])
    #     users = Customer.objects.all()

    #     if user:
    #         return redirect('index')
    #     else:
    #         error_msg='Invalid Username or Password'
    # else:
    #     error_msg =None

    # return render(request, 'login.html',{'error_msg':error_msg})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None :
            login(request,user)
            return  redirect('/')
        else:
            print("error")
            return redirect('/login')

    return render(request,'login.html')


def lgout(request):
    logout(request)
    return redirect('/')

@login_required(login_url="login")
def add_to_cart(request, prod_id):
    product = Product.objects.get(id=prod_id)
    user = request.user
    product_in_cart = False
    product_in_cart = Cart.objects.filter(Q(user=user) & Q(product_id=product)).exists()
    if not product_in_cart:
        Cart(user=user, product_id=product).save()
    return redirect("cart")
    
def add_to_cart_slug(request, prod_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=prod_id)
        user = request.user
        product_in_cart = False
        product_in_cart = Cart.objects.filter(Q(user=user) & Q(product_id=product)).exists()
        if not product_in_cart:
            Cart(user=user, product_id=product).save()
        data = {"success": "success"}
        return JsonResponse(data)
    else:
        data = {"error":"Login"}
        return JsonResponse(data)
    
def plus_cart(request):
    if request.method == "GET" and request.user.is_authenticated:
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        temp_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_amount = ("%.2f" % (float(p.quantity) * float(p.product.discounted_price)))        
            amount += float(temp_amount)
        totalamount = round(amount)
        amount = round(float(float(c.product_id.price) * int(c.quantity)))
        data = {
                'quantity':c.quantity,
                'price':c.product_id.price,
                'amount': amount,
                'totalamount' : totalamount,
                'success':'success'
        }
        return JsonResponse(data, safe=False)
    else:
        data = {
            'error':'auth_error'
        }
        return JsonResponse(data, safe=False)
    

def minus_cart(request):
    if request.method == "GET" and request.user.is_authenticated:
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if (c.quantity > 1):
            c.quantity -= 1
        c.save()
        amount = 0.0
        temp_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_amount = (float(p.quantity) * float(p.product.discounted_price))
            amount += float(temp_amount)
        totalamount = round(amount)
        amount = round(float(float(c.product_id.price) * int(c.quantity)))
        data = {
                'quantity':c.quantity,
                'amount': amount,
                'price':c.product_id.price,
                'totalamount' : totalamount,
                'success': 'success'
        }
        return JsonResponse(data, safe=False)
    else:
        data = {
            'error':'auth_error'
        }
        return JsonResponse(data, safe=False)
    

def remove_cart(request):
    if request.method == "GET" and request.user.is_authenticated:        
        user = request.user
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.delete()
        amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        cart_items = len(cart_product)
        for p in cart_product:    
            temp_amount = (float(p.quantity) * float(p.product_id.price))
            amount += temp_amount
        total_amount = round(amount)
        data = {
            'amount' : amount,
            'totalamount': total_amount,
            'cart_items':cart_items,
            'success':'success'
        }
        return JsonResponse(data)
    else:
        data = {
                    'error':'auth_error'
                }
        return JsonResponse(data, safe=False)
    
@login_required(login_url="login")
def orders(request):
    orders = Order.objects.filter(user=request.user)
    order_items = OrderItem.objects.filter(order__user=request.user)
    return render(request, "orders.html",{"orders": orders,"order_items": order_items})

@login_required(login_url="login")
def place_order_cart(request):
    if request.method == "POST":
        user = request.user
        f_name = request.POST.get("c_fname")
        l_name = request.POST.get("c_lname")
        country = request.POST.get("country")
        address_1 = request.POST.get("c_address1")
        address_2 = request.POST.get("c_address2")
        city = request.POST.get("city")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        subtotal = 0
        total_amount = 0
        carts = Cart.objects.filter(user=user)
        gst = 0
        for cart in carts:
            subtotal += (float(cart.product_id.price)) * (cart.quantity)
        gst = subtotal * 0.18
        total_amount = gst + subtotal
        order = Order.objects.create(user=user,city=city,email=email,phone=phone,state=state,pincode=pincode,address_Line1=address_1,address_Line2=address_2,subtotal=subtotal,gst=gst,total_amount=total_amount    )
        for cart in carts:
            order.products.add(cart.product_id, through_defaults={"quantity": cart.quantity})
        order.save()
        messages.success(request, "Order has been placed successfully")
        return redirect("/orders/")
    else:
        return redirect("/")
@login_required(login_url="login")
def place_order_buy(request):
    if request.method == "POST":
        user = request.user
        f_name = request.POST.get("c_fname")
        l_name = request.POST.get("c_lname")
        country = request.POST.get("country")
        address_1 = request.POST.get("c_address1")
        address_2 = request.POST.get("c_address2")
        city = request.POST.get("city")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        subtotal = 0
        total_amount = 0
        gst = 0
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)
        gst = (float(product.price) * 0.18) 
        subtotal = float(product.price)
        total_amount = gst + subtotal
        order = Order.objects.create(user=user,city=city,email=email,phone=phone,state=state,pincode=pincode,address_Line1=address_1,address_Line2=address_2,subtotal=subtotal,gst=gst,total_amount=total_amount    )
        order.products.add(product, through_defaults={"quantity": 1})
        order.save()
        messages.success(request, "Order has been placed successfully")
        return redirect("/orders/")
    else:
        return redirect("/")