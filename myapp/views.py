from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Type, Item
import calendar
from django.shortcuts import render


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


def index(request):
    type_list = Type.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'type_list': type_list})

def about(request, yr, mth):
    response = HttpResponse()
    mth_name = calendar.month_name[mth]
    heading1 = '<p>This is an Online Grocery Store '+str(mth_name)+ str(yr)+'</p>'
    response.write(heading1)
    return response


class Detail(View):     #CBV for Part 3

    def get(self, request, type_no):
        response = HttpResponse()
        try:
            selected_type = Type.objects.get(pk=type_no)
            items = Item.objects.filter(type=selected_type)
            for i in items:
                para = '<p>' + str(i.stock) + '</p>'
                response.write(para)
            return response
        except:
            return HttpResponse(status=404)

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from django.shortcuts import get_object_or_404
# from .models import Type, Item
# import calendar
#
#
# # Create your views here.
# def index(request):
#     type_list = Type.objects.all().order_by('id')
#     response = HttpResponse()
#     #heading1 = '<p>' + 'Different Types: ' + '</p>'
#     #response.write(heading1)                #send something back when user requests
#     # for type in type_list:
#     #     para = '<p>'+ str(type.id) + ': ' + str(type) + '</p>'
#     #     response.write(para)
#     # items_list = Item.objects.all()
#     items = Item.objects.order_by('-price')
#     heading2 = '<p>' + 'Top 10 items in descending order of price: ' + '</p>'
#     response.write(heading2)
#     for item in range(10):
#         para = '<p>'+str(items[item]) +'</p>'
#         response.write(para)
#     return response
#
#
# def about(request):
#     response = HttpResponse("This is an Online Grocery Store")
#     return response
#
#
# def about_with_params(request, yr, mth):
#     response = HttpResponse()
#     mth_name = calendar.month_name[mth]
#     heading3 = '<p>This is an Online Grocery Store - '+str(mth_name)+ ' ' + str(yr)+'</p>'
#     response.write(heading3)
#     return response
#
# def detail(request, type_no):
#     selected_type = get_object_or_404(Type, id=type_no)
#     items = Item.objects.filter(type=selected_type)
#     response = HttpResponse()
#     heading = '<p>' + f'Items for Type {type_no}: ' + '</p>'
#     response.write(heading)
#
#     for item in items:
#         item_para = '<p>' + str(item) + '</p>'
#         response.write(item_para)
#     return response
#
# def function_based_view(request):
#     return HttpResponse("This is a Function-Based View.")
#
# class Class_based_view(View):
#     def get(self, request):
#         return HttpResponse("This is a Class-Based View.")
#
#
# # Comments explaining the differences during conversion:
#
# # 1. Function-Based View (FBV) is a simple function that takes a request and returns a response.
# # 2. Class-Based View (CBV) is a class that inherits from Django's View class and has methods (like get) for different HTTP methods.
# # 3. In FBV, the logic is directly in the function.
# # 4. In CBV, the logic is encapsulated in methods (e.g., get method for handling HTTP GET requests).
# # 5. CBV allows for more organized code with different methods for different HTTP methods.
# # 6. CBV can be extended more easily, for example, by adding additional methods for different actions.
# # 7. CBV is often more reusable as the behavior is encapsulated within the class.