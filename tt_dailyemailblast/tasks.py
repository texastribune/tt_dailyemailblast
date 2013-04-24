import logging

from celery.task import task

from . import models
from .send_backends import sync

logger = logging.getLogger(__name__)


@task
def send_daily_email_blasts(blast_pk):
    blast = models.DailyEmailBlast.objects.get(pk=blast_pk)
    logger.error('Sending blast for %s' % blast)
    sync.sync_daily_email_blasts(blast)


@task
def send_recipients_list(recipients_list_pk, blast_pk):
    blast = models.DailyEmailBlast.objects.get(pk=blast_pk)
    recipients_list = models.RecipientList.objects.get(pk=recipients_list_pk)
    logger.error('Sending blast for %s to %s' % (blast, recipients_list))
    sync.sync_recipient_list(recipients_list, blast)


@task
def send_recipient(recipient_pk, recipients_list_pk, blast_pk):
    blast = models.DailyEmailBlast.objects.get(pk=blast_pk)
    recipients_list = models.RecipientList.objects.get(pk=recipients_list_pk)
    recipient = models.Recipient.objects.get(pk=recipient_pk)
    logger.error('Sending blast %s to %s of list %s' % (blast, recipient,
            recipients_list))
    sync.sync_recipient(recipient, recipients_list, blast)
