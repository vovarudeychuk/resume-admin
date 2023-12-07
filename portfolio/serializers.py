from rest_framework import serializers
from .models import Portfolio, Project, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'alt', 'image_src']
        
class ProjectSerializerList(serializers.Serializer):
    def to_representation(self, instance):
        project_data = ProjectSerializer(instance).data
        category_data = CategorySerializer(instance.category.all().values("name"), many=True).data

        project_combined_data = {
            **project_data,
           'category': extract_names(category_data),
        }
        return project_combined_data

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['title']
              

class PortfolioSerializerList(serializers.Serializer):
    def to_representation(self, instance):
        portfolio_data = PortfolioSerializer(instance).data
        category_data = CategorySerializer(instance.filterOptions.all().values("name"), many=True).data
        project_data = ProjectSerializerList(instance.projects.all(), many=True).data
        
        portfolio_combined_data = {
                **portfolio_data,
                'filterOptions': extract_names(category_data),
                'projects': project_data,
        }

        return portfolio_combined_data 
        
def extract_names(filter_options):
        return [option["name"] for option in filter_options]    