# Generated by Django 2.2.24 on 2023-03-31 19:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20230325_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='apartments',
            field=models.ManyToManyField(blank=True, null=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='fio',
            field=models.CharField(db_index=True, max_length=100, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]
