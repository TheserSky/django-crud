from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import taskForm
from .models import Tasks
from django.utils import timezone
from django.contrib.auth import login, logout,authenticate

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        print('mostrando form')
        return render(request , 'index.html' , {
            "form": UserCreationForm,
            'error': ''
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #register user  
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save
                login(request , user)
                return redirect('tasks')
            except:
                return render(request , 'index.html' , {
                    "form": UserCreationForm,
                    'error': 'Este usuario ya existe'
                })
        return  render(request , 'index.html' , {
                    "form": UserCreationForm,
                    'error': 'Constraseña no coincide'
                })

def tasks(request):
    tasks = Tasks.objects.filter(user = request.user , dateCompleted__isnull = True)
    return render(request, 'tasks.html' , {
        'tasks': tasks
    })
def task_completed(request):
    tasks = Tasks.objects.filter(user = request.user , dateCompleted__isnull = False)
    return render(request, 'taskCompleted.html' , {
        'tasks': tasks
    })
def createTasks(request):
    if request.method == 'GET':
        return render(request , 'createTasks.html',{
            'form' : taskForm
        })
    else: 
        form = taskForm(request.POST)
        newTask = form.save(commit=False)
        newTask.user = request.user
        newTask.save()
        return redirect('tasks')

def signout (request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request , 'signin.html' , {
            'form': AuthenticationForm,
            'error': ''
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request , 'signin.html' , {
                'form': AuthenticationForm,
                'error': 'Este usuario no existe'
            })
        else:
            login(request, user)
            return redirect('tasks')




def taskdetail(request , task_id):
    if request.method == 'GET':
        task = get_object_or_404(Tasks , pk=task_id, user=request.user)
        form = taskForm(instance=task)
        return render(request , 'task_detail.html' , {
            'task': task,
            'form': form
        })
    else:
        task = get_object_or_404(Tasks , pk=task_id , user=request.user)
        form = taskForm(request.POST, instance=task)
        form.save()
        return redirect('tasks')
    

def taskCompleted(reauest, task_id):
    task = get_object_or_404(Tasks , pk=task_id , user=reauest.user)
    if reauest.method == 'POST':
        task.dateCompleted = timezone.now()
        task.save()
        return redirect('tasks')

def taskDelete(reauest, task_id):
    task = get_object_or_404(Tasks , pk=task_id , user=reauest.user)
    if reauest.method == 'POST':
        task.delete()
        return redirect('tasks')




















