from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ImageUpload
from .serializers import ImageUploadSerializer

class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response("Upload successfully!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import HttpResponse
from .models import ImageUpload

class ImageView(APIView):
    def get(self, request, image_name):
        try:
            image = ImageUpload.objects.get(image_name=image_name)
            return HttpResponse(image.image, content_type='image/png')
        except ImageUpload.DoesNotExist:
            return HttpResponse(status=404)