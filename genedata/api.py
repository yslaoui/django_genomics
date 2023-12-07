from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from .models import *
from .serializers import *

@csrf_exempt
def gene_detail(request, pk):
    try: 
        gene= Gene.objects.get(pk=pk)
    except Gene.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GeneSerializer(gene)
        return JsonResponse(serializer.data)

@csrf_exempt
def genes_list(request):
    try: 
        gene = Gene.objects.all()
    except Gene.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GeneSerializer(gene, many = True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)           



