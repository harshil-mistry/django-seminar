from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    tasks = request.session.get('tasks', [])
    return render(request, 'todo_app/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            # Get current tasks or initialize empty list
            tasks = request.session.get('tasks', [])
            # Add new task
            tasks.append(task)
            # Save back to session
            request.session['tasks'] = tasks
    return redirect('home')

def delete_task(request, index):
    tasks = request.session.get('tasks', [])
    if 0 <= index < len(tasks):
        tasks.pop(index)
        request.session['tasks'] = tasks
    return redirect('home')
