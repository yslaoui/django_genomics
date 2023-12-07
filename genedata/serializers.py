from rest_framework import serializers
from .models import *

class SequencingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencing
        fields = ['id', 'factory', 'location']

class ECSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ec
        fields = ['id', 'ec_name']


class GeneSerializer(serializers.ModelSerializer):
   ec = ECSerializer()
   sequencing = SequencingSerializer()
   class Meta:
       model = Gene
       fields = ['gene_id', 'entity',
                 'source', 'start',
                 'stop', 'start_codon',
                 'sequencing', 'ec']
       
