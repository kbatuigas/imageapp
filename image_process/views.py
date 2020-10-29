from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UploadImageForm
from .models import ImageFile

import base64

# Create your views here.

def index(request):
    return render(request, 'image_process/index.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved

            uploaded_img = form.save(commit=False)
            uploaded_img.image_data = form.cleaned_data['image'].file.read()
            uploaded_img.save()
            return redirect('/')    # Why didn't 'index' work?
    else:
        form = UploadImageForm()
    return render(request, 'image_process/upload.html', {'form': form})


def browse_images(request):
    # make new imagefile from DB
    img = ImageFile.objects.get(pk=2)
    response = HttpResponse(img.image_data, content_type="image/jpeg")

    return response
