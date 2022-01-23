from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Payments = models.PositiveIntegerField(default=0)
    total_amount = models.IntegerField(default=0)
    phone_number = models.IntegerField(null=True)
    
    def __str__(self):
        return (self.user.username)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    order_id = models.TextField(null=True)
    signature = models.TextField(null=True)
    payment_id = models.TextField(null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return (self.user.username)
    
    