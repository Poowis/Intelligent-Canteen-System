# Generated by Django 2.2 on 2019-05-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190505_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('ongoing', 'ongoing'), ('cancelled', 'cancelled'), ('done', 'done')], default='ongoing', max_length=9, null=True),
        ),
    ]
