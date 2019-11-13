from django.db import models

# Create your models here.

class cadastro(models.Models):

    # Nome
        nome = models.CharField(max_lenght = 200)

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
        )

    # Tempo
        tempo = models.CharField(max_length = 10)

    #Voltas
        volta = models.IntegerField(default = 0)
    
    # Penalidades
        penalidade = models.CharField(max_length = 500)