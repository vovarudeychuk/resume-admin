from rest_framework import serializers
from .models import Cv, Education, Experience, Skill

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields = ['id', 'title']

    
class CvSerializerList(serializers.Serializer):
    def to_representation(self, instance):
        cv_data = CvSerializer(instance).data
        education_data = EducationSerializer(instance.education.all(), many=True).data
        experience_data = ExperienceSerializer(instance.experience.all(), many=True).data
        skills_data = SkillsSerializer(instance.skills.all(), many=True).data

        # Combine all data directly under the 'cv' key
        cv_combined_data = {
                **cv_data,
                'education': education_data,
                'experience': experience_data,
                'skills': skills_data,
        }

        return cv_combined_data