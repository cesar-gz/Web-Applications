# Generated by Django 4.0.4 on 2022-05-30 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='texxt',
            new_name='text',
        ),
    ]
