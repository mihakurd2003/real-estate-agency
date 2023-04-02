# Generated by Django 2.2.24 on 2023-04-02 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0016_auto_20230401_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='complained_address',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='text_complaint',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='who_complained',
        ),
        migrations.AddField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='complaints', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='text',
            field=models.TextField(default=None, null=True, verbose_name='Текст жалобы'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_apartments', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(null=True, verbose_name='Новое ли здание'),
        ),
    ]
