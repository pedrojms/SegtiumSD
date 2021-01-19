from rest_framework import routers
from api import views as myapp_views

router = routers.DefaultRouter()
router.register(r'servicios', myapp_views.ServicioViewset)
router.register(r"noticias",myapp_views.NoticiasViewset)
router.register(r"ventas",myapp_views.VentasViewset)


