from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Записка'
        verbose_name_plural = 'Записки'

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, verbose_name="Предмет")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    due = models.DateTimeField(verbose_name="Должник")
    is_finished = models.BooleanField(default=False, verbose_name="Завершено")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = 'Домашнее задание'

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False, verbose_name="Список дел")

    class Meta:
        verbose_name = verbose_name_plural = 'Список дел'

    def __str__(self):
        return self.title
