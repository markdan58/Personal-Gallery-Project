from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Image

# Create your views here.
def displayphoto(request):
    photos = Image.objects.all()
    return render(request,'photopage.html',{"photos":photos})


def details(request,image_id):
    try:
        details = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "details.html", {"details":details})


def search_results(request):

    if 'Image' in request.GET and request.GET["Image"]:
        image = request.GET.get("Image")
        looked_Image = Image.search_category(image)
        message = f"{image}"

        return render(request, 'search.html',{"message":message,"images": looked_Image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
