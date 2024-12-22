from django.urls import path
from . import views

urlpatterns = [
    path('', views.VideoListView.as_view(), name='video_list'),
    path('video/<int:pk>/', views.VideoDetailView.as_view(), name='video_detail'),
    path('presentations/', views.PresentationListView.as_view(), name='presentation_list'),
    path('presentations/upload/', views.upload_presentation, name='presentation_upload'),
]