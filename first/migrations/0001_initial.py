# Generated by Django 2.1.4 on 2019-11-14 05:37

from django.db import migrations, models
import django.utils.timezone
import first.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('enroll_id', models.IntegerField(unique=True, verbose_name='Enroll ID')),
                ('title', models.CharField(blank=True, max_length=30, verbose_name='Title')),
                ('first_name', models.CharField(blank=True, max_length=120, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=120, verbose_name='Last Name')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-date_joined',),
            },
            managers=[
                ('objects', first.models.UserManager()),
            ],
        ),
    ]