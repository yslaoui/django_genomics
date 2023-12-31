# Generated by Django 3.0.3 on 2023-11-22 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Ec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ec_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_id', models.CharField(max_length=256)),
                ('entity', models.CharField(max_length=256)),
                ('source', models.CharField(blank=True, max_length=256)),
                ('start', models.IntegerField(blank=True)),
                ('stop', models.IntegerField(blank=True)),
                ('start_codon', models.CharField(default='M', max_length=1)),
                ('ec', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='genedata.Ec')),
            ],
        ),
        migrations.CreateModel(
            name='Sequencing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=256)),
                ('product', models.CharField(max_length=256)),
                ('gene_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genedata.Gene')),
            ],
        ),
        migrations.CreateModel(
            name='GeneAttributeLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='genedata.Attribute')),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='genedata.Gene')),
            ],
        ),
        migrations.AddField(
            model_name='gene',
            name='sequencing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='genedata.Sequencing'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='gene',
            field=models.ManyToManyField(through='genedata.GeneAttributeLink', to='genedata.Gene'),
        ),
    ]
