# Generated by Django 3.2.3 on 2021-05-23 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='comment',
            new_name='comments',
        ),
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]
