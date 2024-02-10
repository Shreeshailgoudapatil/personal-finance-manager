import category
from django.shortcuts import render

from customer.models import userlogin
from customer.models import transaction
from customer.models import category
from customer.models import goal
from customer.models import budget
from customer.models import newuser

#
# def login(request):
#     return render(request,'login.html')

# def transaction(request):
#     return render(request,'transaction.html')

# def insertlogin(request):
#     if (request.method == "POST"):
#         s1 = request.POST.get("t1")
#         s2 = request.POST.get("t2")
#         s3 = request.POST.get("t3")
#         s4 = request.POST.get("t4")
#         s5 = request.POST.get("t5")
#         s6 = request.POST.get("t6")
#         userlogin.objects.create(user_id=s1, username=s2,  password=s3, email=s4,first_name=s5,last_name=s6)
#         return render(request, "login.html")
#     return render(request,"login.html")

def index(request):
    return render(request,"index.html")
def viewlogin(request):
    userdict = userlogin.objects.all()
    return  render(request,"viewuserlogin.html",{'userdict': userdict})

def login_del(request, pk):
    rid = userlogin.objects.get(id=pk)
    rid.delete()
    userdict = userlogin.objects.all()
    return render(request, "viewuserlogin.html", {'userdict': userdict})

def inserttransaction(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")

        transaction.objects.create( transaction_id=s1, user=s2,  date=s3, amount=s4,description=s5,category=s6,type=s7)
        return render(request, "transaction.html")
    return render(request,"transaction.html")

def transaction_del(request, pk):
    rid = transaction.objects.get(id=pk)
    rid.delete()
    userdict = transaction.objects.all()
    return render(request, "transaction.html", {'userdict': userdict})
# Create your views here.
def viewtransaction(request):
    userdict = transaction.objects.all()
    return  render(request,"viewtransaction.html",{'userdict':userdict})

def insertbudget(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")

        budget.objects.create(budget_id=s1, user=s2, category=s3, month=s4, amount=s5)
        return render(request, "budget.html")
    return render(request, "budget.html")

def budget_del(request, pk):
    rid = budget.objects.get(id=pk)
    rid.delete()
    userdict = budget.objects.all()
    return render(request, "viewbudget.html", {'userdict': userdict})

def viewbudget(request):
    userdict = budget.objects.all()
    return  render(request,"viewbudget.html",{'userdict':userdict})

def goal_del(request, pk):
    rid = goal.objects.get(id=pk)
    rid.delete()
    userdict = goal.objects.all()
    return render(request, "viewgoal.html", {'userdict': userdict})

def insertgoal(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")

        goal.objects.create(goal_id=s1, user=s2, name=s3, target_amount=s4, target_date=s5 , description=s6 )
        return render(request, "goal.html")
    return render(request, "goal.html")

def viewgoal(request):
    userdict = goal.objects.all()
    return  render(request,"viewgoal.html",{'userdict':userdict})


def insertcategory(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")

        category.objects.create(category_id=s1, name=s2, description=s3)
        return render(request, "category.html")
    return render(request, "category.html")

def category_del(request, pk):
    rid = category.objects.get(id=pk)
    rid.delete()
    userdict = category.objects.all()
    return render(request, "viewcategory.html", {'userdict': userdict})

def viewcategory(request):
    userdict = category.objects.all()
    return  render(request,"viewcategory.html",{'userdict':userdict})

def logcheck(request):
    if request.method == "POST":
        s1 = request.POST.get("t2")
        request.session['username'] = s1
        s2 = request.POST.get("t3")
        ucheck = userlogin.objects.filter(username=s1).count()
        if ucheck >= 1:
            udata = userlogin.objects.get(username=s1)
            upass = udata.password
            utype = udata.utype
            if upass == s2:
                if utype == "admin":
                    return render(request, 'admin_home.html')
                if utype == "user":
                    return render(request, 'user_home.html')
            else:
                return render(request, 'login.html', {'msg': 'invalid password'})
        else:
            return render(request, 'login.html', {'msg': 'invalid username'})
    return render(request, "login.html")

# def newuser(request):
#     return render(request,'newuser.html')

def insertnewuser(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        newuser.objects.create(user_id=s1, username=s2, password=s3, email=s4, first_name=s5, last_name=s6,utype=s7)
        userlogin.objects.create(user_id=s1, username=s2, password=s3,utype=s7)
        return render(request, "newuser.html")
    return render(request, "newuser.html")


def admin_home(request):
    return render(request,"admin_home.html")

def user_home(request):
    return render(request,"user_home.html")