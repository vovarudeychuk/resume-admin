from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    place = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()

class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=20, null=True, blank=True)

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Skill(models.Model):
    title = models.CharField(max_length=255, unique=True)
    percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)

class Cv(models.Model):
    title = models.CharField(max_length=255)
    skills_title = models.CharField(max_length=255)
    education = models.ManyToManyField(Education)
    experience = models.ManyToManyField(Experience)
    skills = models.ManyToManyField(Skill)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Deactivate all other objects if this object is set to active
        if self.is_active:
            Cv.objects.exclude(pk=self.pk).update(is_active=False)
        super(Cv, self).save(*args, **kwargs)