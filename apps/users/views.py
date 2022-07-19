from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

from .models import MyUser

# Create your views here.


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
