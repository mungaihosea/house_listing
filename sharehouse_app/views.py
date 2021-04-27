from django.shortcuts import render
from .models import Property
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'index.html', {})

def properties(request):
    queryset = Property.objects.all()
    context = {
        "properties": queryset,
    }
    return render(request, 'searchresults.html', context)

def property_detail(request, id):
    property = get_object_or_404(Property, id = id)
    return render(request, 'listing.html', {"property":property})

def search(request):
    queryset = Property.objects.all()
    context = {
        "properties": queryset,
    }
    return render(request, 'searchresults.html', context)

def landlord(request):
    if request.method == "POST":

        property = Property()
        property.name = request.POST.get('name')
        property.title = request.POST.get('title')
        property.detail = request.POST.get('detail')
        property.email = request.POST.get('email')
        property.bond = request.POST.get('bond')
        property.date = request.POST.get('date')
        if request.FILES:
            print(request.FILES)
            property.image = request.FILES.get('image')

        property.save()

    return render(request, 'landlord.html', {})
    