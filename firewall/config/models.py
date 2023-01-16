from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class FirewallRule(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rule = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class NAT(models.Model):
    protocol = models.CharField(max_length=10)
    source_ip = models.GenericIPAddressField()
    source_port = models.IntegerField()
    destination_ip = models.GenericIPAddressField()
    destination_port = models.IntegerField()
    target_ip = models.GenericIPAddressField()
    target_port = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
