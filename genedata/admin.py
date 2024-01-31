from django.contrib import admin
from .models import *

class GeneAttributeLinkInLine(admin.TabularInline):
    model = GeneAttributeLink
    extra = 3



class GeneAdmin(admin.ModelAdmin):
    list_display = ('gene_id', 'entity', 
                    'source', 'start', 
                    'stop')
    inlines = [GeneAttributeLinkInLine]

class SequencingAdmin(admin.ModelAdmin):
    list_display = ('factory', 'location')

class EcAdmin(admin.ModelAdmin):
    list_display = ('ec_name', )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('type', 'product', 'gene_id')

class AttributeAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')

admin.site.register(Gene, GeneAdmin)
admin.site.register(Sequencing, SequencingAdmin)
admin.site.register(Ec, EcAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(AppUser)
