from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    STATUS = (
        ('✔️', '✔️ Выполнено'),
        ('⌛', '⌛ В процессе'),
        ('❌', '❌ Не начато'),
    )
    status = models.CharField(max_length=10, choices=STATUS, default='❌', verbose_name='Статус')
    priority = models.CharField(max_length=10, choices=[('low', 'Низкий'), ('medium', 'Средний'), ('high', 'Высокий')], default='medium', verbose_name='Приоритет')
    due_date = models.DateField(null=True, blank=True, verbose_name='Дедлайн')
    image = models.ImageField(upload_to='todo/', verbose_name='Картинка')
    author = models.CharField(max_length=100, blank=True, verbose_name='Автор')
    is_public = models.BooleanField(default=False, verbose_name='Публичная')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлена')

    class Meta:
        verbose_name = 'анкета'
        verbose_name_plural = 'анкеты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title