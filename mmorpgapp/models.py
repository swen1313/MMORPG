from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

Tanks = 'танки'
Heals = 'хилы'
DD = 'дд'
Merchants = 'торговцы'
Guildmasters = 'гилдмастеры'
Questgivers = 'квестгиверы'
Blacksmiths = 'кузнецы'
Leatherworkers = 'кожевники'
Potionmasters = 'зельевары'
Spellmasters = 'Мастера Заклинаний'

choices = [(Tanks, 'Танки'), (Heals, 'Хилы'), (DD, 'ДД'), (Merchants, 'Торговцы'),
           (Guildmasters, 'Гилдмастеры'), (Questgivers, 'Квестгиверы'), (Blacksmiths, 'Кузнецы'),
           (Leatherworkers, 'Кожевники'), (Potionmasters, 'Зельевары'), (Spellmasters, 'Мастера Заклинаний')]

class Advert(models.Model):
    userWho = models.ForeignKey(User, on_delete=models.CASCADE)
    postType = models.CharField(max_length=20, choices=choices, default='танки')
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='AdvertCategory')
    header = models.CharField(max_length=64)
    text = models.TextField()
    image = models.ImageField(blank=True)
    file = models.FileField(blank=True)





class AdvertCategory(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Response(models.Model):
    advertResponse = models.ForeignKey(Advert, on_delete=models.CASCADE, default=0)
    userTo = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=64)






# Create your models here.
