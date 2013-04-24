import logging

from armstrong.utils.backends import GenericBackend
from django.conf import settings

from .. import email

logger = logging.getLogger(__name__)


def sync_daily_email_blasts(blast):
    for l in blast.recipient_lists.all():
        l.send(blast)


def sync_recipient_list(recipients_list, blast):
    for r in recipients_list.recipients.all():
        logger.error('sync_recipient_list: %s %s %s' % (blast, recipients_list,
                r))
        r.send(recipients_list, blast)


def sync_recipient(recipient, recipients_list, blast):
    html = blast.render(recipient, recipients_list)
    context_backend = GenericBackend('TT_DAILYEMAILBLAST_CONTEXT',
            defaults=['tt_dailyemailblast.context_backends.basic'])
    context = context_backend.get_backend(blast, recipient, recipients_list)
    subject = blast.blast_type.name.format(**context)
    bodies = {'html': html}  # TODO: Support plain text rendering
    to = (recipient.email,)
    from_email = settings.TT_DAILYEMAILBLAST_FROMEMAIL
    headers = {}  # ???
    email.send_email(subject, bodies, from_email, to, headers)
