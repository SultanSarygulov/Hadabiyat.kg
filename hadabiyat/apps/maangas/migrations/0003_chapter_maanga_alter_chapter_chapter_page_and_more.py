# Generated by Django 4.0.4 on 2022-06-01 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maangas', '0002_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='maanga',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='maangas.maanga'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='chapter_page',
            field=models.ImageField(upload_to='', verbose_name='chapter page'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='maanga',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='maangas.maanga'),
        ),
    ]