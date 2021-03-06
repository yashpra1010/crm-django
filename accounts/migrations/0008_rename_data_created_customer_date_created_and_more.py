# Generated by Django 4.0.4 on 2022-05-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='data_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='data_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='data_created',
            new_name='date_created',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
