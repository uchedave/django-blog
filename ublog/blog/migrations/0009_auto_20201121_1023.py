# Generated by Django 3.1.3 on 2020-11-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201120_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_snippet',
            field=models.CharField(max_length=200),
        ),
    ]
