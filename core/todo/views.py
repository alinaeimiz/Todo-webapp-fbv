from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import ToDo
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def todo(request):
    posts = ToDo.objects.filter(author=request.user)
    posts_active = posts.filter(completed=False)
    posts_completed = posts.filter(completed=True)
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request,'new task is active')
        return redirect("/")
    return render(request, 'to-do-list.html',{'form':form,'posts':posts,
                                              'posts_active':posts_active,
                                              'posts_completed':posts_completed,
                                              })
@login_required
def active(request,pk):
    posts = ToDo.objects.filter(author=request.user)
    if request.method == 'POST':
        if posts.get(id=pk).completed == True:
            posts = posts.filter(id=pk).update(completed=False)
            messages.warning(request,'your task is active')
            return redirect('/')
        else:
            posts = posts.filter(id=pk).update(completed=True)
            messages.success(request,'your task is completed')
            return redirect('/')
            