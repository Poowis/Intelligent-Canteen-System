# Generated by Django 2.2 on 2019-05-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190505_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='detail',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='status',
            field=models.CharField(choices=[('close', 'close'), ('open', 'open')], default='close', max_length=5),
        ),
    ]
