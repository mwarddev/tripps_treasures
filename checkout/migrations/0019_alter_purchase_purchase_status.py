# Generated by Django 3.2 on 2022-07-17 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0018_alter_purchase_purchase_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_status',
            field=models.CharField(choices=[('New Order', 'new_order'), ('In Production', 'in_production'), ('Production Complete', 'production_complete'), ('Despatched', 'despatched')], default='new_order', max_length=19),
        ),
    ]