from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    # Другие поля, которые вам нужны
    def __str__(self):
        return self.title

# Остальные ваши модели и импорты
