# Generated by Django 2.2.6 on 2019-11-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('campus', models.CharField(choices=[('IFPB - AREIA', 'IFPB - CAMPUS: AREIA'), ('IFPB - CABEDELO', 'IFPB - CAMPUS: CABEDELO'), ('IFPB - CABEDELO - CENTRO', 'IFPB - CAMPUS: CABEDELO - CENTRO'), ('IFPB - CAJAZEIRAS', 'IFPB - CAMPUS: CAJAZEIRAS'), ('IFPB - CAMPINA GRANDE', 'IFPB - CAMPUS: CAMPINA GRANDE'), ('IFPB - CATOLÉ DO ROCHA', 'IFPB - CAMPUS: CATOLÉ DO ROCHA'), ('IFPB - ESPERANÇA', 'IFPB - CAMPUS: ESPERANÇA'), ('IFPB - GUARABIRA', 'IFPB - CAMPUS: GUARABIRA'), ('IFPB - ITABAIANA', 'IFPB - CAMPUS: ITABAIANA'), ('IFPB - ITAPORANGA', 'IFPB - CAMPUS: ITAPORANGA'), ('IFPB - JOÃO PESSOA', 'IFPB - CAMPUS: JOÃO PESSOA'), ('IFPB - JOÃO PESSOA', 'IFPB - CAMPUS: MANGABEIRA'), ('IFPB - MONTEIRO', 'IFPB - CAMPUS: MONTEIRO'), ('IFPB - PATOS', 'IFPB - CAMPUS: PATOS'), ('IFPB - PEDRAS DE FOGO', 'IFPB - CAMPUS: PEDRAS DE FOGO'), ('IFPB - PICUÍ', 'IFPB - CAMPUS: PICUÍ'), ('IFPB - PRINCESA ISABEL', 'IFPB - CAMPUS: PRINCESA ISABEL'), ('IFPB - SANTA LUZIA', 'IFPB - CAMPUS: SANTA LUZIA'), ('IFPB - SANTA RITA', 'IFPB - CAMPUS: SANTA RITA'), ('IFPB - SOLEDADE', 'IFPB - CAMPUS: SOLEDADE'), ('IFPB - SOUSA', 'IFPB - CAMPUS: SOUSA')], max_length=20)),
                ('tempo', models.CharField(max_length=10)),
                ('volta', models.IntegerField(default=0)),
                ('penalidade', models.CharField(max_length=500)),
            ],
        ),
    ]