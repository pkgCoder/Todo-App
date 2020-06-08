# Generated by Django 2.2.7 on 2020-06-05 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_auto_20200605_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='complete',
            new_name='completed',
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
