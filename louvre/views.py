from django.shortcuts import render
from .models import Category, Location, Image
# Create your views here.

def index(request):
    '''
    View function for louvre app
    '''
    return render(request, 'about.html')

def gallery(request):
    '''
    Test gallery
    '''
    images = Image.objects.all()
    location = Location.find_location()
    category = Category.find_by_category()


    return render(request, 'gallery.html', {'images':images, 'location':location, 'categorys':category})

def find_image_location(request, location):
    '''
    View function on modal display
    '''
    images = Image.objects.filter(location_name=location)

    return render(request, 'location.html', {'location_images': images})

def search(request):
    '''
    View function that enables search
    '''
    if 'image' in request.GET and request.GET['image']:
        category = request.GET.get("image")
        found_images = Image.find_image_by_category(category)
        message = f"{category}"

        return render(request, 'search.html', {'message': message, 'images':found_images})
    else:
        message = 'Category not found'
        return render(request, 'search.html', {'message': message})
