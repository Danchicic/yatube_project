# Generated by Django 5.0.1 on 2024-02-10 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
