from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import inicio, contacto, PanelAdminView, registro

urlpatterns = [
    path('', inicio, name='inicio'),

    path('login/', auth_views.LoginView.as_view(
        template_name='principal/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('contacto/', contacto, name='contacto'),
    path('admin-panel/', PanelAdminView.as_view(), name='admin_panel'),
    path('registro/', registro, name='registro'),

    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),

]