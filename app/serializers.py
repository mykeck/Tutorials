from rest_framework import serializers
from .models import Articles



class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ("title", "author", "email","date","pk")

    def create(self, validate_data):
        return Articles.objects.create(validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.author = validated_data.get('author',instance.author) 
        instance.email = validated_data.get('email',instance.author) 
        instance.date = validated_data.get('date',instance.author)   
        instance.save()
        return instance 
    