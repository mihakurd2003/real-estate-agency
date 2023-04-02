# Generated by Django 2.2.24 on 2023-03-18 17:46

from django.db import migrations
from django.db.models import Case, When, F, Q
import phonenumbers


def fill_owner_pure_phone_fields(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    phonenumbers_list = [phonenumbers.parse(flat.owners_phonenumber, 'RU') for flat in flats]
    valid_numbers = [phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.E164) for num in phonenumbers_list if phonenumbers.is_valid_number(num)]

    Flat.objects.filter(id__in=[flat.id for flat in flats]).update(owner_pure_phone=valid_numbers)


def rollback_owner_pure_phone_fields(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = None


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone_fields, rollback_owner_pure_phone_fields)
    ]
