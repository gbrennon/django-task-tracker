from django.shortcuts import render, redirect
from .models import Task

def home(request):
    return render(request, 'home.html')

def tasks_view(request):
    if request.method == 'POST' and request.user.is_authenticated:
        title = request.POST.get('title')
        description = request.POST.get('description')
        done = request.POST.get('done') == 'on'
        user = request.user
        Task.objects.create(title=title, description=description, done=done, user=user)
        return redirect('tasks')
    
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})
