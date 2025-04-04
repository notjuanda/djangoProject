from .cliente_views import (
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
)
from .mesero_views import (
    MeseroListView, MeseroCreateView, MeseroUpdateView, MeseroDeleteView
)
from .mesa_views import (
    MesaListView, MesaCreateView, MesaUpdateView, MesaDeleteView
)
from .plato_views import (
    PlatoListView, PlatoCreateView, PlatoUpdateView, PlatoDeleteView
)
from .orden_views import (
    OrdenListView, OrdenCreateView, OrdenUpdateView, OrdenDeleteView, PagarOrdenView
)