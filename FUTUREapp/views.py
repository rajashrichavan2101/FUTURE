

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

     return render(request, 'places_form.html')


 # UPDATE
def places_update(request, id):
    places =get_object_or_404(Places, id=id)

    if request.method == 'POST':
      places.title = request.POST['title']
      places.location = request.POST['location']
      places.description = request.POST['description']
        
    if 'image' in request.FILES:
             places.image = request.FILES['image']
             places.save()
             return redirect('places_list')

             return render(request, 'places_form.html', {'places': places})


 # DELETE
def places_delete(request, id):
     places = get_object_or_404(Places, id=id)
     places.delete()
     return redirect('places_list')