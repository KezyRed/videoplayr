from django.views.generic import ListView, DetailView
from django.shortcuts import render , redirect, get_object_or_404
from .models import Video , Presentation
from .forms import PresentationForm
from pptx import Presentation as PPTXPresentation
from django.views.generic import ListView, DetailView
from .models import Presentation


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
    template_name = 'presentations/feed.html'
    context_object_name = 'presentations'
    paginate_by = 10  # 10 презентаций на страницу
    def get_queryset(self):
        # Сортировка по дате создания в убывающем порядке
        return Presentation.objects.order_by('-created_at')

class PresentationDetailView(DetailView):
    model = Presentation
    template_name = 'presentations/detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Увеличиваем счетчик просмотров
        obj.views_count += 1
        obj.save()
        return obj

def upload_presentation(request):
    if request.method == 'POST':
        form = PresentationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('presentation_list')
    else:
        form = PresentationForm()
    return render(request, 'videoplayer/presentation_upload.html', {'form': form})