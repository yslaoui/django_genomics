import factory
from random import randint
from random import choice


from .models import *

class ECFactory(factory.django.DjangoModelFactory):
    ec_name = 'transferase'

    class Meta:
        model = Ec

class SequencingFactory(factory.django.DjangoModelFactory):
    factory= 'Sanger'
    location = 'UK'

    class Meta:
        model = Sequencing

class GeneFactory(factory.django.DjangoModelFactory):
    gene_id = factory.Sequence(lambda n: 'gene%d'%(n+1))
    entity = choice(['Plasmid', 'Chromosome'])
    source = 'nothing'
    start = randint(1, 10000)
    stop = start + randint(1, 10000)
    stop = 45
    start_codon = 'U'
    ec = factory.SubFactory(ECFactory)
    sequencing = factory.SubFactory(SequencingFactory)

    class Meta:
        model = Gene



# class GeneFactory(factory.django.DjangoModelFactory):
#     gene_id = 'geneX'
#     entity = 'Plasmid'
#     source = 'nothing'
#     start = 12
#     stop = 45
#     start_codon = 'U'
#     ec = factory.SubFactory(ECFactory)
#     sequencing = factory.SubFactory(SequencingFactory)

#     class Meta:
#         model = Gene



