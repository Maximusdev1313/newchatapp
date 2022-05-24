# Generated by Django 4.0.3 on 2022-05-24 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programmming', '0013_remove_comment_user_comments_massage_user_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='massage',
            name='user_comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='user_comments',
            field=models.ForeignKey(default=1653382133759, on_delete=django.db.models.deletion.CASCADE, to='programmming.massage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='massage',
            name='comments',
            field=models.ForeignKey(default=1653382133759, on_delete=django.db.models.deletion.CASCADE, related_name='Massage', to='programmming.comment'),
            preserve_default=False,
        ),
    ]