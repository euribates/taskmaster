# Generated by Django 3.1.1 on 2020-10-29 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_create_default_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default='DEF', on_delete=django.db.models.deletion.PROTECT, to='todo.project'),
        ),
    ]
