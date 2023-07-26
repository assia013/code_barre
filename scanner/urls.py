from django.urls import path
from . import views
urlpatterns=[
    path("register/",views.register,name='register'),
    path("",views.login,name='login'),
    path("logout/",views.logout_view,name='logout'),
    path("interface/",views.interface,name='interface'),
    path("categorie/",views.ajouter_categorie,name='categorie'),
    path("marque/",views.ajouter_marque,name='marque'),
    path("produit/",views.ajouter_produit,name='produit'),
    path("scanner/",views.scanner,name='scanner'),
    
]