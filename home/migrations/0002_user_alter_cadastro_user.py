# Generated by Django 5.1.1 on 2024-11-09 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('CRM', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('senha', models.CharField(default='', max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cadastros', to='home.user'),
        ),
    ]
