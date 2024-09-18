from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
