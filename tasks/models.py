from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    reminder_time = models.TimeField(null=True, blank=True, help_text="Time when you want to be reminded")
    reminder_date = models.DateField(null=True, blank=True, help_text="Date for the reminder")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ['-created_at']
