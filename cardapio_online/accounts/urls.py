from django.urls import path
from .views import * 
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('accounts/usuario_create', UsuarioCreate.as_view(), name="usuario_create")

]