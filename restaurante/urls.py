from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/crear/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_edit'),
    path('clientes/<int:pk>/borrar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('meseros/', views.MeseroListView.as_view(), name='mesero_list'),
    path('meseros/crear/', views.MeseroCreateView.as_view(), name='mesero_create'),
    path('meseros/<int:pk>/editar/', views.MeseroUpdateView.as_view(), name='mesero_edit'),
    path('meseros/<int:pk>/borrar/', views.MeseroDeleteView.as_view(), name='mesero_delete'),
    path('mesas/', views.MesaListView.as_view(), name='mesa_list'),
    path('mesas/crear/', views.MesaCreateView.as_view(), name='mesa_create'),
    path('mesas/<int:pk>/editar/', views.MesaUpdateView.as_view(), name='mesa_edit'),
    path('mesas/<int:pk>/borrar/', views.MesaDeleteView.as_view(), name='mesa_delete'),
    path('platos/', views.PlatoListView.as_view(), name='plato_list'),
    path('platos/crear/', views.PlatoCreateView.as_view(), name='plato_create'),
    path('platos/<int:pk>/editar/', views.PlatoUpdateView.as_view(), name='plato_edit'),
    path('platos/<int:pk>/borrar/', views.PlatoDeleteView.as_view(), name='plato_delete'),
    path('ordenes/', views.OrdenListView.as_view(), name='orden_list'),
    path('ordenes/crear/', views.OrdenCreateView.as_view(), name='orden_create'),
    path('ordenes/<int:pk>/editar/', views.OrdenUpdateView.as_view(), name='orden_edit'),
    path('ordenes/<int:pk>/borrar/', views.OrdenDeleteView.as_view(), name='orden_delete'),
    path('ordenes/<int:pk>/pagar/', views.PagarOrdenView.as_view(), name='orden_pagar'),
]
