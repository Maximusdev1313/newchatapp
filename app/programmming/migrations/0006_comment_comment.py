# Generated by Django 4.0.4 on 2022-05-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmming', '0005_rename_massage_comment_comments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=1652966737736, max_length=2500),
            preserve_default=False,
        ),
    ]