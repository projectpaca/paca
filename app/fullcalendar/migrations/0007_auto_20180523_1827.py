# Generated by Django 2.0.4 on 2018-05-23 16:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullcalendar', '0006_auto_20180523_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='supervisor',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete='Ansvarig', to=settings.AUTH_USER_MODEL),
        ),
    ]
