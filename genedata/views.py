from typing import Any, Dict, List
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from .models import *
from .forms import *

# Create your views here.

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
    success_url = '/'

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
