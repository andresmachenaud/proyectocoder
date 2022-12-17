from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),

    path("estudiantes/", estudiantes, name="coder-estudiantes"),

    path("profesores/", profesores, name="coder-profesores"),
    path("profesores/crear/", crear_profesor, name="coder-profesores-crear"),

    path("cursos/", cursos, name="coder-cursos"),
    path("cursos/crear/", crear_curso, name="coder-cursos-crear"),
    path("cursos/buscar/", buscar_curso, name="coder-cursos-buscar"),
    path("cursos/buscar/resultados/", resultados_buscar_cursos, name="coder-cursos-buscar-resultados"),
    path("cursos/borrar/<id>", eliminar_curso, name="coder-cursos-borrar"),
    path("cursos/editar/<id>", editar_curso, name="coder-cursos-editar"),

    path("entregables/", EntregablesList.as_view(), name="coder-entregables"),
    path("entregables/detalle/<pk>/", EntregableDetail.as_view(), name="coder-entregables-detalle"),
    path("entregables/crear/", EntregableCreate.as_view(), name="coder-entregables-crear"),
    path("entregables/editar/<pk>/", EntregableUpdate.as_view(), name="coder-entregables-editar"),
    path("entregables/borrar/<pk>/", EntregableDelete.as_view(), name="coder-entregables-borrar"),

    path("login/", login_request, name="login"),
    path("registro/", register_request, name="registro"),
    path("registro/success/", confirmacion_registro, name="confirmacion-registro"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    path("perfil/editar/", editar_perfil, name="perfil-editar"),
    path("perfil/avatar/", agregar_avatar, name="perfil-avatar"),

    path("test/", test, name="coder-test")
]
