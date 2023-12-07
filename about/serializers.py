from rest_framework import serializers
from .models import About, Client, Service, Testimonial

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'