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
   ec = ECSerializer(read_only=True)
   sequencing = SequencingSerializer(read_only=True)
   class Meta:
       model = Gene
       fields = [ 'id', 'gene_id', 'entity',
                 'source', 'start',
                 'stop', 'start_codon',
                 'sequencing', 'ec']    
    
   def create(self, validated_data):
       ec_data = self.initial_data["ec"]
       seq_data = self.initial_data["sequencing"] 
       gene = Gene(**{**validated_data, 
                      'ec': Ec.objects.get(pk=ec_data['id']), 
                      'sequencing': Sequencing.objects.get(pk=seq_data['id'])
                      })
       gene.save()
       return gene
   
