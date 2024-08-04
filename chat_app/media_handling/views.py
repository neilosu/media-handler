from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ImageUpload
from .serializers import ImageUploadSerializer
from django.http import HttpResponse
from PIL import Image
from io import BytesIO
from django.http import JsonResponse


class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            response_data = {'image_name': request.FILES['image'].name}
            return JsonResponse(response_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import HttpResponse
from .models import ImageUpload

class ImageView(APIView):
    def get(self, request, image_name):
        try:
            image_record = ImageUpload.objects.get(image_name=image_name)
            return HttpResponse(image_record.image, content_type='image/png')
        except ImageUpload.DoesNotExist:
            return HttpResponse(status=404)

class ThumbnailView(APIView):
    def get(self, request, image_name):
        try:
            image_record = ImageUpload.objects.get(image_name=image_name)
            image = Image.open(BytesIO(image_record.image))
            
            # Create thumbnail
            thumbnail_size = (100, 100)
            image.thumbnail(thumbnail_size)
            thumb_io = BytesIO()
            image.save(thumb_io, format='PNG')
            thumb_io.seek(0)

            return HttpResponse(thumb_io.read(), content_type='image/png')
        except ImageUpload.DoesNotExist:
            return HttpResponse(status=404)
