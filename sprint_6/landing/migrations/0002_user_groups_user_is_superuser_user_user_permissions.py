# Generated by Django 4.2.2 on 2023-06-21 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customuser_set', related_query_name='customuser', to='auth.group'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='customuser_set', related_query_name='customuser', to='auth.permission'),
        ),
    ]
