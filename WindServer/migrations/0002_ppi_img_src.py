# Generated by Django 2.2.3 on 2019-07-04 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WindServer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppi',
            name='img_src',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
