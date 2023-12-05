import datetime
from django import template
from ..models import Gene
register = template.Library()

@register.simple_tag
def todays_date():
    return datetime.datetime.now().strftime("%d %b, %Y")

@register.simple_tag
def authors_name(): 
    return "Cabrero"

@register.simple_tag
def gene_count():
    return len(Gene.objects.all())


