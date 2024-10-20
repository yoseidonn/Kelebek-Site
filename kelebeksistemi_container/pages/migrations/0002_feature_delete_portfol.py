# Generated by Django 4.2.2 on 2023-06-12 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Görsel')),
                ('title', models.CharField(verbose_name='Başlık')),
                ('side_title', models.CharField(verbose_name='Yan başlık')),
                ('text', models.CharField(verbose_name='İçerik')),
                ('side', models.CharField(choices=[('LEFT', 'Sol'), ('RIGHT', 'Sağ')], default='LEFT')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Eklenme tarihi.')),
            ],
        ),
        migrations.DeleteModel(
            name='Portfol',
        ),
    ]
