from django.db import models

class Gene(models.Model):
    gene_id = models.CharField(max_length=256, null=False, blank=False)
    entity = models.CharField(max_length=256, null=False, blank=False)
    source = models.CharField(max_length=256, null=False, blank=True)
    