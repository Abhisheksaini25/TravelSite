from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import os,json
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

#@login_required(login_url='login')
def Home(request):
    gallery_folder = os.path.join(settings.MEDIA_ROOT, 'gallery')
    try:
        images = [f for f in os.listdir(gallery_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    except FileNotFoundError:
        images = []

    return render(request, 'home.html', {'gallery_images': images})

def logout_page(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')


def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

@login_required(login_url='login')
def plan_trip(request):
    return render(request,'bookatrip.html')


def trip(request):
    if request.method == "POST":
        city = request.POST.get('city')
        day = int(request.POST.get('days'))

        if city is None or day is None:
            messages.error(request, "Please fill out the trip form before viewing your plan.")
            return redirect('plan')
        #activities = [request.POST.get(f'activity_day_{i}', '') for i in range(1, days + 1)]

        days = [
            {"day_number": 1, "description": "Explore Gateway of India and nearby",
             "image_url": "/static/avi/day1.jpg"},
            {"day_number": 2, "description": "Visit Elephanta Caves and Chowpatty Beach",
             "image_url": "/static/avi/day2.jpg"},
            # etc.
        ]

        return render(request, 'showtrip.html',{
            'days': days,
            'city': city
        })
    else:
        messages.error(request, "Please fill out the trip form before viewing your plan.")
        return redirect('plan')


def hotels(request):
    path = os.path.join(settings.BASE_DIR, 'static', 'data', 'hotels')
    data = open(path, "r")
    hotel_string = data.read()
    hotel_ls = hotel_string.split('\n')
    hotel_list = []
    for i in hotel_ls:
        hotel_list.append(i.split(','))
    hotel_data = []
    for i in hotel_list:
        di = {}
        di['name'] = i[0]
        di['city'] = i[1]
        di['price'] = i[2]
        di['image'] = i[3]
        hotel_data.append(di)
    data.close()

    cities = sorted(list(set([hotel['city'] for hotel in hotel_data])))

    # get selected city from GET parameter if available
    selected_city = request.GET.get('city', 'all').lower()

    return render(request, 'hotel.html', {
        'hotels': hotel_data,
        'cities': cities,
        'selected_city': selected_city,
    })


def restaurants(request):
    path = os.path.join(settings.BASE_DIR, 'static', 'data', 'restaurants')
    data = open(path, "r")
    rst_string = data.read()
    rst_ls = rst_string.split('\n')
    rst_list = []
    for i in rst_ls:
        rst_list.append(i.split(','))
    rst_data = []
    for i in rst_list:
        di = {}
        di['name'] = i[0]
        di['city'] = i[1]
        di['rating'] = i[2]
        di['services'] = [i[3], i[4], i[5], i[6]]
        di['price'] = i[7]
        di['image_url'] = i[8]
        rst_data.append(di)
    data.close()

    selected_city = request.GET.get('city', 'all')

    cities = sorted({r['city'] for r in rst_data})

    return render(request, 'restaurant.html', {
        'restaurants': rst_data,
        'cities': cities,
        'selected_city': selected_city,
    })


def gallery(request):
    data_file = os.path.join(settings.BASE_DIR, 'gallery_data.txt')
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            destinations = json.loads(file.read())
    else:
        destinations = []
    return render(request, 'gallery.html', {'destinations': destinations})

def add_photo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        image = request.FILES['image']

        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'gallery'))
        #fs = FileSystemStorage(location=os.path.join('media/gallery'))
        filename = fs.save(image.name, image)
        image_url = fs.url('gallery/' + filename)

        data_file = os.path.join(settings.BASE_DIR, 'gallery_data.txt')
        if os.path.exists(data_file):
            with open(data_file, 'r') as file:
                destinations = json.loads(file.read())
        else:
            destinations = []

        destinations.append({
            'name': name,
            'city': city,
            'image': image_url,
        })

        with open(data_file, 'w') as file:
            file.write(json.dumps(destinations, indent=4))

        return JsonResponse({'success': True, 'name': name, 'city': city, 'image': image_url})


@login_required
def change_password(request):
    if request.method == 'POST':
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if new_password1 == new_password2:
            user = request.user
            user.set_password(new_password1)
            user.save()
            update_session_auth_hash(request, user)  # Keep user logged in
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Passwords do not match.'})

    return JsonResponse({'success': False, 'error': 'Invalid request.'})

def test(request):
    gallery_folder = os.path.join(settings.MEDIA_ROOT, 'gallery')
    try:
        images = [f for f in os.listdir(gallery_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    except FileNotFoundError:
        images = []

    return render(request, 'home.html', {'gallery_images': images})