from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def gene_detail(request, pk):
    try: 
        gene= Gene.objects.get(pk=pk)
    except Gene.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GeneSerializer(gene)
        return Response(serializer.data)
    if request.method == 'POST':
        print(request.data)
        serializer = GeneSerializer(gene)
        return Response(serializer.data)

@api_view(['GET'])
def genes_list(request):
    try: 
        gene = Gene.objects.all()
    except Gene.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GeneSerializer(gene, many = True)
        print(serializer.data)
        return Response(serializer.data)           


