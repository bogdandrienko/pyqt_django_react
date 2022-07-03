from rest_framework import serializers
from . import models


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageModel
        fields = '__all__'
