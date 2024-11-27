from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tasks = models.ManyToManyField(Task, blank=True, related_name="tags")

    def __str__(self):
        return self.name