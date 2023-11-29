from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    genes = Gene.objects.all()
    return render(request, 
                  'genedata/index.html', 
                  {'genes': genes})

def gene(request, pk):
    gene = Gene.objects.get(id = pk)
    return render(request, 
                  'genedata/gene.html', 
                  {'gene': gene})

