from django.contrib import admin

from .models import Caixa, MeioDePagamento, Mesa, Produto, Pedido, Pagamento

admin.site.register(Caixa)
admin.site.register(MeioDePagamento)
admin.site.register(Mesa)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Pagamento)
