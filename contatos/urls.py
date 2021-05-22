from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Path to search URL
    path('search/', views.search, name='search'),
    # Open Tags with an argument that will be sent to the URL
    # Inform the type of argument: Integer -> because it will get the contact's ID
    # Enter a name for the argument = contact_id
    # Inform the name of the views (.\contatos\views) = contact_detail
    # Set the namespace for contact_detail
    path('<int:contact_id>', views.contact_detail, name='contact_detail'),
]
