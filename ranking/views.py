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
   

