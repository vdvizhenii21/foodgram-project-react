# Generated by Django 3.2.7 on 2021-10-08 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_follow_is_subscribed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='is_subscribed',
            new_name='follower',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'follower')},
        ),
    ]
