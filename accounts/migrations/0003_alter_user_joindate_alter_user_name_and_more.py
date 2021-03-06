# Generated by Django 4.0.1 on 2022-02-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_name_user_nickname_alter_user_lastlogin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joindate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=5, verbose_name='실명'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=15, unique=True, verbose_name='닉네임'),
        ),
    ]
