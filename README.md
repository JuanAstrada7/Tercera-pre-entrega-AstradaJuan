# Tercera-pre-entrega-AstradaJuan

# Proyecto Web de Alfajores con Django

Este proyecto utiliza Django con el patrón MVT y está diseñado para gestionar información sobre alfajores, clientes y pedidos.

## Pasos para probar el proyecto

1. Clone el repositorio desde GitHub.
2. Para inciar el servidor deben tener **Django** instalado
3. La pagina cuenta con los modelos Alfajor, Clientes y Pedidos.
4. Realice las migraciones con `python manage.py makemigrations` seguido de `python manage.py migrate`.
5. Cree un superusuario con `python manage.py createsuperuser` para acceder al panel de administración de Django.
6. Ejecute el servidor de desarrollo con `python manage.py runserver`.
7. Abra su navegador y vaya a [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) para acceder al panel de administración.
8. Utilice las vistas definidas en las URLs para probar la funcionalidad de la aplicación.

¡Disfrute del proyecto!
