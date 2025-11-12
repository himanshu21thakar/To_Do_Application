
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    # For now, pass empty task lists
    context = {
        'tasks': [],
        'completed_tasks': []
    }
    return render(request, "home.html", context)


def addTask(request):
    if request.method == 'POST':
        # Handle adding a new task
        task = request.POST.get('task')
        # TODO: Save to database
        return redirect('home')
    return redirect('home')


def delete_task(request, id):
    # TODO: Delete task from database
    return redirect('home')


def edit_task(request, id):
    # TODO: Edit task functionality
    return redirect('home')


def mark_as_done(request, pk):
    # TODO: Mark task as complete
    return redirect('home')


def mark_as_undone(request, pk):
    # TODO: Mark task as incomplete
    return redirect('home')