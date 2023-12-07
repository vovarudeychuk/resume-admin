from django.db import models

class Contact(models.Model):
    icon = models.CharField(max_length=50)
    link = models.URLField()
    type = models.CharField(max_length=50)
    value = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.type

class Social(models.Model):
    # name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    link = models.URLField()

    # def __str__(self):
    #     return self.name

class Account(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    contacts = models.ManyToManyField(Contact)
    google_map = models.URLField()
    name = models.CharField(max_length=255)
    resume_pdf = models.URLField()
    socials = models.ManyToManyField(Social)
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Deactivate all other objects if this object is set to active
        if self.is_active:
            Account.objects.exclude(pk=self.pk).update(is_active=False)
        super(Account, self).save(*args, **kwargs)
