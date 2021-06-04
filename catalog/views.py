from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from .models import Contact
from .forms import ContactForm

# Create your views here.
class IndexView(ListView):
    template_name = 'contact/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Contact.objects.all()


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/contact-detail.html'


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/create.html', context)

def edit(request, pk, template_name = 'contact/edit.html'):
    contact = get_object_or_404(Contact, pk=pk)
    print(contact)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, template_name, context)


def delete(request, pk, template_name='contact/delete.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method=='POST':
            contact.delete()
            return redirect('index')
    return render(request, template_name, {'object': contact})