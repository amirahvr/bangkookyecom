# Generated by Django 5.1.2 on 2024-11-21 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='merek_produk',
            field=models.CharField(choices=[('The Body Shop', 'The Body Shop'), ('somethinc', 'somethinc'), ('skintific', 'skintific')], max_length=30),
        ),
    ]