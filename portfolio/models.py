from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    

class Project(models.Model):  
    title = models.CharField(max_length=255) 
    alt = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    image_src = models.ImageField(upload_to='project-images/', default='')

class Portfolio(models.Model):
    title = models.CharField(max_length=50, default='')
    filterOptions = models.ManyToManyField(Category)
    projects = models.ManyToManyField(Project)
    
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Deactivate all other objects if this object is set to active
        if self.is_active:
            Portfolio.objects.exclude(pk=self.pk).update(is_active=False)
        super(Portfolio, self).save(*args, **kwargs)