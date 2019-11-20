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
        penal_choice = (
            ('Nenhuma', 'Nenhuma'),
            
            ('Tocar o robô', 'Tocar o robô'),

            ('O robô tocou em qualquer borda da pista', 'O robô tocou em qualquer borda da pista'),

            ('Não passar por dentro do túnel', 'Não passar por dentro do túnel'),

            ('Quando o robô não conseguir subir a rampa 30 graus', 'Quando o robô não conseguir subir a rampa'),

            ('Quando o robô não conseguir descer a rampa 30 graus', 'Quando o robô não conseguir descer a rampa'),

            ('Não separar ou separar incorretamente algum objeto da zona de coleta seletiva', 'Não separar ou separar incorretamente algum objeto da zona de coleta seletiva'),
            
            ('Robô virar de lado ou de ponta cabeça', 'Robô virar de lado ou de ponta cabeça'),

            ('Robô destruir a pista', 'Robô destruir a pista'),

            ('Não acessar a Área de Coleta Seletiva', 'Não acessar a Área de Coleta Seletiva'),

            ('DNS - Did Not Start', 'DNS - Did Not Start')
        )
        
        
        penalidade_1 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_1
        Valor_da_penalidade_1 = models.IntegerField(default = 0)

        penalidade_2 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_2
        Valor_da_penalidade_2 = models.IntegerField(default = 0)

        penalidade_3 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_3
        Valor_da_penalidade_3 = models.IntegerField(default = 0)

        penalidade_4 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_4
        Valor_da_penalidade_4 = models.IntegerField(default = 0)

        penalidade_5 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_5
        Valor_da_penalidade_5 = models.IntegerField(default = 0)

        penalidade_6 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_6
        Valor_da_penalidade_6 = models.IntegerField(default = 0)

        penalidade_7 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_7
        Valor_da_penalidade_7 = models.IntegerField(default = 0)

        penalidade_8 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_8
        Valor_da_penalidade_8 = models.IntegerField(default = 0)

        penalidade_9 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_9
        Valor_da_penalidade_9 = models.IntegerField(default = 0)

        penalidade_10 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_10
        Valor_da_penalidade_10 = models.IntegerField(default = 0)

        penalidade_11 = models.CharField(
            max_length = 50,
            choices = penal_choice)

        # Valor da penalidade_11
        Valor_da_penalidade_11 = models.IntegerField(default = 0)

def __str__(self):
    return self.nome