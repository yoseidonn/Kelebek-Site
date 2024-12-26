# Generated by Django 5.1.4 on 2024-12-19 16:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True, verbose_name='Satın alım tarihi.')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Satın alım tutarı.')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Satın alımı yapan kullanıcı.')),
            ],
        ),
        migrations.CreateModel(
            name='LicenseKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128, unique=True, verbose_name='Lisans anahtarı:')),
                ('key_type', models.CharField(choices=[('STD', 'Standart'), ('PRO', 'Profesyonel')], default='STD', max_length=32, verbose_name='Lisans tipi:')),
                ('disk_serial_number1', models.BigIntegerField(blank=True, help_text='Disk seri numarasi', null=True, verbose_name='DSN 1:')),
                ('disk_serial_number2', models.BigIntegerField(blank=True, help_text='Disk seri numarasi', null=True, verbose_name='DSN 2:')),
                ('end_date', models.DateField(verbose_name='Lisansın sona eriş tarihi:')),
                ('purchase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='program.purchase', verbose_name='Satın alım:')),
            ],
        ),
    ]