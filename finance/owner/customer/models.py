from django.db import models

# Create your models here.

from django.db import models

class newuser(models.Model):
    user_id = models.CharField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=200,null=True,blank=True)
    password = models.CharField(max_length=200,null=True,blsank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    utype = models.CharField(max_length=200, null=True, blank=True)


class userlogin(models.Model):
    user_id = models.CharField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=200,null=True,blank=True)
    password = models.CharField(max_length=200,null=True,blank=True)
    utype = models.CharField(max_length=200, null=True, blank=True)



class transaction(models.Model):
    transaction_id = models.CharField(max_length=200,null=True,blank=True)
    user = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateField(max_length=200,null=True,blank=True)
    amount = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    category = models.CharField(max_length=200,null=True,blank=True)
    type = models.CharField(max_length=200,null=True,blank=True) # 'income' or 'expense'

class category(models.Model):
    category_id = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)

class budget(models.Model):
    budget_id = models.CharField(max_length=200,null=True,blank=True)
    user = models.CharField(max_length=200,null=True,blank=True)
    category = models.CharField(max_length=200,null=True,blank=True)
    month = models.DateField(null=True,blank=True)  # YYYY-MM format
    amount = models.CharField(max_length=200,null=True,blank=True)

class goal(models.Model):
    goal_id = models.CharField(max_length=200,null=True,blank=True)
    user = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    target_amount = models.CharField(max_length=200,null=True,blank=True)
    target_date = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)

