from typing import Any, Dict, List
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

# Create your views here.

def some_view(request):
    if not request.user.is_authenticated:
        return HttpResponse("You are not logged in")
    else:
        return HttpResponse("You are logged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../')

def register(request):
    master_genes = Gene.objects.all()
    registered = False
    if request.method == 'POST':
        # Create form instances and pass them request data as argument
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)
        # Check that user input data is valid
        if user_form.is_valid() and profile_form.is_valid():
            # If forms are valid, create a corresponding model instance for them
            user = user_form.save(commit=False)  # create a new user model instance. commit=False ensures that the new user is not saved in the database yet, because we still need to hash the password
            user.set_password(user.password) # hash the password
            user.save() # now in the database and model, the hashed password is saved and commited to the database

            # create an instance of the AppUser model from the form. Assign the user model instance to the Appuser attribute. Add the organisation field if it has been provided bty the user
            profile = profile_form.save(commit = False)
            profile.user = user
            if 'organization' in user_form.data:
                profile.organization = request.POST['organization']
            profile.save()
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'genedata/register.html', {'user_form' : user_form, 
                                                      'profile_form' : profile_form,
                                                      'registered' : registered, 
                                                      'master_genes': master_genes})
def user_login(request):
    master_genes = Gene.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['username']

        # Check the credentials against the database. If Ok, returns the user model instance. Otherwise return None
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
               login(request, user)  
               return HttpResponseRedirect('../')
            else:
                return HttpResponse("Your account is disabled") 
        else:
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'genedata/login.html', {'master_genes': master_genes} )        


class GeneList(ListView):
    model = Gene
    context_object_name = 'master_genes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'poslist' in self.request.get_full_path():
            context['genes'] = Gene.objects.filter(entity__exact='Chromosome').filter(start_codon='+')

        if 'type' in self.kwargs:
            if 'Chromosome' in self.kwargs['type'] or 'Plasmid' in self.kwargs['type']: 
                context['genes'] = Gene.objects.filter(entity__exact=self.kwargs['type'])
        print(self.kwargs)
        return context
                   
    def get_template_names(self):
        if 'poslist' in self.request.get_full_path():
            return('genedata/list.html') 
        if 'type' in self.kwargs:
            if 'Chromosome' in self.kwargs['type'] or 'Plasmid' in self.kwargs['type']: 
                return 'genedata/list.html'            
        return('genedata/index.html')
    

# Q. #todo Override the get_template_names method. If poslist is in the full path,
# return genedata/list.html with the result. Same if type is part of the request
#  parameters. Else return genedata/index.html. Verify tat it works

def poslist(request):
    genes = Gene.objects.filter(entity__exact='Chromosome').filter(start_codon='+')
    master_genes = Gene.objects.all()
    print(genes)
    return render(request, 
                  'genedata/list.html', 
                  {'genes': genes, 'master_genes': master_genes, 'type': type})


class GeneDetail(DetailView):
    model = Gene
    context_object_name = 'gene'
    template_name = 'genedata/gene.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

class GeneCreate(CreateView):
    model = Gene
    form_class = GeneForm
    success_url = '/create_gene'
    template_name = 'genedata/create_gene.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

class GeneDelete(DeleteView):
    model = Gene
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

class GeneUpdate(UpdateView):
    model = Gene
    fields = ['gene_id', 'entity', 
                'source', 'start', 
                'stop', 'start_codon', 
                'sequencing', 'ec']
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

    def get_success_url(self): 
        return reverse('gene', kwargs = {'pk': self.object.pk })



def list(request, type):
    print('the type is ' + type)
    genes = Gene.objects.filter(entity__exact=type)
    master_genes = Gene.objects.all()
    print(genes)
    return render(request, 
                  'genedata/list.html', 
                  {'genes': genes,'master_genes': master_genes,  'type': type})



def create_ec(request):
    master_genes = Gene.objects.all()
    if request.method == 'POST':
        form = EcForm(request.POST) 
        if form.is_valid():
            ec = Ec()
            ec.ec_name = form.cleaned_data['ec_name']
            ec.save()
            return HttpResponseRedirect("/create_ec")
        else:
            form = EcForm()
            ecs = Ec.objects.all()
            print("EC is not valid")
            return render(request, 'genedata/create_ec.html', {'error': 'failed', 'ecs': ecs, 'master_genes': master_genes, 'form': form})
 
    else:
        ecs = Ec.objects.all()
        form = EcForm()
        return render(request, 'genedata/create_ec.html', {'ecs': ecs, 'master_genes': master_genes, 'form': form})


def spa(request):
    return render(request, 'genedata/spa.html')
