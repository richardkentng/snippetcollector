# Generated by Django 3.1.7 on 2021-03-13 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210313_0356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='name',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='content',
        ),
    ]