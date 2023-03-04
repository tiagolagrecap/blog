from django import http
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Post
from django.shortcuts import render, redirect
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect('/')

    context = {'posts': posts, 'form': form}
    return render(request, 'blog/index.html', context)


def post_view(request, pk):
    post = Post.objects.get(id=pk)

    context = {'post': post}
    return render(request, 'blog/post-view.html', context)


@login_required
def post_delete(request, pk):
    item = Post.objects.get(id=pk)
    item.delete()
    return redirect('/')


@login_required
def post_update(request, pk):
    item = Post.objects.get(id=pk)
    form = PostForm(instance=item)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'item': item}
    return render(request, 'blog/post_update.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')


