"""owner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from django.shortcuts import get_object_or_404

from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # url("login", views.insertlogin, name="login"),
    # url("transaction", views.transaction, name="transaction"),
    #url("insertlogin", views.insertlogin, name="insertlogin"),
    url("inserttransaction", views.inserttransaction, name="inserttransaction"),
    url("insertbudget", views.insertbudget, name="insertbudget"),
    url("insertcategory", views.insertcategory, name="insertcategory"),
    url("insertgoal", views.insertgoal, name="insertgoal"),
    url("^$",views.index,name="index"),


    url("viewlogin", views.viewlogin, name="viewlogin"),
    url("login_del/(?P<pk>\d+)/$", views.login_del, name="login_del"),

    url("viewtransaction", views.viewtransaction, name="viewtransaction"),
    url("transaction_del/(?P<pk>\d+)/$", views.transaction_del, name="transaction_del"),

    url("viewbudget", views.viewbudget, name="viewbudget"),
    url("budget_del/(?P<pk>\d+)/$", views.budget_del, name="budget_del"),


    url("viewgoal", views.viewgoal, name="viewgoal"),
    url("goal_del/(?P<pk>\d+)/$", views.goal_del, name="goal_del"),


    url("viewcategory", views.viewcategory, name="viewcategory"),
    url("category_del/(?P<pk>\d+)/$", views.category_del, name="category_del"),

    url("logcheck", views.logcheck, name="logcheck"),
    # url("newuser", views.newuser, name="newuser"),
    url("insertnewuser", views.insertnewuser, name="insertnewuser"),

    url("user_home", views.user_home, name="user_home"),
    url("admin_home", views.admin_home, name="admin_home"),







]
