# Generated by Django 4.1 on 2023-05-02 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_alter_item_item_season_alter_item_item_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]