from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    master_genes = Gene.objects.all()
    return render(request, 
                  'genedata/index.html', 
                  {'master_genes': master_genes})

def gene(request, pk):
    gene = Gene.objects.get(id = pk)
    master_genes = Gene.objects.all()
    gene.access += 1
    gene.save()
    print ('gene.access = ' + str(gene.access))
    return render(request, 
                  'genedata/gene.html', 
                  {'gene': gene, 'master_genes': master_genes})

def list(request, type):
    print('the type is ' + type)
    genes = Gene.objects.filter(entity__exact=type)
    master_genes = Gene.objects.all()
    print(genes)
    return render(request, 
                  'genedata/list.html', 
                  {'genes': genes,'master_genes': master_genes,  'type': type})

def poslist(request):
    genes = Gene.objects.filter(entity__exact='Chromosome').filter(start_codon='+')
    master_genes = Gene.objects.all()
    print(genes)
    return render(request, 
                  'genedata/list.html', 
                  {'genes': genes, 'master_genes': master_genes, 'type': type})

def delete(request, pk):
    GeneAttributeLink.objects.filter(gene_id=pk).delete()
    gene_to_delete = Gene.objects.filter(id=pk)
    gene_to_delete.delete()
    return HttpResponseRedirect('/')

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

def create_gene(request):
    master_genes = Gene.objects.all()
    if request.method == 'POST':
        form = GeneForm(request.POST)
        if form.is_valid():
            gene = form.save() 
            return HttpResponseRedirect("/create_gene")
        else:
            return render(request, 'genedata/create_gene.html', {'error': 'failed',  'master_genes': master_genes, 'form': form})
    else:
        form = GeneForm()
        return render(request, 'genedata/create_gene.html', {'master_genes': master_genes, 'form': form})


