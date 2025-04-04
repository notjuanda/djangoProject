from django import forms
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from ..models.orden import Orden
from ..models.cliente import Cliente


class OrdenListView(ListView):
    model = Orden
    template_name = 'restaurante/ordenes/list.html'


class OrdenCreateView(CreateView):
    model = Orden
    fields = ['mesero', 'mesa', 'platos', 'estado', 'fechaHora']
    template_name = 'restaurante/ordenes/form.html'
    success_url = reverse_lazy('orden_list')


class OrdenUpdateView(UpdateView):
    model = Orden
    fields = ['mesero', 'mesa', 'platos', 'estado', 'fechaHora']
    template_name = 'restaurante/ordenes/form.html'
    success_url = reverse_lazy('orden_list')


class OrdenDeleteView(DeleteView):
    model = Orden
    template_name = 'restaurante/ordenes/confirm_delete.html'
    success_url = reverse_lazy('orden_list')


class PagoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre del Cliente")
    nit = forms.CharField(max_length=20, label="NIT")


class PagarOrdenView(FormView):
    template_name = 'restaurante/ordenes/pago_form.html'
    form_class = PagoForm
    success_url = reverse_lazy('orden_list')

    def form_valid(self, form):
        orden_id = self.kwargs['pk']
        orden = Orden.objects.get(pk=orden_id)

        nombre = form.cleaned_data['nombre']
        nit = form.cleaned_data['nit']

        cliente, created = Cliente.objects.get_or_create(
            nit=nit,
            defaults={'nombre': nombre}
        )
        orden.cliente = cliente
        orden.estado = 'cerrado'
        orden.save()

        return redirect(self.success_url)
