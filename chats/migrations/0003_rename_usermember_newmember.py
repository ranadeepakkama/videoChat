# Generated by Django 4.2 on 2023-06-27 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_usermember_delete_room'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserMember',
            new_name='NewMember',
        ),
    ]