# Generated by Django 2.2.6 on 2019-11-20 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0003_auto_20191117_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='penalidade',
        ),
        migrations.AddField(
            model_name='cadastro',
            name='penalidade_1',
            field=models.CharField(choices=[('penal_1', 'Tocar o robô'), ('penal_2', 'entrou na pista')], default=0, max_length=30),
            preserve_default=False,
        ),
    ]
