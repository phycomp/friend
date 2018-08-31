# Generated by Django 2.2 on 2018-08-15 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='timestamp')),
                ('blocker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blocker_friendship', to=settings.AUTH_USER_MODEL)),
                ('friend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend_friendship', to=settings.AUTH_USER_MODEL)),
                ('invoker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoker_friendship', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_friendship', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'friendship',
            },
        ),
    ]
