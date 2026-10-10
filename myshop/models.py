from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.IntegerField(max_length=10,  verbose_name='Цена')
    image = models.ImageField(verbose_name='Фото товара', upload_to='product/')
    category = models.CharField(max_length=100, verbose_name='Категория')
    weight = models.IntegerField(default=0, verbose_name='Вес (г)')
    color = models.CharField(max_length=50, blank=True, verbose_name='Цвет')
    stock = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')
    is_active = models.BooleanField(default=True, verbose_name='Доступен для продажи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.title


class SerialNumber(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='serial_number',
        verbose_name='Товар'
    )
    number = models.CharField(max_length=100, unique=True, verbose_name='Серийный номер')
    issued_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата выдачи')
    is_used = models.BooleanField(default=False, verbose_name='Использован')

    class Meta:
        verbose_name = 'серийный номер'
        verbose_name_plural = 'серийные номера'

    def __str__(self):
        return f'{self.number} ({self.product.title})'


class ProductComment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Товар'
    )
    author_name = models.CharField(max_length=100, verbose_name='Имя автора')
    comment = models.TextField(max_length=500, verbose_name='Комментарий')
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Оценка (1-5)'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'комментарий к товару'
        verbose_name_plural = 'комментарии к товарам'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author_name} - {self.product.title} ({self.rating}/5)'