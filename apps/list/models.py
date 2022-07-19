from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class List(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class ListItem(models.Model):
    all_list = models.ForeignKey(List, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.text
