# To Do Application

Simple Django To-Do application with reminders.

Local setup

1. Create and activate virtualenv

# To Do Application

Simple Django To-Do application with reminders.

## Local setup

1. Create and activate virtualenv

```powershell
python -m venv env
& .\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run migrations and start server

```powershell
python manage.py migrate
python manage.py runserver
```

3. Admin

Create superuser and visit http://127.0.0.1:8000/admin/

---

## Detailed README

### Overview

This is a small Django-based To-Do application that supports:

- Creating, editing and deleting tasks
- Marking tasks as completed / uncompleted
- Adding a reminder date and time to a task
- Showing reminder alerts in the UI and firing a client-side popup + sound when a reminder is due
- Admin interface for managing tasks

### Project structure (important files)

- `tasks/models.py` — Task model (fields: `task` (CharField), `is_completed` (BooleanField), `reminder_date` (DateField), `reminder_time` (TimeField), `created_at`, `updated_at`)
- `tasks/views.py` — Views for listing tasks, adding, editing, deleting and marking done/undone. The `home` view collects tasks and (server-side) near-past reminders for display.
- `tasks/urls.py` — URL patterns for task actions.
- `templates/home.html` — Single-page UI: lists tasks, completed tasks, add-form, and contains client-side JavaScript used to trigger popup notifications and audio when reminders are due.
- `todo_main/settings.py` — Django settings, includes the `tasks` app in `INSTALLED_APPS`.

### How reminders work

1. When creating a task you may set `reminder_date` and `reminder_time`.
2. The server-side `home` view shows reminders that are already due (within a configured window) so you see them when you open the page.
3. The client-side JavaScript scans rendered tasks and schedules `setTimeout` timers for future reminders (and immediately displays near-past reminders). When a reminder triggers the UI:
	 - Inserts a modal popup with task details (high z-index backdrop)
	 - Plays a short beep using the Web Audio API
	 - Attempts to show a native browser notification (if the user granted permission)

### Important limitations

- The client-side notifications only work while the page is open in the browser. To receive notifications when the browser is closed you'd need a service worker + Push API and an HTTPS host.
- Many browsers block audio playback until the user interacts with the page. If you don't hear the beep, click once anywhere on the page and try again.

### Setup (detailed)

1. Create and activate a virtual environment (PowerShell):

```powershell
cd "C:\Users\Lenovo\OneDrive\Desktop\Projects\Django\To_Do_app"
python -m venv env
& .\env\Scripts\Activate.ps1
```

2. Install dependencies

If a `requirements.txt` exists run:

```powershell
pip install -r requirements.txt
```

If there is no `requirements.txt`, install Django manually (project uses Django 5.x in the local env):

```powershell
pip install django
```

3. Apply migrations and create a superuser

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server

```powershell
python manage.py runserver
# Open http://127.0.0.1:8000/ in your browser
```

### How to test reminders

1. Add a task with the reminder date set to today's date and the reminder time to the current time (or 1 minute from now).
2. Allow browser notifications when prompted (your browser will ask for permission).
3. Click anywhere on the page once (ensures audio is allowed).
4. Wait — the app will either show an immediate alert (if the reminder is already due) or schedule a popup/sound for the exact time.

### Troubleshooting

- If you see "Found 0 reminders" in the console but your task is saved, confirm the saved reminder fields in the admin or run:

```powershell
& .\env\Scripts\Activate.ps1
python manage.py shell -c "from tasks.models import Task; print([(t.id, t.task, t.reminder_date, t.reminder_time, t.is_completed) for t in Task.objects.all()])"
```

- If the popup doesn't appear at reminder time but the console shows scheduled logs:
	- Confirm `document.querySelectorAll('.reminder-data')` returns elements in DevTools Console.
	- Try calling `showNotificationPopup('Test', 'HH:MM', 'YYYY-MM-DD')` from the console to validate popup rendering and `playNotificationSound()` to test audio.

### Development notes and suggestions

- Add a `notified` boolean or a `last_notified` DateTime on the `Task` model to avoid repeated notifications across page reloads.
- For background notifications when the page is closed, implement a Service Worker and Push Notifications (requires hosting on HTTPS).
- Add unit tests for view behaviors (simple smoke tests) in `tasks/tests.py`.

### Git and remote

This repository was pushed to your GitHub remote. If you need to restore previous git metadata we backed it up locally in `.git-backup`.

### License

Pick a license for your project if you plan to share it publicly (MIT is common for simple apps).

### Contact / Help

If you want, I can:
- add the `notified` flag and migrations
- implement a simple Service Worker demo (requires HTTPS to fully work)
- add tests for reminder scheduling

Tell me which of the above you'd like next.

