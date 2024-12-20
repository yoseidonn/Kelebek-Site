# Generated by Django 4.2.2 on 2023-06-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pp',
            field=models.ImageField(blank=True, default='/static/images/logo.png', upload_to='', verbose_name='Profil fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('Admin', 'Yönetici'), ('Developer', 'Geliştirici'), ('User', 'Kullanıcı')], default='User'),
        ),
    ]
