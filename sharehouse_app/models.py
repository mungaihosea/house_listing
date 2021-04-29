from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length = 30)
    detail = models.TextField()
    bond = models.IntegerField()
    email = models.EmailField()
    date = models.CharField(max_length = 30)
    image = models.ImageField(null = True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"