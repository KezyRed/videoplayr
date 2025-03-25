from django.views.generic import ListView, DetailView
from django.shortcuts import render , redirect, get_object_or_404
from .models import Video , Presentation
from .forms import PresentationForm
from pptx import Presentation as PPTXPresentation
from django.views.generic import ListView, DetailView
from .models import Presentation
# Требуемые библиотеки дял работы с презинтация майкрософт
import os
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pythoncom
import win32com.client
import comtypes.client


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

def upload_presentation(request):
    """
    Представление для загрузки и конвертации презентации PowerPoint
    """
    if request.method == 'POST' and request.FILES['presentation']:
        presentation = request.FILES['presentation']
        fs = FileSystemStorage()
        filename = fs.save(presentation.name, presentation)
        file_path = fs.path(filename)
        
        # Конвертация презентации в изображения
        slides = convert_pptx_to_images(file_path)
        
        return render(request, 'presentation_viewer.html', {
            'slides': slides
        })
    return render(request, 'upload_presentation.html')

def convert_pptx_to_images(file_path):
    """
    Конвертация презентации PowerPoint в изображения слайдов
    """
    # Инициализация COM-библиотек
    pythoncom.CoInitialize()
    
    try:
        # Инициализация PowerPoint
        powerpoint = win32com.client.Dispatch("Powerpoint.Application")
        presentation = powerpoint.Presentations.Open(file_path)
        
        # Папка для сохранения слайдов
        slides_dir = os.path.join(settings.MEDIA_ROOT, 'slides')
        os.makedirs(slides_dir, exist_ok=True)
        
        slides_paths = []
        
        # Экспорт каждого слайда в PNG
        for i, slide in enumerate(presentation.Slides, 1):
            slide_filename = f'slide_{i}.png'
            slide_path = os.path.join(slides_dir, slide_filename)
            slide.Export(slide_path, 'PNG')
            slides_paths.append(os.path.join('slides', slide_filename))
        
        # Закрытие презентации
        presentation.Close()
        powerpoint.Quit()
        
        return slides_paths
    
    except Exception as e:
        print(f"Ошибка конвертации презентации: {e}")
        return []
    finally:
        # Освобождение COM-библиотек
        pythoncom.CoUninitialize()