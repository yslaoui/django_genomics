from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *


# Create your views here.

def index(request):
    genes = Gene.objects.all()
    return render(request, 
                  'genedata/index.html', 
                  {'genes': genes})

def gene(request, pk):
    gene = Gene.objects.get(id = pk)
    gene.access += 1
    gene.save()
    print ('gene.access = ' + str(gene.access))
    return render(request, 
                  'genedata/gene.html', 
                  {'gene': gene})

def list(request, type):
    print('the type is ' + type)
    genes = Gene.objects.filter(entity__exact=type)
    print(genes)
    return render(request, 
                  'genedata/list.html', 
                  {'genes': genes, 'type': type})

def poslist(request):
    genes = Gene.objects.filter(entity__exact='Chromosome').filter(start_codon='+')
    print(genes)
    return render(request, 
                  'genedata/list.html', 
                  {'genes': genes, 'type': type})

def delete(request, pk):
    GeneAttributeLink.objects.filter(gene_id=pk).delete()
    gene_to_delete = Gene.objects.filter(id=pk)
    gene_to_delete.delete()
    return HttpResponseRedirect('/')


# class Gene(models.Model):
#     gene_id = models.CharField(max_length=256, null=False, blank=False, db_index=True)
#     entity = models.CharField(max_length=256, null=False, blank=False)
#     source = models.CharField(max_length=256, null=False, blank=True)
#     start = models.IntegerField(null=False, blank=True)
#     stop = models.IntegerField(null=False, blank=True)
#     start_codon = models.CharField(max_length=1, default='M')
#     sequencing = models.ForeignKey(Sequencing, on_delete=models.DO_NOTHING)
#     ec = models.ForeignKey(Ec, on_delete=models.DO_NOTHING)

