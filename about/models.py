from django.db import models
from tinymce import models as tinymce_models


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='testimonial-images/')
    content = models.CharField(max_length=250, default="")
    
    def __str__(self):
        return self.name   

class Service(models.Model):
    title = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='service-images/')
    text = models.CharField(max_length=250, default="")
    
    def __str__(self):
        return self.title  
    
class Client(models.Model):
    name = models.CharField(max_length=250, default="")
    description = tinymce_models.HTMLField()
    logo = models.ImageField(upload_to='client-images/')
    
    def __str__(self):
        return self.name   

class About(models.Model):
    about_text = models.TextField(default='')
    clients = models.ManyToManyField(Client)
    services = models.ManyToManyField(Service)
    testimonials = models.ManyToManyField(Testimonial)    
    is_active = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        # Deactivate all other objects if this object is set to active
        if self.is_active:
            About.objects.exclude(pk=self.pk).update(is_active=False)
        super(About, self).save(*args, **kwargs)