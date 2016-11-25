from django.shortcuts import render, get_object_or_404, Http404, HttpResponse, redirect, reverse
from django.db import models
from models import ClothingItem, Outfit
from django.contrib.auth.decorators import login_required
from forms import UserPostForm
# Create your views here.

@login_required(login_url='/login/')
def my_styleme(request):
    items = ClothingItem.objects.filter(owner_id=request.user.id)
    outfit_count = len(request.user.outfits.all())
    form = UserPostForm()
    return render(request, 'styleme/styleme.html', {"items": items, "outfit_count": outfit_count, 'form': form})

@login_required(login_url='/login/')
def users_outfits(request):
    outfits = Outfit.objects.filter(owner_id=request.user.id)
    return render(request, 'styleme/outfits.html', {"outfits": outfits})


def outfit_items(request, id):
    outfit = get_object_or_404(Outfit, pk = id)
    return render(request, "styleme/outfit_details.html", {"outfitItems": outfit.items.all})

def get_welcome(request):
    return render(request, "styleme/welcome.html")

def upload_pic(request):
    if request.method == 'POST':
        form = UserPostForm(request.POST, request.FILES)
        if form.is_valid():
            outfit=form.save(commit=False)
            outfit.owner=request.user
            outfit.save()
        return redirect(reverse("styleme"))




#
# def outfit_details(request):
#     outfit_details=Outfit.objects.all()
#     return render(request,"styleme/outfit_details.html",{"outfit_details": outfit_details})