from django.urls import path
from . import views
from .views import PresentationListView, PresentationDetailView, upload_presentation


urlpatterns = [
    path('', views.VideoListView.as_view(), name='video_list'),
    path('video/<int:pk>/', views.VideoDetailView.as_view(), name='video_detail'),
    path('presentations/', views.PresentationListView.as_view(), name='presentation_list'),
    path('presentations/upload/', views.upload_presentation, name='presentation_upload'),
    path('', PresentationListView.as_view(), name='presentation_feed'),
    path('<int:pk>/', PresentationDetailView.as_view(), name='presentation_detail'),
    path('upload-presentation/', upload_presentation, name='upload_presentation'),
]