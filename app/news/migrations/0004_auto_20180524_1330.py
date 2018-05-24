# Generated by Django 2.0.4 on 2018-05-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180523_1747'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={},
        ),
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.AddField(
            model_name='news',
            name='body',
            field=models.TextField(default='Innehåll saknas.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='self.title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]