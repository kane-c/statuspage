from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import date
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Component(models.Model):
    STATUS_OPERATIONAL = 0
    STATUS_DEGRADED_PERFORMANCE = 1
    STATUS_PARTIAL_OUTAGE = 2
    STATUS_MAJOR_OUTAGE = 3

    STATUSES = (
        (STATUS_OPERATIONAL, 'Operational',),
        (STATUS_DEGRADED_PERFORMANCE, 'Degraded performance',),
        (STATUS_PARTIAL_OUTAGE, 'Partial outage',),
        (STATUS_MAJOR_OUTAGE, 'Major outage',),
    )

    STATUS_CLASSES = (
        # Bootstrap 3 alert classes
        (STATUS_OPERATIONAL, 'success',),
        (STATUS_DEGRADED_PERFORMANCE, 'info',),
        (STATUS_PARTIAL_OUTAGE, 'warning',),
        (STATUS_MAJOR_OUTAGE, 'danger',),
    )

    name = models.CharField(max_length=100)
    status = models.PositiveSmallIntegerField(choices=STATUSES)

    def __str__(self):
        return self.name

    def get_status_class(self):
        return Component.STATUS_CLASSES[self.status][1]


@python_2_unicode_compatible
class Incident(models.Model):
    title = models.CharField(max_length=100)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def date_range(self):
        updates = self.status_updates.all()

        first = updates[0]

        last = updates.order_by('datetime_created')[0]

        if first.datetime_created.date() == last.datetime_created.date():
            return '%s-%s' % (date(first.datetime_created, 'M d, G:i'),
                              date(last.datetime_created, 'G:i T'))
        else:
            return '%s - %s' % (date(first.datetime_created, 'M d, G:i'),
                                date(last.datetime_created, 'M d, G:i T'))

    def get_absolute_url(self):
        return reverse('incident', args=(self.pk,))


@python_2_unicode_compatible
class IncidentStatus(models.Model):
    TYPE_INVESTIGATING = 0
    TYPE_IDENTIFIED = 1
    TYPE_MONITORING = 2
    TYPE_RESOLVED = 3

    TYPE_CHOICES = (
        (TYPE_INVESTIGATING, 'Investigating',),
        (TYPE_IDENTIFIED, 'Identified',),
        (TYPE_MONITORING, 'Monitoring',),
        (TYPE_RESOLVED, 'Resolved',),
    )

    incident = models.ForeignKey(Incident, related_name='status_updates')
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_type_display()

    def full_description(self):
        return '**%s** - %s' % (self.get_type_display(), self.description)

    class Meta:
        ordering = '-datetime_created',


@python_2_unicode_compatible
class Chart(models.Model):
    name = models.CharField(max_length=100)
    html = models.TextField(verbose_name='HTML')

    def __str__(self):
        return self.name
