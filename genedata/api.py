from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins




from .models import *
from .serializers import *

class GeneList(generics.ListAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer 

class GeneDetail(generics.GenericAPIView, 
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





class EcList(generics.ListAPIView):
    queryset = Ec.objects.all()
    serializer_class = ECSerializer



class EcDetail(generics.GenericAPIView, 
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Ec.objects.all()
    serializer_class = ECSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class GeneListType(generics.GenericAPIView, 
                 mixins.ListModelMixin):
    
    def get_queryset(self):
        print(self.kwargs)
        entity_type = self.kwargs.get('type', None)
        if entity_type:
            return Gene.objects.filter(entity__exact=entity_type)
        return Gene.objects.all()

    serializer_class = GeneSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
