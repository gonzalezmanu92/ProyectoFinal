from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.index, name="index2"),
    path("aperturadecaja", views.aperturadecaja, name="aperturadecaja"),
    path("cierredecaja", views.cierredecaja, name="cierredecaja"),
    path("pagoimpuestos", views.pagoimpuestos, name="pagoimpuestos"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("cart", views.cart_view, name="cart"),
    path("order", views.order_view, name="order"),
    path("guardar_dato", views.guardar_dato, name="pagina_exitosa"),
    path("guardar_pago_impuesto", views.guardar_pago_impuesto, name="pagina_exitosa_pagoimpuesto"),
    path("guardar_dato_cierracaja", views.guardar_dato_cierrecaja, name="pagina_exitosa_cierrecaja"),
    path("topping/<int:cart_id>/", views.topping_view, name="topping"),
    path("removefromcart/<int:cart_id>/", views.removefromcart_view, name="removefromcart"),
    ]
