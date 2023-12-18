# Generated by Django 3.2.23 on 2023-12-18 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smart_mingle_app', '0005_auto_20231218_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extradetails',
            name='user_id',
        ),
        migrations.AddField(
            model_name='extradetails',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='auth.user'),
            preserve_default=False,
        ),
    ]
