#from django.shortcuts import render

# Create your views here.


# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .models import Places

# READ – show all places
def places_list(request):
    places = Places.objects.all()
    return render(request, 'FUTUREapp/places.html',{'places': places})
def about(request):
    return render(request, 'FUTUREapp/about.html')
def contact(request):
    return render(request, 'FUTUREapp/contact.html')
def blog(request):
    return render(request, 'FUTUREapp/blog.html')
def mainPage(request):
    return render(request, 'FUTUREapp/index.html')


 # CREATE
def places_create(request):
     if request.method == 'POST':
        Places.objects.create(
             title=request.POST['title'],
            location=request.POST['location'],
            description=request.POST['description'],
            image=request.FILES['image'],
        )
        return redirect('places_list')

     return render(request, 'FUTUREapp/places_form.html')



 # UPDATE
def places_update(request, id):
    place = get_object_or_404(Places, id=id)

    if request.method == 'POST':
        place.title = request.POST['title']
        place.location = request.POST['location']
        place.description = request.POST['description']

        if 'image' in request.FILES:
            place.image = request.FILES['image']

        place.save()
        return redirect('places_list')

    return render(request, 'FUTUREapp/places_form.html', {'place': place})

 # DELETE
def places_delete(request, id):
     places = get_object_or_404(Places, id=id)
     places.delete()
     return redirect('places_list')