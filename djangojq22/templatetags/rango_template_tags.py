from django import template
from ..models import *
from datetime import date, timedelta
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import datetime

#these template tags are repeating methods not in views.py that are called from the template html. In this case it is called from
#index.html to display latest posts, todo list, etc.

register=template.Library()
@register.inclusion_tag('rango/cats.html')
def get_category_list():
    return {'cats':Category.objects.all()}

@register.simple_tag()
def total_categories():
    return Category.objects.count()
#def get_category_list(cat=None):
#    print(cat)
#    return ('python')
@register.inclusion_tag('djangojq22/latest_categories.html')
def show_latest_categories():
    latest_categories=Category.objects.all()[:2]
    return {'latest_categories':latest_categories}

@register.filter(name="longTime")
def longTime(aTime):
    return aTime.strftime("%m/%d/%Y %I:%M%p")

@register.filter(name='get_due_date_string')
def get_due_date_string(value):
    delta = value - date.today()
    if delta.days == 0:
        return "Today!"
    elif delta.days < 1:
        return "%s %s ago!" % (abs(delta.days),
            ("day" if abs(delta.days) == 1 else "days"))
    elif delta.days == 1:
        return "Tomorrow"
    elif delta.days > 1:
        return "In %s days" % delta.days

@register.filter(name='ellipses')
def ellipses(value, arg):
    original_string = value
    max_length = arg

    if len(original_string) <= max_length:
        return original_string
    else:
        return original_string[:max_length] + "..."