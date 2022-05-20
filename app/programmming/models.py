from pyexpat import model
from django.db import models
from pkg_resources import require
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200 , blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name

class Massage(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    massage = models.TextField(max_length=2500)
    file = models.FileField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return self.name

class Comment(models.Model):
    user_comments = models.ForeignKey(Massage, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    comment = models.TextField(max_length=2500)
    def __str__(self):
        return self.comment