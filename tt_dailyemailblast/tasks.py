from celery.task import task

from . import models
from . import send_backends


@task
def send_daily_email_blasts(blast_pk):
    blast = models.DailyEmailBlast.objects.get(pk=blast_pk)
    send_backends.sync_daily_email_blasts(blast)


@task
def send_recipients_list(recipients_list_pk, blast_pk):
    blast = models.DailyEmailBlast.objects.get(pk=blast_pk)
    recipients_list = models.ReceipientList.objects.get(pk=recipients_list_pk)
    send_backends.sync_recipients_list(recipients_list, blast)


@task
def send_recipients(recipient_pk, recipients_list_pk, blast_pk):
    blast = models.DailyEmailBlast.objects.get(pk=blast_pk)
    recipients_list = models.ReceipientList.objects.get(pk=recipients_list_pk)
    recipient = models.Receipient.objects.get(pk=recipient_pk)
    send_backends.sync_recipient(recipient, recipients_list, blast)
