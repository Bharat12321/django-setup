# Generated by Django 2.1.4 on 2019-11-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20191114_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
