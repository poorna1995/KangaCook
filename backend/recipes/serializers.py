# # recipes/serializers.py
# from rest_framework import serializers
# from .models import Recipe

# class RecipeSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Recipe
#         fields = ['id', 'title', 'description', 'image_url', 'category']





from django.conf import settings
from rest_framework import serializers
from django.urls import reverse
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField()  # Get the image URL dynamically

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'image_url', 'category']

    def get_image_url(self, obj):
        """Return the absolute URL of the image."""
        if obj.image_url: 
            return settings.STATIC_URL + obj.image_url  # Combine the static URL with the relative path
        else:
            return None  # Or return a default image URL