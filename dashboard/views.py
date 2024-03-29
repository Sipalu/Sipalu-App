import urllib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import RegisterUserFrom
from django.contrib import messages
from .models import OrderItem, Profile, ShippingAddress
from django.contrib.auth.models import User, auth
import requests
import json
from django.conf import settings
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from .forms import CategoryForm
from .models import Category, Service, Worker, BlogComment, Order
from dashboard.templatetags import extras
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import datetime
from channels.layers import get_channel_layer
# Create your views here.
from django.contrib.auth import logout

from asgiref.sync import async_to_sync
from .tasks import test_fun


def celeryt(request):
    test_fun.delay()
    return HttpResponse("done")


def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': json.dumps("Notification")
        }
    )
    return HttpResponse("Done")


def logout_request(request):
    logout(request)
    return redirect("/login")


def aboutus(request):
    return render(request, 'dashboard/aboutus.html')


def search(request):
    service = Service.objects.all()
    keyword = request.GET.get('query').capitalize()
    if keyword:
        services = Service.objects.filter(service_name__contains=keyword)
        return render(request, 'dashboard/search.html', {'service': services})
    return render(request, 'dashboard/search.html', {'services': service})


def dashboard(request):
    services = Service.objects.filter().order_by('-count')[:8]
    if request.user.is_authenticated:
        try:
            pro = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            fname = request.user.first_name
            lname = request.user.last_name
            uname = request.user.username
            email = request.user.email
            password = "password"
            user = User.objects.get(username=uname)
            Prof = Profile(firstname=fname, lastname=lname, user=user, email=email)
            Prof.save()
            user.passsword = password
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Successfully crated password and your default password is: password")

        order, created = Order.objects.get_or_create(customer=request.user, complete=False)

        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {
        'room_name': "broadcast",
        'service': services,
        'cartItems': cartItems

    }
    return render(request, 'dashboard/dashboard.html', context)

# function for registration

def register(request):
    form = RegisterUserFrom()
    if request.method == 'POST':
        form = RegisterUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, firstname=user.first_name, lastname=user.last_name, email=user.email)
            messages.add_message(request, messages.SUCCESS, 'User created Successfully')
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, "Failed to create an account, Check carefully and Try Again!")
            return render(request, 'dashboard/register.html', {'form': form})


    context = {
        'form': form
    }
    return render(request, 'dashboard/register.html', context)


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passwd = request.POST['password']
        print("First")
        user = auth.authenticate(username=uname, password=passwd)

        if user is not None:
            if not user.is_staff:

                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': settings.RECAPTCHA_PRIVATE_KEY,
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req = urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())
                print(result)

                ''' End reCAPTCHA validation '''
                if result['success']:
                    auth.login(request, user)
                    messages.success(request, "User Signed In " + uname)
                    return redirect("/")

                else:
                    print('fail')
                    messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                    return redirect('/login')

                # return redirect("/signup")

                # return HttpResponse("Success")

            elif user.is_staff:
                auth.login(request, user)
                messages.success(request, "Welcome to Sipalu Admin Site.")
                return redirect('/admin')
                # return HttpResponse("Success")
        else:
            messages.add_message(request, messages.ERROR, "Invalid Username and Password!")
            # return render(request, 'dashboard/login.html')
            return HttpResponse("Failed")

    else:
        return render(request, 'dashboard/login.html')

# function for category
def category(request):
    categ = Category.objects.all()
    ser_id = request.GET.get('service')
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    cartItems = order.get_cart_items
    cat_id = request.GET.get('categories')

    if ser_id:

        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        service = Service.objects.filter(category=ser_id)
        if request.method == "POST":
            minPrice = request.POST.get("minPrice")
            maxPrice = request.POST.get("maxPrice")
            service = service.filter(service_price__gte=minPrice, service_price__lte=maxPrice)

        paginator = Paginator(service, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        services = Service.objects.all()
        categories = Category.objects.all()

        context = {
            'service': page_obj,
            'cartItems': cartItems,
            'category': categ,
            'services': services,
            'categories': categories,

        }

        return render(request, 'dashboard/rentalservices.html', context)

    return render(request, 'dashboard/demo.html', {'cat': categ, 'cartItems': cartItems})


def servicedetail(request, id):
    each_service = Service.objects.get(id=id)
    comments = BlogComment.objects.filter(service=each_service, top=None).order_by('-id')
    replies = BlogComment.objects.filter(service=each_service).exclude(top=None)

    replyDict = {}
    for reply in replies:
        if reply.top.id not in replyDict.keys():
            replyDict[reply.top.id] = [reply]
        else:
            replyDict[reply.top.id].append(reply)

    print(replyDict)
    each_service.count += 1
    each_service.save()
    context = {
        'service': each_service,
        'comments': comments,
        'replyDict': replyDict,

    }

    return render(request, 'dashboard/servicedetails.html', context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        service_id = request.POST.get('serviceID')
        service = Service.objects.get(id=service_id)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = BlogComment(comment_post=comment, user=user, service=service)
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(id=parentSno)
            comment = BlogComment(comment_post=comment, user=user, top=parent, service=service)

            comment.save()
            messages.add_message(request, messages.SUCCESS, "Your reply has been posted successfully")

    return redirect(f"/service-deatils/{service.id}")

  


def toggleLike(request, service_id):
    # an ajax call is made using this function
    post = BlogComment.objects.get(id=service_id)
    like_count = post.like.count()
    is_like = False
    if request.method == 'POST':
        for like in post.like.all():

            if like == request.user:
                is_like = True
                like_count = post.like.count()

                break
        if not is_like:
            post.like.add(request.user)
            like_count = post.like.count()

        if is_like:
            post.like.remove(request.user)
            like_count = post.like.count()

    return JsonResponse({"is_like": is_like, "like_count": like_count})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}


    return render(request, 'dashboard/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'shipping': False}
    return render(request, 'dashboard/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user
    product = Service.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, service=product)

    if action == 'add':
        messages.success(request, "Service Added")
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        messages.success(request, "Service removed")
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)


def mylist(request):
    user = request.user
    items = Order.objects.filter(customer=user, ).order_by('-id')
    
    context = {
        'items': items,
    }
    return render(request, 'dashboard/mylist.html', context)
