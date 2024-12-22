from django.views.generic import ListView, DetailView
from django.shortcuts import render , redirect
from .models import Video , Presentation
from .forms import PresentationForm
from pptx import Presentation as PPTXPresentation

# Create your views here.
class VideoListView(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'
    ordering = ['-created_at']

class VideoDetailView(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'
    context_object_name = 'video'

class PresentationListView(ListView):
    model = Presentation
    template_name = 'videoplayer/presentation_list.html'
    context_object_name = 'presentations'

def upload_presentation(request):
    if request.method == 'POST':
        form = PresentationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('presentation_list')
    else:
        form = PresentationForm()
    return render(request, 'videoplayer/presentation_upload.html', {'form': form})