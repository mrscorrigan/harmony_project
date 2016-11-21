from django.shortcuts import render, HttpResponse, Http404
from django.db import models
from models import ClothingItem
# Create your views here.

def my_styleme(request):
    items = ClothingItem.objects.all()
    return render(request, 'styleme/styleme.html', {"items": items})

def get_welcome(request):
    return render(request, "styleme/welcome.html")

def upload_pic(request):
    # if request.method == 'POST':
        # form = UserPostForm(request.POST, request.FILES)
        # if form.is_valid():
        #     m = Styleme.objects.get(pk=id)
        #     m.image = form.cleaned_data['image']
        #     m.save()
        #     return HttpResponse('image upload success')
    return Http404 ('upload failed')