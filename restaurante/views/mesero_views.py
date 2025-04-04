from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models.mesero import Mesero

class MeseroListView(ListView):
    model = Mesero
    template_name = 'restaurante/meseros/list.html'

class MeseroCreateView(CreateView):
    model = Mesero
    fields = ['nombre', 'apellido', 'telefono']
    template_name = 'restaurante/meseros/form.html'
    success_url = reverse_lazy('mesero_list')

class MeseroUpdateView(UpdateView):
    model = Mesero
    fields = ['nombre', 'apellido', 'telefono']
    template_name = 'restaurante/meseros/form.html'
    success_url = reverse_lazy('mesero_list')

class MeseroDeleteView(DeleteView):
    model = Mesero
    template_name = 'restaurante/meseros/confirm_delete.html'
    success_url = reverse_lazy('mesero_list')
