# Generated by Django 4.1 on 2022-09-03 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='release_year',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='chapter',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.book'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='chapter',
            name='subtitle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='chapter',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
