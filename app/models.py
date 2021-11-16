from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(null=True, max_length=200)
    def __str__(self):
        return self.user.username
    @property
    def full_name(self):
        return self.user.first_name + ' ' +self.user.last_name
class Categories(models.Model):
    category_name=models.CharField(null=False, max_length=200)
    description=models.CharField(null=False, max_length=100)
    def __str__(self):
        return self.category_name
class Services(models.Model):
    services=models.CharField(max_length=300, null=False)
    price=models.FloatField(null=False)
    pick_up_location = models.CharField(max_length=100, null=True)
    drop_location = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.services
class News(models.Model):
    news=models.CharField(max_length=500, null=True)
    image = models.ImageField(null=True)
    news_date=models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ' '
    def __str__(self):
        return self.news
class Complaints(models.Model):
    customer_name=models.OneToOneField(User, on_delete=models.CASCADE)
    message=models.CharField(max_length=300,null=True)
    def __str__(self):
        return self.user.username
class Orders(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    pick_up_location=models.CharField(max_length=100, null=True)
    drop_location = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=30, null=False)

class Payment(models.Model):
    pay_type={
        ("Naqd", "Naqd"),
        ("PaymeGo", "PaymeGo"),
        ("Uzcard", "Uzcard"),
        ("Click", "Click"),
        ("Humo", "Humo")
    }
    pay_customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True )
    pay_date=models.DateTimeField(auto_now_add=True)
    payment=models.CharField(max_length=20, choices=pay_type)
