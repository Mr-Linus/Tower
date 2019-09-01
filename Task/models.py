from django.db import models
from User.models import User
# Create your models here.


class Namespace(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='Created Time')

