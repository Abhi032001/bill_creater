from django.contrib import admin
from django.urls import path
from .import views
from.views import InvoiceListView
from django.conf.urls.static import static
from django.conf import settings
# from app import views as user_views

app_name = 'invoice'

urlpatterns = [
    path("",views.Home, name= "home"),
    path("album/",views.Album_page,name= "album"),
    path("girl/",views.Girl_page,name= "girl"),
    path("boy/",views.Boy_page,name= "boy"),
    path("wedding/",views.Wedding_page,name= "wedding"), 
    path("kid/",views.Kid_page,name= "kid"),
    path("team/",views.Team_page,name= "team"),

    # ========================contact===================

     path("contact/",views.Contact_page,name= "contact"),
     path("data/",views.Insert_data, name="data"),
     path("customer/",views.Data_page,name= "customer"),


    # ==============================admin================
     path("login_page/",views.LoginPage,name= "login_page"),
     path("login/",views.Login,name= "login"),



    # ==============================bill===============================



    path("invoice-list/",InvoiceListView.as_view(), name= "invoice-list"),
    path('create/', views.createInvoice, name="invoice-create"),
    path('invoice-detail/<id>', views.view_PDF, name='invoice-detail'),
    path('invoice-download/<id>', views.generate_PDF, name='invoice-download'),
    path('invoice-delete/<id>', views.delete, name='invoice-delete'),  
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)