from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
    

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)