# Generated by Django 4.2.5 on 2023-09-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdtaskManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=20),
        ),
    ]
