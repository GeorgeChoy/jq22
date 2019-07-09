from django import template
from datetime import date, timedelta

#this is an example of a filter which samples a date to see whether it is today, in past or in future.
#the date is passed in as an argument(value). You need to load this into your template header.
#see index.html. there is a {% load app_filters %}
register = template.Library()
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