# Generated by Django 3.0.3 on 2023-11-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genedata', '0003_gene_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='access',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
