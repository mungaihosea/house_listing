from django.shortcuts import render
from .models import Property
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user, logout as logout_user
from django.db.models import Q

def index(request):
    return render(request, 'index.html', {})

def properties(request):
    queryset = Property.objects.all()
    context = {
        "properties": queryset,
    }
    return render(request, 'properties.html', context)

def property_detail(request, id):
    property = get_object_or_404(Property, id = id)
    return render(request, 'listing.html', {"property":property})

def search(request):
    if request.method == "POST":
        print(request.POST)
        keyword = request.POST.get('keyword')
        upper_price = request.POST.get('upper_price', None)
        lower_price = request.POST.get('lower_price', None)
        
        try:
            queryset = Property.objects.filter(Q(title__icontains = keyword) | Q(detail__icontains = keyword) | Q(bond__gt = int(lower_price)) |Q(bond__lt = int(upper_price)))
        except:
            queryset = Property.objects.filter(Q(title__icontains = keyword) | Q(detail__icontains = keyword))

    else:
        queryset = Property.objects.all()
    context = {
        "properties": queryset,
    }
    return render(request, 'searchresults.html', context)

def landlord(request):
    queryset = Property.objects.filter(user = request.user) #get all properties
    return render(request, 'landlord.html', {"properties":queryset})


def sign_up(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST.get('username', None)
        user.email = request.POST.get('email', None)
        user.set_password(request.POST.get('password'))
        user.save()
        login_user(request, user)
        return redirect('index')
    return render(request, 'sign_up.html', {})

def login(request):
    error = None
    if request.method == "POST":
        print(request.POST)
        try:
            user = User.objects.get(username = request.POST.get('username'))
            if user.check_password(request.POST.get("password")):
                login_user(request, user)
                return redirect("index")
        except Exception as e:
            error = "Invalid login credentials"
            print(e)
        
    return render(request, 'login.html', {"error":error})

def logout(request):
    logout_user(request)
    return redirect('login')

def edit_property(request, id):
    p = get_object_or_404(Property, id = id)
    if request.method == "POST":
        try:
            property = Property.objects.get(id = id)
            property.title = request.POST.get('title')
            property.detail = request.POST.get('detail')
            property.email = request.POST.get('email')
            property.bond = request.POST.get('bond')
            if request.FILES:
                print(request.FILES)
                property.image = request.FILES.get('image')

            property.save()
            return redirect('landlord')
        except Exception as e:
            print(e)
    return render(request, 'edit_property.html', {'property':p})

def add_property(request):
    if request.method == "POST":
        property = Property()
        property.user = request.user
        property.title = request.POST.get('title')
        property.detail = request.POST.get('detail')
        property.email = request.POST.get('email')
        property.bond = request.POST.get('bond')
        if request.FILES:
            print(request.FILES)
            property.image = request.FILES.get('image')
        property.save()

        return redirect('landlord')
    return render(request, 'create_property.html', {})

def remove_property(request, id):
    p = get_object_or_404(Property, id = id)
    p.delete()
    return redirect('landlord')