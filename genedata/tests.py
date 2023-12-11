import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy


from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


from .model_factories import *
from .serializers import *

from random import randint
from random import choice


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
        self.assertEqual(data['entity'], self.gene1.entity)
        print(data['gene_id'])

        
        
    def test_geneDetailReturnFailureOnBadPk(self):
        response = self.client.get(self.bad_url)
        self.assertEqual(response.status_code, 404)

    def test_geneDetailDeleteSuccess(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, 204)


class GeneSerializeTest(APITestCase):
    gene1 = None
    serializer = None

    def setUp(self):
        self.gene1 = GeneFactory.create(pk=1, gene_id="gene1") 
        self.serializer = GeneSerializer(self.gene1)

    def tearDown(self):
        Ec.objects.all().delete()
        Sequencing.objects.all().delete()
        Gene.objects.all().delete()
        ECFactory.reset_sequence(0)
        SequencingFactory.reset_sequence(0)
        GeneFactory.reset_sequence(0)

    def test_geneserializer(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['gene_id', 'entity','source', 
                                                'start', 'stop', 'start_codon', 
                                                 'sequencing', 'ec']))

    def test_serializerGeneIDhasCorrectData(self):
        data = self.serializer.data
        self.assertEqual(data['gene_id'], 'gene1')


class GeneListTest(APITestCase):
    good_url = None

    def setUp(self):
        self.good_url = reverse('gene_list_api')
        self.gene1 = GeneFactory.create() 
        self.gene2 = GeneFactory.create() 

    def tearDown(self):
        Ec.objects.all().delete()
        Sequencing.objects.all().delete()
        Gene.objects.all().delete()
        ECFactory.reset_sequence(0)
        SequencingFactory.reset_sequence(0)
        GeneFactory.reset_sequence(0)

    def test_geneListReturnSuccess(self):
        response = self.client.get(self.good_url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        print("data is", data)
        self.assertEqual(data[0]['entity'], self.gene1.entity)
        self.assertEqual(data[1]['gene_id'], 'gene2')
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['sequencing']['factory'], 'Sanger')
        






    # def test_geneDetailReturnSuccess(self):
    #     response = self.client.get(self.good_url, format='json')
    #     self.assertEqual(response.status_code, 200) 
    #     data = json.loads(response.content)
    #     self.assertTrue('entity' in data)
    #     self.assertEqual(data['entity'], self.gene1.entity)
    #     print(data['gene_id'])
