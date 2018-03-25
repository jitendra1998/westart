from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class StartUps(models.Model):
#    start_up_name = models.CharField(max_length=256)
#    start_up_description = models.TextField(blank=True, null=True)
#    start_up_members = models.TextField(blank=True, null=True)
#    start_up_skills_req = models.TextField(blank=True, null=True)
#    start_up_sal = models.IntegerField()
#
#
#    def __str__(self):
#        return self.start_up_name

class Sessionpart(models.Model):
    username = models.CharField(max_length=256)
    def __str__(self):
        return self.username


class UserDetails(models.Model):
    username = models.CharField(max_length=256,primary_key=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    type = models.IntegerField(null=True)

    def __str__(self):
        return self.username

class StartUps(models.Model):
    start_up_username = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    start_up_name = models.CharField(max_length=256)
    start_up_description = models.CharField(max_length=256)

    def __str__(self):
        return self.start_up_name

class Menudetails(models.Model):
    Menu_start_up_name = models.CharField(max_length=256)
    Menu_start_up_item = models.CharField(max_length=256)
    Menu_start_up_item_price = models.IntegerField()
    # Menu_image = models.ImageField(upload_to='food_img',blank=True)

    def __str__(self):
        return self.Menu_start_up_item


class Orderdetails(models.Model):
    user_name = models.CharField(max_length=256)
    order_start_up_name = models.CharField(max_length=256)
    order_item = models.CharField(max_length=256)
    order_price = models.CharField(max_length=256)

    # def __str__(self):
    #     return self.order_item + self.order_price

# class Profile(models.Model):
#     username = models.CharField(max_length=250)
#     password = models.CharField(max_length=250)
#     email = models.CharField(max_length=250, default="n")
#
#
#    #
#    # user = models.OneToOneField(User, on_delete=models.CASCADE)
#    # current_stratup = models.TextField(blank=True, null=True)
#    # applied_startup = models.TextField(blank=True, null=True)
#    # mobile = models.IntegerField()
#    # address = models.TextField(blank=True, null=True)
#
#
# class Ventures(models.Model):
#
#    ventures_name = models.TextField(blank=True, null=True)
#    ventures_description = models.TextField(blank=True, null=True)
#
#
# class Ventures_Request(models.Model):
#    ventures_request_start_up_name = models.TextField(blank=True, null=True)
#    ventures_request_USP = models.TextField(blank=True, null=True)
#    ventures_request_Amount = models.IntegerField()
