from django.db import models

class Task(models.Model):
    TASK_STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('in_process', 'In Process'),
        ('deletion', 'Deletion of the Task'),
    )

    name = models.CharField(max_length=255)
    content = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    points = models.IntegerField(choices=zip(range(1, 11), range(1, 11)))
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES)

    def __str__(self):
        return self.name