from rest_framework import serializers
from .models import ImageUpload

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ('image', 'uploaded_at', 'image_name')

    def create(self, validated_data):
        file = self.context['request'].FILES['image']
        validated_data['image'] = file.read()
        validated_data['image_name'] = file.name
        return super().create(validated_data)
