# map_app/views.py
from django.shortcuts import render, redirect
from .models import Location
from .forms import LocationForm

def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map_view')
    else:
        form = LocationForm()
    
    return render(request, 'add_location.html', {'form': form})


def map_view(request):
    locations = Location.objects.all()
    return render(request, 'map_app/map.html', {'locations': locations})