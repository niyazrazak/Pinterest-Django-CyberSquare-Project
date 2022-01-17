from select import select
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewUserForm
from .models import *
# Create your views here.


def fnHead(request):
    form = NewUserForm
    context = {"form": form}
    return render(request, 'head.html', context)


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


def fnReadOnly(request, pid):
    form = NewUserForm
    try:
        pinid = Post.objects.filter(id=pid).get(id=pid)
    except:
        pinid = ''
    try:
        stuff = get_object_or_404(Post, id=pid)
        totalLikes = stuff.total_likes()
    except:
        totalLikes = ''
    try:
        comment = Comment.objects.filter(post_id=pid).all().select_related()
    except:
        comment = ''
    context = {'pin': pinid, 'likes': totalLikes,
               'comment': comment, "form": form}
    return render(request, 'readonly.html', context)


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
    try:
        stuff = get_object_or_404(Post, id=pid)
        totalLikes = stuff.total_likes()
    except:
        totalLikes = ''
    try:
        comment = Comment.objects.filter(post_id=pid).all().select_related()
    except:
        comment = ''
    context = {'pin': pinid, 'likes': totalLikes, 'comment': comment}
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


def fnComments(request, pk):
    try:
        if request.method == 'POST':
            user_id = request.session['log']
            user = User.objects.get(id=user_id)
            comment = request.POST.get('comment_post')
            print(comment)
            print(type(pk))
            qrytest = Comment(comment=comment, user=user, post_id=pk)
            qrytest.save()
            return HttpResponseRedirect(reverse('readpin', args=[str(pk)]))
    except:
        return HttpResponseRedirect(reverse('readpin', args=[str(pk)]))


def fnLogout(request):
    logout(request)
    return redirect('index')


def BlogPostLike(request, pk):
    try:
        user_id = request.session['log']
        post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
        # print(pk, user_id)
        # if post.likes.filter(user_id=user_id).exists():
        #     print("remove")
        #     # post.likes.remove(user_id)
        # else:
        post.likes.add(user_id)
        return HttpResponseRedirect(reverse('readpin', args=[str(pk)]))
    except:
        print("Except worked")
        return HttpResponseRedirect(reverse('readpin', args=[str(pk)]))
