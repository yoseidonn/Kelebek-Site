# Generated by Django 4.2.2 on 2023-06-29 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_feature_image_alter_heading_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images/features/thumbnails/%Y/%m/%d', verbose_name='Görsel'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='side',
            field=models.CharField(choices=[('LEFT', 'Sol'), ('RIGHT', 'Sağ')], default='LEFT', verbose_name='Metin yönü'),
        ),
        migrations.AlterField(
            model_name='heading',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images/headings/thumbnails/%Y/%m/%d', verbose_name='Görsel'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images/slide_thumbnails/%Y/%m/%d', verbose_name='Görsel'),
        ),
    ]
