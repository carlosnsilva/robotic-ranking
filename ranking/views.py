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


def Calculando(request):
    # Calculando as penalidades
    DB = cadastro.objects.values_list('Valor_da_penalidade_1','Valor_da_penalidade_2','Valor_da_penalidade_3','Valor_da_penalidade_4','Valor_da_penalidade_5','Valor_da_penalidade_6','Valor_da_penalidade_7','Valor_da_penalidade_8','Valor_da_penalidade_9','Valor_da_penalidade_10','Valor_da_penalidade_11')
    

'''    
l=[]
array=[(1,2,3),(4,5,6),(7,8,9)]
print(array)
for i in array:
  for j in (i):
    print(j)
    l.append(j)

print(l)

Percorrendo nas tuplas'''    