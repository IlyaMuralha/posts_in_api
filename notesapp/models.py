from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # с помощью класса мета определяем параметр сортировки
    class Meta:
        ordering = ['-updated_at']
