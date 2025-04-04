# restaurante/views/mesa_views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models.mesa import Mesa

class MesaListView(ListView):
    model = Mesa
    template_name = 'restaurante/mesas/list.html'

class MesaCreateView(CreateView):
    model = Mesa
    fields = ['numero']
    template_name = 'restaurante/mesas/form.html'
    success_url = reverse_lazy('mesa_list')

class MesaUpdateView(UpdateView):
    model = Mesa
    fields = ['numero']
    template_name = 'restaurante/mesas/form.html'
    success_url = reverse_lazy('mesa_list')

class MesaDeleteView(DeleteView):
    model = Mesa
    template_name = 'restaurante/mesas/confirm_delete.html'
    success_url = reverse_lazy('mesa_list')
