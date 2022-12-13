from django.shortcuts import render
from datetime import datetime
from src.models import Order, Kitchen_Order
# Create your views here.
def orders( orderno,items):
    items = str(items).replace("my order is", "")
    Order_Number = orderno
    order = Order(Order_Number = Order_Number, items = items, date = datetime.today())
    order.save()
    print(items)

def bill(request):
    stud = Order.objects.all().order_by("-id")
    return render(request, "billindex.html", {"stu": stud})

def kitchen(request):
    stud = Kitchen_Order.objects.all().order_by("-id")
    return render(request, "kitchen.html", {"stu": stud})

