from rest_framework import serializers
from .models import Account, Contact, Social

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'avatar', 'title', 'resume_pdf', 'google_map']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'

class CombinedAccountSerializer(serializers.Serializer):
    def to_representation(self, instance):
        account_data = AccountSerializer(instance).data
        contact_data = ContactSerializer(instance.contacts.all(), many=True).data
        socials_data = SocialSerializer(instance.socials.all(), many=True).data

        combined_data = {
                **account_data,
                'contacts': contact_data,
                'socials': socials_data
        }
        
        return combined_data
            
