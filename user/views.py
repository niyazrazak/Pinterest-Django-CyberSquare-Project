from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import NewUserForm
from .models import *
# Create your views here.


def fnIndex(request):
    form = NewUserForm
    try:
        pin = Post.objects.all()
    except:
        pin = ''
    context = {"form": form, "pin": pin}
    return render(request, 'index.html', context)


def fnSignUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.add_message(request, messages.INFO,
                                     'Email already Exists.')
                messages.error(
                    request, 'Email is Already Exists Try Another Email')
                return redirect("index")
            else:
                user = form.save()
                print("User Created")
                messages.success(
                    request, 'Accounts Created Successfully')
                return redirect("index")
    return redirect("index")


def fnSignIn(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        user = User.objects.filter(email=email, password=password).exists()
        if user:
            user = User.objects.get(email=email, password=password)
            request.session['log'] = user.id
            User.objects.get(id=user.id)
            print("Logged In")
            return redirect('userhome')
        else:
            return render(request, 'index.html', {'mes': 'Error : Wrong Username/Password'})
    return redirect("index")


def fnMain(request):
    return render(request, 'main.html')


def fnHome(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    try:
        pin = Post.objects.all()
    except:
        pin = ''
    context = {"pin": pin}
    return render(request, 'userhome.html', context)


def fnMypost(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    try:
        pin = Post.objects.filter(user=user_id).all()
    except:
        pin = ''
    context = {"pin": pin}
    print("pin")
    return render(request, 'mypost.html', context)


def fnAddpost(request):
    user_id = request.session['log']
    return render(request, 'addpost.html')


def fnAddPin(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        img = request.FILES['image']
        title = request.POST['title']
        caption = request.POST['caption']
        brief = request.POST['brief']
        print(img, title, caption, brief)
        Post.objects.create(img=img, title=title,
                            caption=caption, brief=brief, user=user)
        messages.success(request, 'Post uploaded sucessfully')
        return redirect('mypost')
    return redirect('addpost')


def fnEditPin(request, pid):
    try:
        pinid = Post.objects.filter(id=pid).get(id=pid)
    except:
        pinid = ''
    context = {'pin': pinid}
    return render(request, 'editpost.html', context)


def fnEditPost(request, pid):
    if request.method == 'POST':
        title = request.POST['title']
        caption = request.POST['caption']
        brief = request.POST['brief']
        print(title, caption, brief)
        Post.objects.filter(id=pid).update(title=title,
                                           caption=caption, brief=brief)
        messages.success(
            request, 'Post Updated Successfully')
        return redirect('mypost')
    return redirect('mypost')


def fnDeletePin(request, pid):
    Post.objects.filter(id=pid).delete()
    messages.success(
        request, 'Post Deleted Successfully')
    return redirect('mypost')


def fnReadPost(request, pid):
    try:
        pinid = Post.objects.filter(id=pid).get(id=pid)
    except:
        pinid = ''
    context = {'pin': pinid}
    return render(request, 'readpost.html', context)


def fnProfile(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    try:
        pin = Post.objects.filter(user=user_id).count()
    except:
        pin = ''
    context = {'user': user, 'pin': pin}
    return render(request, 'myprofile.html', context)


def fnLogout(request):
    logout(request)
    return redirect('index')
