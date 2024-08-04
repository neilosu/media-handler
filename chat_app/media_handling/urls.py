from django.urls import path
from .views import ImageUploadView, ImageView, ThumbnailView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('image/<str:image_name>/', ImageView.as_view(), name='image-view'),
    path('thumbnail/<str:image_name>/', ThumbnailView.as_view(), name='thumbnail-view'),
]
