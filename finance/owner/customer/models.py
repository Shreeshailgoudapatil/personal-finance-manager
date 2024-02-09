from django.db import models

# Create your models here.

from django.db import models

class userlogin(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(userlogin, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=200)
    type = models.CharField(max_length=10)  # 'income' or 'expense'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

class Budget(models.Model):
    budget_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(userlogin, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    month = models.CharField(max_length=7)  # YYYY-MM format
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Goal(models.Model):
    goal_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(userlogin, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_date = models.DateField()
    description = models.TextField(blank=True)

