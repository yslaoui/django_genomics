from rest_framework import serializers
from .models import *


class GeneSerializer(serializers.ModelSerializer):
   class Meta:
       model = Gene
       fields = ['gene_id', 'entity',
                 'source', 'start',
                 'stop', 'start_codon',
                 'sequencing', 'ec']
