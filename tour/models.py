from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название тура')
    description = models.TextField(blank=True, verbose_name='Описание')
    date = models.DateField(verbose_name='Дата тура')
    categories = models.ManyToManyField(Category, related_name='tours', verbose_name='Категории')

    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = 'туры'

    def __str__(self):
        return f'{self.title} ({self.date})'


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')

    class Meta:
        verbose_name = 'человек'
        verbose_name_plural = 'люди'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tickets', verbose_name='Тур')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='tickets', verbose_name='Человек')
    ticket_number = models.CharField(max_length=50, unique=True, verbose_name='Номер билета')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')

    class Meta:
        verbose_name = 'билет'
        verbose_name_plural = 'билеты'
        unique_together = ['tour', 'person']

    def __str__(self):
        return f'Билет #{self.ticket_number} — {self.person.name} на {self.tour.title}'


class Comment(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='comments', verbose_name='Тур')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5,
        verbose_name='Оценка (1-5)'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.person.name} — {self.tour.title} ({self.rating}/5)'