# restaurante/views/plato_views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models.plato import Plato

class PlatoListView(ListView):
    model = Plato
    template_name = 'restaurante/platos/list.html'

class PlatoCreateView(CreateView):
    model = Plato
    fields = ['nombre', 'descripcion']
    template_name = 'restaurante/platos/form.html'
    success_url = reverse_lazy('plato_list')

class PlatoUpdateView(UpdateView):
    model = Plato
    fields = ['nombre', 'descripcion']
    template_name = 'restaurante/platos/form.html'
    success_url = reverse_lazy('plato_list')

class PlatoDeleteView(DeleteView):
    model = Plato
    template_name = 'restaurante/platos/confirm_delete.html'
    success_url = reverse_lazy('plato_list')
