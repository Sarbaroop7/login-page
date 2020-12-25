from django.db import models

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
    cookies = models.TextField()
    class Meta:
        db_table="login_userlogin"