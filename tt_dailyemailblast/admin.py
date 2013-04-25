from django.contrib import admin
from django.db import models as django_models
from tinymce.widgets import TinyMCE

from .models import (Recipient, RecipientList, DailyEmailBlast,
        DailyEmailBlastType)


def send_blasts(model_admin, request, qs):
    for blast in qs:
        blast.send()


class RecipientInline(admin.TabularInline):
    model = RecipientList.recipients.through
    verbose_name = 'recipient'
    verbose_name_plural = 'recipients'


class RecipientListAdmin(admin.ModelAdmin):
    model = RecipientList
    inlines = [RecipientInline]


class RecipientListInline(admin.TabularInline):
    model = DailyEmailBlast.recipient_lists.through
    verbose_name = 'recipient list'
    verbose_name_plural = 'recipient lists'


class DailyEmailBlastAdmin(admin.ModelAdmin):
    model = DailyEmailBlast
    inlines = [RecipientListInline]
    list_display = ('blast_type', 'recipients',
                    'created_on', 'sent_on', 'send_completed_on',)
    formfield_overrides = {
        django_models.TextField: {'widget': TinyMCE()},
    }
    actions = [send_blasts]

    def get_queryset(self, request):
        qs = super(DailyEmailBlastAdmin, self).get_queryset()
        return qs.prefetch_related('recipient_lists')

    def recipients(self, blast):
        return u', '.join([unicode(l) for l in blast.recipient_lists.all()])


admin.site.register(DailyEmailBlastType)
admin.site.register(Recipient)
admin.site.register(RecipientList, RecipientListAdmin)
admin.site.register(DailyEmailBlast, DailyEmailBlastAdmin)
