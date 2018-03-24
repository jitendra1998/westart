from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StartUps(models.Model):
    start_up_name = models.CharField(max_length=256)
    start_up_description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.start_up_name

   



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_stratup = models.TextField(blank=True, null=True)
    applied_startup = models.TextField(blank=True, null=True)
    mobile = models.IntegerField()
    address = models.TextField(blank=True, null=True)




