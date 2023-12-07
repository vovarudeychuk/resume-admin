from django.db import models
from tinymce import models as tinymce_models


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='testimonial-images/')
    content = models.CharField(max_length=250, default="")

class Service(models.Model):
    title = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='service-images/')
    text = models.CharField(max_length=250, default="")
    
class Client(models.Model):
    name = models.CharField(max_length=250, default="")
    description = tinymce_models.HTMLField()
    logo = models.ImageField(upload_to='client-images/')

class About(models.Model):
    about_text = tinymce_models.HTMLField()
    clients = models.ManyToManyField(Client)
    services = models.ManyToManyField(Service)
    testimonials = models.ManyToManyField(Testimonial)    
    is_active = models.BooleanField(default=False)
