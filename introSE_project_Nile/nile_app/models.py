from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length = 100)
    details = models.CharField(max_length = 500)

class Item(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.name
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
