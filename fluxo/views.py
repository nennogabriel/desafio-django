from django.http import HttpResponse
from django.template import loader
from .models import Mesa, Pedido, Pagamento

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def mesas(request):
    mesas = Mesa.objects.filter(fechado=False)
    template = loader.get_template('mesa/index.html')
    context = {
        'mesas': mesas,
    }
    return HttpResponse(template.render(context, request))

def mesa(request, mesa_id):
    mesa = Mesa.objects.get(pk=mesa_id)
    pedidos = Pedido.objects.filter(mesa=mesa_id)
    pagamentos = Pagamento.objects.filter(mesa=mesa_id)
    template = loader.get_template('mesa/detail.html')
    context = {
        'mesa': mesa,
        'pedidos': pedidos,
        'pagamentos': pagamentos,
    }
    return HttpResponse(template.render(context, request))

