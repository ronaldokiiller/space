from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Imagem
from .forms import ImagemForm

def home(request):
    imagens = Imagem.objects.all()  # ou filtre por usuário, se quiser
    return render(request, 'home.html', {'imagens': imagens})

@login_required
def lista_imagens(request):
    imagens = Imagem.objects.filter(usuario=request.user)
    return render(request, 'galeria/lista.html', {'imagens': imagens})

@login_required
def criar_imagem(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = form.save(commit=False)
            imagem.usuario = request.user
            imagem.save()
            return redirect('lista_imagens')
    else:
        form = ImagemForm()
    return render(request, 'galeria/form.html', {'form': form})

@login_required
def editar_imagem(request, pk):
    imagem = get_object_or_404(Imagem, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES, instance=imagem)
        if form.is_valid():
            form.save()
            return redirect('lista_imagens')
    else:
        form = ImagemForm(instance=imagem)
    return render(request, 'galeria/form.html', {'form': form})

@login_required
def deletar_imagem(request, pk):
    imagem = get_object_or_404(Imagem, pk=pk, usuario=request.user)
    if request.method == 'POST':
        imagem.delete()
        return redirect('lista_imagens')
    return render(request, 'galeria/confirmar_delete.html', {'imagem': imagem})

def index(request):
    return render(request, 'galeria/index.html')


def imagem(request):
    return render(request, 'galeria/imagem.html')