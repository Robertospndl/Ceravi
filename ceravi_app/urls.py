from django.urls import path
#importa as funções de controle (controllers em MVC) que em django estão no views.py
from ceravi_app import views

#A seguir são configuradas as rotas da nossa aplicação
urlpatterns = [
    path("", views.login, name="home"),
   
    path("login/", views.login, name="login"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("pagina_inicial/", views.pagina_inicial, name="pagina_inicial"),
    path("esqueceu_senha/", views.esqueceu_senha, name="esqueceu_senha"),
]