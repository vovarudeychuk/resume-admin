from rest_framework import serializers
from .models import About, Client, Service, Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Testimonial
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Service
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Client
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):    
    class Meta:
        model = About
        fields = ['about_text']

class AboutSerializerList(serializers.Serializer):
    def to_representation(self, instance):
        
        about = AboutSerializer(instance).data 
        clients = ClientSerializer(instance.clients.all(), many=True).data
        services = ServiceSerializer(instance.services.all(), many=True).data
        testimonials = TestimonialSerializer(instance.testimonials.all(), many=True).data

        print(about)
        combined_data = {
                **about,
                'clients': clients,
                'services': services,
                'testimonials': testimonials
        }    
        
        return combined_data