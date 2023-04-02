from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    new_building = models.BooleanField('Новое ли здание', null=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    liked_by = models.ManyToManyField(
        verbose_name='Кто лайкнул',
        to=User, related_name='liked_apartments',
        blank=True
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(
        verbose_name='Кто жаловался',
        to=User, on_delete=models.PROTECT,
        related_name='complaints',
        default=None, null=True,
    )
    flat = models.ForeignKey(
        verbose_name='Квартира, на которую пожаловались',
        to=Flat, on_delete=models.PROTECT,
        related_name='complaints',
        default=None, null=True,
    )
    text = models.TextField('Текст жалобы', default=None, null=True)

    def __str__(self):
        return f'{self.user} на {self.flat}'


class Owner(models.Model):
    fio = models.CharField('ФИО владельца', max_length=100, db_index=True)
    phonenumber = models.CharField('Номер владельца', max_length=20, db_index=True)
    pure_phonenumber = PhoneNumberField('Нормализованный номер владельца', blank=True, db_index=True)
    apartments = models.ManyToManyField(
        verbose_name='Квартиры в собственности',
        to=Flat, related_name='owners',
        blank=True
    )

    def __str__(self):
        return self.fio




