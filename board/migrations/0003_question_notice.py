# Generated by Django 3.2.8 on 2021-11-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20210330_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='notice',
            field=models.BooleanField(default=False),
        ),
    ]