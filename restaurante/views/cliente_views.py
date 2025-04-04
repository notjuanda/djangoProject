# restaurante/views/cliente_views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models.cliente import Cliente

class ClienteListView(ListView):
    model = Cliente
    template_name = 'restaurante/clientes/list.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'nit']  # Ajusta según tu modelo
    template_name = 'restaurante/clientes/form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'nit']
    template_name = 'restaurante/clientes/form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'restaurante/clientes/confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
