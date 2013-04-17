from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

from . import email


def sync_daily_email_blasts(blast):
    for l in blast.recipients_lists.all():
        l.send(blast)


def async_daily_email_blasts(blast):
    try:
        from .tasks import send_daily_email_blasts
    except ImportError, e:
        msg = _(u"Please install Celery before using the async backend: %s" % e)
        raise ImproperlyConfigured(msg)
    send_daily_email_blasts.apply_async(args=[blast.pk])


def sync_recipients_list(recipients_list, blast):
    for r in recipients_list.recipientss.all():
        r.send(recipients_list, blast)


def async_recipients_list(recipients_list, blast):
    try:
        from .tasks import send_recipients_list
    except ImportError, e:
        msg = _(u"Please install Celery before using the async backend: %s" % e)
        raise ImproperlyConfigured(msg)
    send_recipients_list.apply_async(args=[recipients_list.pk, blast.pk])


def sync_recipients(recipients, recipients_list, blast):
    email.send_email(blast.render(recipients, recipients_list))


def async_recipients(recipients, recipients_list, blast):
    try:
        from .tasks import send_recipients
    except ImportError, e:
        msg = _(u"Please install Celery before using the async backend: %s" % e)
        raise ImproperlyConfigured(msg)
    send_recipients.apply_async(args=[recipients.pk, recipients_list.pk,
            blast.pk])
