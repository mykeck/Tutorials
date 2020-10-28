from rest_framework import serializers
from models import Articles



class ArticlesSerializer(serializers.Serializer):
    class Meta:
        model = Articles
        fields = ("title", "author" "email","date")

    def create(self, validate_data):
        return Articles.objects.create(validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get()    
    