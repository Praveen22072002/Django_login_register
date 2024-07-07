from django.db import models

class Signup(models.Model):
    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    username = models.CharField(max_length=32, unique=True, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    password = models.CharField(max_length=32, blank=False)
    repassword = models.CharField(max_length=32, blank=False)
    address_line_1 = models.CharField(max_length=255, default='Default Address Line 1')
    city = models.CharField(max_length=100, default='Default City')
    state = models.CharField(max_length=100, default='Default State')
    pincode = models.CharField(max_length=10, default='Default Pincode')

    def __str__(self):
        return "{}".format(self.first_name)


class DocSignup(models.Model):
    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    empid = models.CharField(max_length=10, blank=False)
    username = models.CharField(max_length=32, unique=True, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    password = models.CharField(max_length=32, blank=False)
    repassword = models.CharField(max_length=32, blank=False)
    address_line_1 = models.CharField(max_length=255, default='Default Address Line 1')
    city = models.CharField(max_length=100, default='Default City')
    state = models.CharField(max_length=100, default='Default State')
    pincode = models.CharField(max_length=10, default='Default Pincode')

    def __str__(self):
        return "{}".format(self.first_name)
