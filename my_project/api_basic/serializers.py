from rest_framework import serializers
from .models import Article

"""
USING MODEL SERIALIZERS
"""

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'