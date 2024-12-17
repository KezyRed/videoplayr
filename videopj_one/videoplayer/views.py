from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Video

class VideoListView(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'
    ordering = ['-created_at']

class VideoDetailView(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'
    context_object_name = 'video'