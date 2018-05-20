# Generated by Django 2.0.4 on 2018-05-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='emp_type',
            field=models.CharField(choices=[('full time', 'Heltid'), ('part time', 'Deltid'), ('hourly paid', 'Timanställning'), ('probationary', 'Provanställning')], max_length=20, null=True, verbose_name='Anställningsform'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Namn'),
        ),
    ]