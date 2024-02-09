from django.shortcuts import render

from customer.models import userlogin
from customer.models import transaction


def login(request):
    return render(request,'login.html')

def transaction(request):
    return render(request,'transaction.html')

def insertlogin(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        userlogin.objects.create(user_id=s1, username=s2,  password=s3, email=s4,first_name=s5,last_name=s6)
        return render(request, "login.html")
    return render(request,"login.html")
def viewlogin(request):
    userdict = userlogin.objects.all()
    return  render(request,"viewlogin.html",{'userdict':userdict})


def inserttransaction(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        transaction.objects.create( transaction_id=s1, user=s2,  date=s3, amount=s4,description=s5,category=s6,type=s6)
        return render(request, "transaction.html")
    return render(request,"transaction.html")
# Create your views here.
def viewtransaction(request):
    userdict = transaction.objects.all()
    return  render(request,"viewtransaction.html",{'userdict':userdict})
