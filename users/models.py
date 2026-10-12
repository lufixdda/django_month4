from email.policy import default

from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    photo = models.ImageField(upload_to='users/', blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    GENDER = (
        ('М','М'),
        ('Ж','Ж')
    )
    gender = models.CharField(max_length=100,
                             choices=GENDER, 
                             default='М')
    birthday = models.DateField('Дата рождения', null=True, blank=True)
    relationship = models.BooleanField('В отношениях', default=False ,blank=True )
    url_blog = models.URLField('Ссылка на ютуб', blank=True)
    description = models.TextField('О себе', max_length=400, blank=True)

    def __str__(self):
        return self.username