import factory

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
    gene_id = 'geneX'
    entity = 'Plasmid'
    source = 'nothing'
    start = 12
    stop = 45
    start_codon = 'U'
    ec = factory.SubFactory(ECFactory)
    sequencing = factory.SubFactory(SequencingFactory)

    class Meta:
        model = Gene



