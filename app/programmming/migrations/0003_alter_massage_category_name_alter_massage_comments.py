# Generated by Django 4.0.4 on 2022-05-19 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programmming', '0002_comment_massage_massage_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massage',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programmming.category'),
        ),
        migrations.AlterField(
            model_name='massage',
            name='comments',
            field=models.CharField(max_length=2500, null=True),
        ),
    ]
