# Generated by Django 4.0.4 on 2022-05-27 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programmming', '0019_remove_massage_file_files'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='file',
            new_name='file_field',
        ),
    ]