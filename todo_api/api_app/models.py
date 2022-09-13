from django.db import models


class User(models.Model):
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=255,
    )
    tg_id = models.IntegerField(
        verbose_name='ID телеги'
    )
    created_at = models.DateTimeField(
        verbose_name='Создан',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.username}"


class Category(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']

    def __str__(self):
        return f"{self.title}"


class Task(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255,
    )
    comment = models.TextField(
        verbose_name='Подробности'
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to=Category,
        on_delete=models.PROTECT,
        related_name='task'
    )
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to=User,
        on_delete=models.CASCADE,
        related_name='task'
    )
    created_at = models.DateTimeField(
        verbose_name='Создан',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Обновлён',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['user']

    def __str__(self):
        return f"{self.title}"
