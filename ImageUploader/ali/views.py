from django.shortcuts import render
from .forms import imageform
from django.contrib import messages
from .models import myimage
# Create your views here.
def imageview(request):
    if request.method == "POST":
        form = imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Images uploaded Successfully")
    else:
     form = imageform()
     img = myimage.objects.all()
    return render(request, 'ali/home.html', {'form': form, 'img':img})