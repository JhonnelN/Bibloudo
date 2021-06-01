# Generated by Django 3.1.6 on 2021-04-07 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repisa', '0009_auto_20210331_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Semestre',
                'verbose_name_plural': 'Semestres',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='libro',
            name='semestre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repisa.semestre'),
        ),
    ]
