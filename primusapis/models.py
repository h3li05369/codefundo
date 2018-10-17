from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
status_choice=(
    ('U','unknown'),
    ('S','safe')
    )

class Device(models.Model):
    user_type = models.CharField(max_length=20, default="", blank=True)
    device_id = models.TextField()

    def __str__(self):
        return self.device_id


class Client(models.Model):
    name = models.CharField(max_length=100, default="Durgesh")
    address = models.TextField(max_length=300, blank=True)
    email = models.EmailField(blank=True)
    mobile = models.IntegerField(blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    log = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    gender = models.CharField(choices=GENDER_CHOICES,default='M',max_length=10)
    status = models.CharField(choices=status_choice,default='U',max_length=10)
    device = models.OneToOneField(Device, null=True, related_name='client' , on_delete=models.CASCADE)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True)
    following = models.TextField(max_length=1000,default='[9760839890]',null=True)

    def __str__(self):
        return self.name







        