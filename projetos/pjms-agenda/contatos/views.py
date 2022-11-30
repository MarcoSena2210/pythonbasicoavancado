# https://docs.djangoproject.com/en/2.2/topics/pagination/
from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value # Q Usando simular consulta + complexas com OR
from django.db.models.functions import Concat
from django.contrib import messages

# Create your views here.
def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    # Paginação
    paginator = Paginator(contatos,10)  # Show 5 contacts per page.
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

# Ver apenas um contato
def ver_contato(request,contato_id):
    #contato = Contato.objects.get(id=contato_id)    #Retorna apenas um registro da base de dados
    contato = get_object_or_404(Contato, id=contato_id) #Para pegar a except
    if not contato.mostrar:
        raise Http404()
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

def busca(request):
    #Pegando o request
    termo = request.GET.get('termo')
    # Não existe termo
    if termo is None or not termo:
        messages.add_message(
            request, messages.ERROR,'Campos termo não pode ficar vazio na busca!'
        )
        return redirect('index')
    campos = Concat('nome', Value(' '),'sobrenome')

    '''
    Forma anterior, so funciona para busca um campo individual
    Ao digitar nome e sobrenome  falha
    contatos = Contato.objects.order_by('-id').filter(
        # Faz a consulta usando o OR
        Q(nome__icontains=termo) | Q(sobrenome__icontanis=termo),
        mostrar=True
    )
    '''
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    # print(contatos.query)  # Debug
    # Paginação
    paginator = Paginator(contatos, 10)  # Show 5 contacts per page.
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })