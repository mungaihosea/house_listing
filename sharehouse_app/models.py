from django.db import models

class Property(models.Model):
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