from rest_framework import serializers

from .models import Blog
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = User
        fields = '__all__'



class BlogSerializer() : 
    title = serializers.CharField()
    content = serializers.CharField()
    crated = serializers.DateTimeField()


class BlogModelSerializer(serializers.ModelSerializer) :
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Blog
        fields = '__all__'
        depth = 1
        