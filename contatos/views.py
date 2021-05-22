from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact


# Create your views here.
@login_required(redirect_field_name='login')
def index(request):
    # Get all Contact objects
    # contacts = Contact.objects.all()
    # Get all Contact objects sorted by names and filter for
    contacts = Contact.objects.order_by('name').filter(
        show=True
    )
    # Show 12 contacts per page.
    paginator = Paginator(contacts, 12)
    #
    page_number = request.GET.get('page')
    #
    page_obj = paginator.get_page(page_number)
    # Pass the contact objects as a dictionary key
    return render(request, 'contatos/index.html', {
        'contact_key': page_obj
    })


# The 'contact_id' argument is added to the method
# To get only a contact's information
# To be displayed on the contact_detail page
def contact_detail(request, contact_id):
    # Get an object of class Contact and if it doesn't exist send a 404 error page
    contact = get_object_or_404(Contact, id=contact_id)
    # If the contact is marked not to be displayed
    if not contact.show:
        messages.add_message(
            request,
            messages.ERROR,
            'Pagina não disponível!'
        )
        return redirect('index')
    # Pass the contact objects as a dictionary key
    return render(request, 'contatos/contact_detail.html', {
        'contact_key': contact
    })


def search(request):
    # Get the terms entered in the search form on the page
    terms_search = request.GET.get('terms')
    # Limit access to the page through the browser navigation bar
    if terms_search is None or not terms_search:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo de pesquisa vázio'
        )
        return redirect('index')
    # Concatenates the database 'name' and 'surname' fields to perform the search
    fields = Concat('name', Value(' '), 'surname')
    # Creates the list of Contact objects that match the annotations and search filters
    contacts = Contact.objects.annotate(
        complet_name=fields
    ).filter(
        Q(complet_name__icontains=terms_search) | Q(telephone__icontains=terms_search)
    )

    # ---> Code to monitor requests to the database
    # print(contacts.query)

    # ---> Initial code to filter the search terms
    # contacts = Contact.objects.order_by('name').filter(
    #    Q(name__icontains=terms_search) | Q(surname__icontains=terms_search),
    #    show=True
    # )

    # Show 12 contacts per page.
    paginator = Paginator(contacts, 12)
    #
    page_number = request.GET.get('page')
    #
    page_obj = paginator.get_page(page_number)
    # Pass the contact objects as a dictionary key
    return render(request, 'contatos/search.html', {
        'contact_key': page_obj
    })
