from django.db import models


class Blog(models.Model):
    title = models.CharField(verbose_name='укажите название блога', max_length=20)
    image = models.ImageField(verbose_name='загрузите фото блога', upload_to='blog/')
    description = models.TextField(verbose_name='укажите описание блога', blank=True)
    author_email = models.EmailField(verbose_name='укажите свою почту', default='none@example.com')
    CATEGORIES = (
        ('Детектив', 'Детектив'),
        ('Комедия', 'Комедия'),
        ('Фантастика', 'Фантастика')
    )
    categories = models.CharField(verbose_name='Выбери категорию блога',
                                 choices=CATEGORIES,
                                 default='Фантастика',
                                 max_length=100)
    url_blog = models.URLField(verbose_name='есть ссылка на ютуб?', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'список блогов'

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название книги')
    author = models.CharField(max_length=100, verbose_name='Автор')
    isbn = models.CharField(max_length=13, verbose_name='ISBN', unique=True)
    published_date = models.DateField(verbose_name='Дата публикации')
    pages = models.IntegerField(verbose_name='Количество страниц')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    publisher = models.CharField(max_length=100, verbose_name='Издательство', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', blank=True)
    cover_image = models.ImageField(verbose_name='Обложка', upload_to='book/covers/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title