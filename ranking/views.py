from django.shortcuts import render, redirect
from .forms import Insertcadastro
from .models import cadastro

# Create your views here.

# Create

def create(request):
    form = Insertcadastro(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read')
    
    return render(request,'cadastro.html',{'form': form})


# Read 
def read(request):
    resp = cadastro.objects.all().order_by('tempo')
    return render(request,'rank.html', {'resp': resp})

# Delete
def delete(request,id):
    result = cadastro.objects.get(id=id)

    if request.method == 'POST':
        result.delete()
        return redirect('read')
    
    return render(request,'confirm.html',{'result': result})

#Update
def update(request,id):
    alter = cadastro.objects.get(id=id)
    form = Insertcadastro(request.POST or None, instance = alter)

    if form.is_valid():
        form.save()
        return redirect('read')

    return render(request, 'cadastro.html', {'form': form, 'alter': alter}) 


def Calculando(request,id):
    # Pegando o valores do tempo e das penalidades já transformado em porcentagem
    value = cadastro.objects.get(id=id) 
    tempo = value.tempo
    array_penal=[
        
        (value.Valor_da_penalidade_1)/100,
        
        (value.Valor_da_penalidade_2)/100,
        
        (value.Valor_da_penalidade_3)/100,
        
        (value.Valor_da_penalidade_4)/100,
        
        (value.Valor_da_penalidade_5)/100,
        
        (value.Valor_da_penalidade_6)/100,
        
        (value.Valor_da_penalidade_7)/100,
        
        (value.Valor_da_penalidade_8)/100,
        
        (value.Valor_da_penalidade_9)/100,
        
        (value.Valor_da_penalidade_10)/100,
        
        (value.Valor_da_penalidade_11)/100
    ]
   
   # Separando o minuto do segundo, 
   # Convertendo os minutos em segundos e somando os minutos convertidos com os segundos

    minuto = tempo // 1
    segundos = tempo % 1
    m_segundo = (minuto * 60)
    tempo_total = m_segundo + segundos

    # Aplicando as porcentagens das penalidades

    p = sum(array_penal)

    penalidade = (tempo_total * p)

    tempo_penalidade = (tempo_total + penalidade) # OBS -> o tempo penalidade está todo em segundo

    tempo_total_min = (tempo_penalidade/60) # OBS -> o tempo penalidade está todo em minutos, separar agr o minuto do segundo para ficar legível

    minuto_total = (tempo_total_min // 1) # Separando os minutos após aplicar as penalidades
    
    segundo_total_min = (tempo_total_min % 1) # Separando os segundos após aplicar as penalidades
                                            # Aqui os segundos estão em minutos, precisa converter para segundo de forma legível

    segundo_total_seg = (segundo_total_min * 60) # Transformando os segundos que estão em minutos em segundos corretamente

    tempo_result = (minuto_total + segundo_total_seg) #   OBS -> tempo em forma legível

    # Colocando no Banco o novo valor do tempo após aplicado as penalidades
    value.tempo = tempo_result

    return redirect('read')