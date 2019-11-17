from django.db import models

# Create your models here.

class cadastro(models.Model):

    # Nome
        nome = models.CharField(max_length = 200)

    # Campus
        campus_choice = (
            ('IFPB - AREIA', 'IFPB - CAMPUS: AREIA'),
            ('IFPB - CABEDELO', 'IFPB - CAMPUS: CABEDELO'),
            ('IFPB - CABEDELO - CENTRO', 'IFPB - CAMPUS: CABEDELO - CENTRO'),
            ('IFPB - CAJAZEIRAS', 'IFPB - CAMPUS: CAJAZEIRAS'),
            ('IFPB - CAMPINA GRANDE', 'IFPB - CAMPUS: CAMPINA GRANDE'),
            ('IFPB - CATOLÉ DO ROCHA', 'IFPB - CAMPUS: CATOLÉ DO ROCHA'),
            ('IFPB - ESPERANÇA', 'IFPB - CAMPUS: ESPERANÇA'),
            ('IFPB - GUARABIRA', 'IFPB - CAMPUS: GUARABIRA'),
            ('IFPB - ITABAIANA', 'IFPB - CAMPUS: ITABAIANA'),
            ('IFPB - ITAPORANGA', 'IFPB - CAMPUS: ITAPORANGA'),
            ('IFPB - JOÃO PESSOA', 'IFPB - CAMPUS: JOÃO PESSOA'),
            ('IFPB - JOÃO PESSOA', 'IFPB - CAMPUS: MANGABEIRA'),
            ('IFPB - MONTEIRO', 'IFPB - CAMPUS: MONTEIRO'),
            ('IFPB - PATOS', 'IFPB - CAMPUS: PATOS'),
            ('IFPB - PEDRAS DE FOGO', 'IFPB - CAMPUS: PEDRAS DE FOGO'),
            ('IFPB - PICUÍ', 'IFPB - CAMPUS: PICUÍ'),
            ('IFPB - PRINCESA ISABEL', 'IFPB - CAMPUS: PRINCESA ISABEL'),
            ('IFPB - SANTA LUZIA', 'IFPB - CAMPUS: SANTA LUZIA'),
            ('IFPB - SANTA RITA', 'IFPB - CAMPUS: SANTA RITA'),
            ('IFPB - SOLEDADE', 'IFPB - CAMPUS: SOLEDADE'),
            ('IFPB - SOUSA', 'IFPB - CAMPUS: SOUSA'),
            )


        campus = models.CharField(
            max_length = 30,
            choices = campus_choice
            )

    # Tempo
        tempo = models.FloatField()

    #Voltas
        volta = models.IntegerField(default = 0)
    
    # Penalidades
        penalidade = models.CharField(max_length = 500)


def __str__(self):
    return self.nome