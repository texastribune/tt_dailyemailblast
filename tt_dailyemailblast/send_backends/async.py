from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

try:
    from .. import tasks
except ImportError, e:
    msg = _(u"Please install Celery before using the async backend: %s" % e)
    raise ImproperlyConfigured(msg)


def async_daily_email_blasts(blast):
    tasks.send_daily_email_blasts.apply_async(args=[blast.pk])


def async_recipients_list(recipients_list, blast):
    tasks.send_recipients_list.apply_async(args=[recipients_list.pk, blast.pk])


def async_recipient(recipient, recipients_list, blast):
    tasks.send_recipient.apply_async(args=[recipient.pk, recipients_list.pk,
            blast.pk])
