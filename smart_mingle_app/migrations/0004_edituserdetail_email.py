# Generated by Django 3.2.23 on 2023-12-15 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_mingle_app', '0003_remove_edituserdetail_display_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='edituserdetail',
            name='email',
            field=models.EmailField(default='email', max_length=24),
        ),
    ]