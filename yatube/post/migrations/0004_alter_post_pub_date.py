# Generated by Django 5.0.1 on 2024-02-20 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_group_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]