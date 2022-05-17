from django import template
from news.models import Category

rigister = template.Library()

@rigister.simple_tag()
def get_categories():
    return Category.objects.all()