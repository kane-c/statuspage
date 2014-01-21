from django.contrib import admin

from . import models


class IncidentStatusInline(admin.StackedInline):
    model = models.IncidentStatus
    extra = 1


class IncidentAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'datetime_created',
    )

    inlines = (
        IncidentStatusInline,
    )


class PieceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'status',
    )

    list_editable = (
        'status',
    )

admin.site.register(models.Component, PieceAdmin)
admin.site.register(models.Chart)
admin.site.register(models.Incident, IncidentAdmin)
