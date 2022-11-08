# Generated by Django 4.0.3 on 2022-11-06 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('runs_app', '0004_alter_run_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='runner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]