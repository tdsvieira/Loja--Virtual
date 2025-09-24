from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from loja.views import dashboard, index, signup  # importe todas as views do seu app

urlpatterns = [
    path('', index, name='index'),  # raiz: página inicial pública
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main'), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),  # página após login
    path('signup/', signup, name='signup'),  # página de cadastro

]
