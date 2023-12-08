import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy


from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


from .model_factories import *
from .serializers import *

class GeneTest(APITestCase):
    gene1 = None
    gene2 = None
    good_url = ''
    bad_url = ''
    delete_url = ''
    
    def setUp(self):
        self.gene1 = GeneFactory.create(pk=1, gene_id="gene1") 
        self.gene2 = GeneFactory.create(pk=2, gene_id="gene2")
        self.gene3 = GeneFactory.create(pk=3, gene_id="gene3")
        self.good_url = reverse('gene_detail_api', kwargs={'pk': 1})
        self.delete_url = reverse('gene_detail_api', kwargs={'pk': 3})
        self.bad_url = '/api/gene/H'


    def tearDown(self):
        Ec.objects.all().delete()
        Sequencing.objects.all().delete()
        Gene.objects.all().delete()
        ECFactory.reset_sequence(0)
        SequencingFactory.reset_sequence(0)
        GeneFactory.reset_sequence(0)
        

    def test_geneDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        self.assertEqual(response.status_code, 200) 

        data = json.loads(response.content)
        self.assertTrue('entity' in data)
        self.assertEqual(data['entity'], 'Plasmid')

        
        
    def test_geneDetailReturnFailureOnBadPk(self):
        response = self.client.get(self.bad_url)
        self.assertEqual(response.status_code, 404)

    def test_geneDetailDeleteSuccess(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, 204)


# Q. #todo Now we want to test that deleting records works.
# At the top of the class, create an empty delete_url string,
# Add a new gene 3 
# and add a URL for deleting it.The url has the same name as for 
# getting data from /api/gene/id, just change the pk in the kwargs 
# Next create a test for geneDetailDeletion. 
# Make the client delete the record. Remember that in the API file
#  when we have a successful delete, the status code was 204. 
# Assert that in your test

