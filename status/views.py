from __future__ import unicode_literals
import calendar
import datetime

from django.shortcuts import render, get_object_or_404
from django.utils.datastructures import SortedDict
from django.utils.timezone import now

from .models import Incident, Component, Chart


def index(request):
    # Get last 2 weeks of incidents
    DAYS = 14

    offset_days = 0
    today = datetime.datetime.today()
    start = (today - datetime.timedelta(days=offset_days))
    end = (start - datetime.timedelta(days=DAYS)).date()

    incidents = Incident.objects.filter(datetime_created__gte=end)

    dates = ((start - datetime.timedelta(days=d)).date() for d in range(0, DAYS))
    incidents_grouped = SortedDict()

    for date in dates:
        incidents_grouped[date] = [i for i in incidents if i.datetime_created.date() == date]

    components = [Component.objects.all()[0]]

    charts = Chart.objects.all()

    if len(components) == 1:
        problem = components[0].status
    else:
        problem = max(*[p.status for p in components])

    return render(request, 'status/index.html', {
        'charts': charts,
        'dates': incidents_grouped,
        'problem': problem,
        'components': components,
        'today': today,
    })


def incident(request, pk):
    obj = get_object_or_404(Incident, pk=pk)

    return render(request, 'status/incident.html', {
        'object': obj,
    })


def history(request):
    incidents = Incident.objects.all()

    today = now().date().replace(day=1)

    def add_months(source_date, months):
        month = source_date.month - 1 + months
        year = source_date.year + month / 12
        month = month % 12 + 1
        day = min(source_date.day, calendar.monthrange(year, month)[1])

        return datetime.date(year, month, day)

    months = [add_months(today, -n) for n in range(12)]

    grouped_incidents = SortedDict()

    for m in months:
        grouped_incidents[m] = [i for i in incidents if i.datetime_created.year == m.year and i.datetime_created.month == m.month]

    return render(request, 'status/history.html', {
        'object_list': grouped_incidents,
    })
