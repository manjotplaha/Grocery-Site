from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from .models import Type, Item, TeamMembers, Client, OrderItem
from django.shortcuts import get_object_or_404
import calendar
from .forms import OrderItemForm, InterestForm,ItemSearchForm
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.shortcuts import redirect

class SignUpView(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to the login page once you complete step 3
            return redirect('myapp:login')
        return render(request, self.template_name, {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'registration/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))



@login_required
def myorders(request):
    user = request.user
    if hasattr(user, 'client'):
        client = user
        orders = OrderItem.objects.filter(client=client)
        return render(request, 'myapp/myorders.html', {'orders': orders})
    else:
        message = 'You are not a registered client!'
        return render(request, 'myapp/myorders.html', {'message': message})

# Create your views here.
# def index(request):
#     type_list = Type.objects.all().order_by('id')
#     response = HttpResponse()
#     heading1 = '<p>' + 'Different Types: ' + '</p>'
#     response.write(heading1)                #send something back when user requests
#     # for type in type_list:
#     #     para = '<p>'+ str(type.id) + ': ' + str(type) + '</p>'
#     #     response.write(para)
#     # items_list = Item.objects.all()
#     items = Item.objects.order_by('-price')
#     for item in range(10):
#         para = '<p>'+str(items[item]) +'</p>'
#         response.write(para)
#     return response


# def index(request):
#
#     type_list = Type.objects.all().order_by('id')[:10]
#     # Session counting
#     session_count = request.session.get('count', 0)
#     request.session['count'] = session_count + 1
#
#     # Setting cookie
#     response = HttpResponse(render(request, 'myapp/index.html', {'session_count': session_count, 'type_list': type_list}))
#     response.set_cookie('cookie_counter', 'value', max_age=10)  # Set a cookie that expires in 10 seconds
#
#     return response

def index(request):
    type_list = Type.objects.all().order_by('id')
    session_count = int(request.COOKIES.get('cookie_counter', 0))
    session_count += 1
    response = HttpResponse(render(request, 'myapp/index.html', {'session_count': session_count, 'type_list': type_list}))
    response.set_cookie('cookie_counter', str(session_count), max_age=10)
    return response

def about(request):
    welcome_message = "This is an Online Grocery Store."
    session_count = int(request.COOKIES.get('cookie_counter2', 0))
    session_count += 1
    response = HttpResponse(render(request, 'myapp/about.html', {'session_count': session_count, 'welcome_message':welcome_message}))
    response.set_cookie('cookie_counter2', str(session_count), max_age=10)
    return response
# Lab 6 | PART 1| iii

# Yes, we are passing type_list as context variable, this is an argument which is passed on to the template
# for viewing, this list would be iterated to showcase the data in the template.

# def about(request, yr, mth):
#     response = HttpResponse()
#     mth_name = calendar.month_name[mth]
#     heading1 = '<p>This is an Online Grocery Store '+str(mth_name)+ str(yr)+'</p>'
#     response.write(heading1)
#     return response

# Lab 6 | Part 1 | d
# def about(request):
#     # mth_name = calendar.month_name[mth]
#     return render(request, 'myapp/about.html')

    # Answer for part d, iii
    #Yes, I am passing Year and month te template which has been taken as a input fromm the user, further the month name is calculated based on month number entered


# LAB 6 | Part 1 | e.
class Detail(View):     #CBV for Part 3

    def get(self, request, type_no):
        selected_type = Type.objects.get(pk=type_no)
        items = Item.objects.filter(type=selected_type)
        return render(request, 'myapp/detail.html', {'selected_type': selected_type,'items': items})
#"""To Answer part 5 ofe part, i am passing the selected_type and items list as variable to the template, these would be later traversed and displayed in the template."""

        # response = HttpResponse()
        #
        # for i in items:
        #     para = '<p>' + str(i.stock) + '</p>'
        #     response.write(para)
        # return response

def aboutUs(request):
    response = HttpResponse()
    heading1 = '<p> This is an Online Grocery Store </p>'
    response.write(heading1)
    return response


# # Comments explaining the differences during conversion:
#
# # 1. Function-Based View (FBV) is a simple function that takes a request and returns a response.
# # 2. Class-Based View (CBV) is a class that inherits from Django's View class and has methods (like get) for different HTTP methods.
# # 3. In FBV, the logic is directly in the function.
# # 4. In CBV, the logic is encapsulated in methods (e.g., get method for handling HTTP GET requests).
# # 5. CBV allows for more organized code with different methods for different HTTP methods.
# # 6. CBV can be extended more easily, for example, by adding additional methods for different actions.
# # 7. CBV is often more reusable as the behavior is encapsulated within the class.

# lAB 6 PART 2
class TeamMembersView(View):
    def get(self, request):
        details = TeamMembers.objects.all().order_by('-first_name')
        return render(request, 'myapp/teamDetailView.html',{'details':details})

def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp/items.html', {"itemlist":itemlist})

def placeorder(request):
    msg = ''
    ordered_item_name = ''
    ordered_quantity = ''
    client_name = ''
    itemlist = Item.objects.all()

    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.quantity <= order.item.stock:
                order.save()
                ordered_item_name = order.item.name
                ordered_quantity = order.quantity
                client_name = order.client.username
                order.item.stock -= order.quantity
                order.item.save()
                msg = 'Your order has been placed successfully.'
                # msg = '{{ordered_quantity}} {ordered_item_name} has been placed successfully by {client_name}'
            else:
                # msg = 'We do not have sufficient stock to fill your order.'
                return render(request, 'myapp/order_response.html', {'msg': msg})
    else:
        form = OrderItemForm()
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg, 'itemlist': itemlist, 'ordered_item_name':ordered_item_name, 'ordered_quantity':ordered_quantity,'client_name':client_name})


def item_search(request):
    price = None
    if request.method == 'POST':
        form = ItemSearchForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            price = item.price
    else:
        form = ItemSearchForm()

    return render(request, 'myapp/item_search.html', {'form': form, 'price': price})


def itemdetail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    # Initialize message variable
    message = ''

    # Check if the item is available
    if not item.available:
        message = 'This item is currently not available.'

    # If a POST request, process the interest form
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interested = int(form.cleaned_data['interested'])
            item.interested += interested
            item.save()
            # Redirect or display a success message
            return render(request, 'myapp/itemdetail.html',
                          {'item': item, 'form': form, 'message': 'Thank you for showing your interest!'})
    else:
        # Create a new instance of the interest form
        form = InterestForm()

    return render(request, 'myapp/itemdetail.html', {'item': item, 'form': form, 'message': message})