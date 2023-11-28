
# Configuring the script to work with the bioweb django project
import os
import sys

import django
import csv
from collections import defaultdict

sys.path.append('/home/quantumleap/Documents/git/uol/course/4_Level6S1/django/projects/topic2/bioweb')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bioweb.settings')

django.setup()

# Import models to be able to add data to models
from genedata.models import *

# Import logging library
import logging
logger = logging.getLogger(__name__)



# Define path to data
data_file = '/home/quantumleap/Documents/git/uol/course/4_Level6S1/django/projects/topic2/bioweb/data.csv'


# Create data structures
genes = defaultdict(list)
sequencing = set()
ec = set()
products = defaultdict(dict)
attributes = defaultdict(dict)

# Populate data structures
with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') # csv_reader is an object that allows you to iterate over rows of your data. Each row is a list of values
    header = csv_reader.__next__() # skip the header
    for row in csv_reader:
        ec.add(row[8])
        sequencing.add((row[4], row[5]))
        genes[row[0]] = row[1:4] + row[6:9]
        product_pairs = row[9].split(';')
        attribute_pairs = row[10].split(';')
        for pair in attribute_pairs:
            tupple = pair.split(':')
            attributes[row[0]][tupple[0]] = tupple[1]
        for pair in product_pairs:
            tupple = pair.split(':')
            products[row[0]][tupple[0]] = tupple[1] 


# for elem in ec:
#     print(elem)
# for elem in product_pairs:
#     print(elem)
# print(genes)
# print(products)
print(attributes)


# Deleting data from database -- allows you to run the script as many time as you want without duplicating insertions
GeneAttributeLink.objects.all().delete()
Gene.objects.all().delete()
Ec.objects.all().delete()
Sequencing.objects.all().delete()
Attribute.objects.all().delete()
Product.objects.all().delete()

# Inserting data in database
 # foreign key dictionaries
ec_rows = {}
sequencing_rows = {}
gene_rows = {}
product_rows = {}

for entry in ec: # ec is a set of strings
    try:
        row = Ec.objects.create(ec_name=entry) # create an instance of Ec class. Equivalemntly insert the string entry in the ec_name column
        row.save() # save the data in the database. Attention migration is concerned with database schema, not data records
        ec_rows[entry] = row # saving the instance because it is a foreign key in gene data
    except Exception as e:
        logger.error(f"error creating EC object {e}")
print(ec_rows)

for entry in sequencing:
    try: 
        row = Sequencing.objects.create(factory = entry[0], 
                                        location = entry[1])
        row.save()
        sequencing_rows[entry[0]] = row
    except Exception as e:
        logger.error(f"Error creating Sequencing object {e}")
print(sequencing_rows)

for gene_id, data in genes.items():
    row = Gene.objects.create(gene_id = gene_id,
                              entity = data[0],
                              start = data[1],
                              stop = data[2],
                              start_codon = data[3],
                              ec = ec_rows[data[5]],
                              sequencing = sequencing_rows['Sanger'] 
                            )
    row.save()
    gene_rows[gene_id] = row
print(gene_rows)



for gene_id, data in products.items():
    for key in data.keys():        
        row = Product.objects.create(type = key, 
                                     product = data[key], 
                                     gene_id = gene_rows[gene_id])
        row.save()


for gene_id, data in attributes.items():
    for key in data.keys():
        row = Attribute.objects.create(key = key,                                        value=data[key])
        row.gene.add(gene_rows[gene_id])
        row.save()


