from django.shortcuts import render, redirect
from django.contrib import messages

from fluxocaixa.forms import GastosForm


def index(request):
    return render(request, 'index.html')

def gastos(request):
    if str(request.method) == 'POST':
        form = GastosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Gasto cadastrado com sucesso!")
            return redirect('gastos')
        else:
            messages.error(request, 'Erro ao salvar o Gasto')
            return redirect('gastos')
    else:#getResponse
        context = {
            'form': GastosForm()
        }
        return render(request, 'gastos.html', context)
