# Generated by Django 4.0.4 on 2022-05-20 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programmming', '0009_remove_comment_user_comments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='massage',
            name='user_comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='user_comments',
            field=models.ForeignKey(default=1653027703338, on_delete=django.db.models.deletion.CASCADE, to='programmming.massage'),
            preserve_default=False,
        ),
    ]
