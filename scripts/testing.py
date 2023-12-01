
# =============================================================================
# Configuring the script to work with the bioweb django project 
# =============================================================================


# -- Import OS -----------------------------------------------------------

import sys
import os
import django
import csv
from collections import defaultdict

sys.path.append('/home/quantumleap/Documents/git/uol/course/4_Level6S1/django/projects/topic2/bioweb')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bioweb.settings')

django.setup()

# -- Import models to be able to add data to models -----------------------------------------------------------

from genedata.models import *

# -- Import logging library -----------------------------------------------------------

import logging
logger = logging.getLogger(__name__)

# -- Define path to data -----------------------------------------------------------

 
data_file = '/home/quantumleap/Documents/git/uol/course/4_Level6S1/django/projects/topic2/bioweb/data.csv'

# =============================================================================
# Related Manager 
# =============================================================================


# Getting the first record ie the first instance of the gene model
someGene = Gene.objects.all()[0]
print(someGene)
# Getting the queryset if linked attributes to the gene. Attention you must use lowercases
links = someGene.geneattributelink_set.all()
print(links)
for link in links:
    print(str(link.attribute.key) + ' : ' + str(link.attribute.value))



# =============================================================================
# Filtering 
# =============================================================================
filteredGenes = Gene.objects.filter(entity__exact = "Chromosome")
print(filteredGenes)