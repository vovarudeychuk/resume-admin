from django.db import models
from tinymce import models as tinymce_models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    image_alt = models.CharField(max_length=255)
    image_src = models.ImageField(upload_to='blog-images/')
    text = tinymce_models.HTMLField()
    category = models.ManyToManyField(Category)
    is_active = models.BooleanField(default=False)