# Generated by Django 2.2 on 2019-05-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190506_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='extra',
            name='extra_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, choices=[('ongoing', 'ongoing'), ('cancelled', 'cancelled'), ('ready', 'ready'), ('done', 'done')], default='ongoing', max_length=9, null=True),
        ),
    ]
