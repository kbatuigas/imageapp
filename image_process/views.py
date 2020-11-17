
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from .forms import UploadImageForm
from .models import ImageFile

import base64
import io

# Create your views here.

def index(request):
    return render(request, 'image_process/index.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Don't save image to DB just yet
            uploaded_img = form.save(commit=False)
            # Read bytes into BinaryField
            uploaded_img.image_data = form.cleaned_data['image'].file.read()
            # Now we can save to DB
            uploaded_img.save()
            return redirect('/')    # Why didn't 'index' work?
    else:
        form = UploadImageForm()
    return render(request, 'image_process/upload.html', {'form': form})


def view_image(request):
    # make new imagefile from DB
    img = ImageFile.objects.get(pk=2)
    response = HttpResponse(img.image_data, content_type="image/jpeg")

    return response


class ImageListView(generic.ListView):
    model = ImageFile
    template_name = 'image_process/browse.html'
    context_object_name = 'images_all'


    def get_context_data(self, *args, **kwargs):
        context = super(ImageListView, self).get_context_data(*args, **kwargs)
        queryset = ImageFile.objects.filter(image_data__isnull=False)
        results = []
        for image_row in queryset:
            enc_image = base64.b64encode(image_row.image_data).decode('utf-8')
            results.append(enc_image)

        context['results'] = results
        return context






