# Generated by Django 4.1 on 2023-05-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_alter_item_item_season_alter_item_item_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_season',
            field=models.CharField(blank=True, choices=[('春', '春'), ('夏', '夏'), ('秋', '秋'), ('冬', '冬')], db_index=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_size',
            field=models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('F', 'F')], max_length=150, null=True),
        ),
    ]
