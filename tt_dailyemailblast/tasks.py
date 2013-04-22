from celery.task import task

from . import models
from .send_backends import sync


@task
def send_daily_email_blasts(blast_pk):
    blast = models.DailyEmailBlast.objects.get(pk=blast_pk)
    sync.sync_daily_email_blasts(blast)


@task
def send_recipients_list(recipients_list_pk, blast_pk):
    blast = models.DailyEmailBlast.objects.get(pk=blast_pk)
    recipients_list = models.RecipientList.objects.get(pk=recipients_list_pk)
    sync.sync_recipients_list(recipients_list, blast)


@task
def send_recipient(recipient_pk, recipients_list_pk, blast_pk):
    blast = models.DailyEmailBlast.objects.get(pk=blast_pk)
    recipients_list = models.RecipientList.objects.get(pk=recipients_list_pk)
    recipient = models.Recipient.objects.get(pk=recipient_pk)
    sync.sync_recipient(recipient, recipients_list, blast)
