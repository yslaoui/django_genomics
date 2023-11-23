from django.db import models

class Sequencing(models.Model):
    factory = models.CharField(max_length=256, null=False, blank=False)
    location = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self) :
        return self.factory

class Ec(models.Model):
    ec_name = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.ec_name

class Gene(models.Model):
    gene_id = models.CharField(max_length=256, null=False, blank=False, db_index=True)
    entity = models.CharField(max_length=256, null=False, blank=False)
    source = models.CharField(max_length=256, null=False, blank=True)
    start = models.IntegerField(null=False, blank=True)
    stop = models.IntegerField(null=False, blank=True)
    start_codon = models.CharField(max_length=1, default='M')
    sequencing = models.ForeignKey(Sequencing, on_delete=models.DO_NOTHING)
    ec = models.ForeignKey(Ec, on_delete=models.DO_NOTHING)

    def __str__(self) :
        return self.gene_id

class Product(models.Model):
    type = models.CharField(max_length=256, null=False, blank=False)
    product = models.CharField(max_length=256, null=False, blank=False)
    gene_id = models.ForeignKey(Gene, on_delete= models.CASCADE)

    def __str__(self):
        return self.product

class Attribute(models.Model):
    key = models.CharField(max_length=256, null=False, blank=False)
    value = models.CharField(max_length=256, null=False, blank=False)
    gene = models.ManyToManyField(Gene, through="GeneAttributeLink")

    def __str__(self):
        return self.value

class GeneAttributeLink(models.Model):
    gene = models.ForeignKey(Gene, on_delete=models.DO_NOTHING) 
    attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)    

    def __str__(self):
        return self.key + " " + self.value