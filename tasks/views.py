from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    
    # Check for reminders that should be shown
    current_datetime = timezone.now()
    reminders = []
    
    for task in tasks:
        if task.reminder_time and task.reminder_date:
            try:
                # Create a timezone-aware datetime from date and time
                reminder_datetime = datetime.combine(task.reminder_date, task.reminder_time)
                
                # Get the timezone from settings
                if timezone.is_naive(reminder_datetime):
                    reminder_datetime = timezone.make_aware(reminder_datetime)
                
                # Show reminder if current time is within 24 hours after reminder time
                # and reminder hasn't been marked as done
                time_diff = (current_datetime - reminder_datetime).total_seconds()
                
                # Show if reminder time has passed and task is not completed
                if time_diff >= 0 and time_diff < 86400:  # Within 24 hours of reminder time
                    reminders.append({
                        'task': task,
                        'reminder_datetime': reminder_datetime,
                        'time_until': reminder_datetime
                    })
            except Exception as e:
                print(f"Error checking reminder: {e}")
    
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'reminders': reminders,
        'current_date': current_datetime.date(),
        'current_time': current_datetime.time(),
    }
    return render(request, "home.html", context)


def addTask(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        reminder_date = request.POST.get('reminder_date')
        reminder_time = request.POST.get('reminder_time')
        
        if task_text:
            task_data = {
                'task': task_text,
            }
            
            if reminder_date:
                task_data['reminder_date'] = reminder_date
            if reminder_time:
                task_data['reminder_time'] = reminder_time
                
            Task.objects.create(**task_data)
        return redirect('home')
    return redirect('home')


def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
    except Task.DoesNotExist:
        pass
    return redirect('home')


def edit_task(request, id):
    try:
        task = Task.objects.get(id=id)
        if request.method == 'POST':
            new_task_text = request.POST.get('task')
            reminder_date = request.POST.get('reminder_date')
            reminder_time = request.POST.get('reminder_time')
            
            if new_task_text:
                task.task = new_task_text
                if reminder_date:
                    task.reminder_date = reminder_date
                if reminder_time:
                    task.reminder_time = reminder_time
                task.save()
            return redirect('home')
    except Task.DoesNotExist:
        pass
    return redirect('home')


def mark_as_done(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.is_completed = True
        task.save()
    except Task.DoesNotExist:
        pass
    return redirect('home')


def mark_as_undone(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.is_completed = False
        task.save()
    except Task.DoesNotExist:
        pass
    return redirect('home')
