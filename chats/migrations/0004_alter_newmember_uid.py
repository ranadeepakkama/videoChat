# Generated by Django 4.2 on 2023-06-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_rename_usermember_newmember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newmember',
            name='uid',
            field=models.CharField(max_length=200),
        ),
    ]
