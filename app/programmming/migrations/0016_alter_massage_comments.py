# Generated by Django 4.0.3 on 2022-05-24 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programmming', '0015_remove_comment_user_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massage',
            name='comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programmming.comment'),
        ),
    ]
