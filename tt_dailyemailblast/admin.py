from django.contrib import admin
from django.db import models as django_models
from tinymce.widgets import TinyMCE

from .models import (Recipient, RecipientList, DailyEmailBlast,
        DailyEmailBlastType)


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
    formfield_overrides = {
        django_models.TextField: {'widget': TinyMCE()},
    }



admin.site.register(DailyEmailBlastType)
admin.site.register(Recipient)
admin.site.register(RecipientList, RecipientListAdmin)
admin.site.register(DailyEmailBlast, DailyEmailBlastAdmin)
