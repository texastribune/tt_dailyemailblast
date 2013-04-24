import logging

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
    subject = blast.subject
    bodies = {'html': html, 'text': 'This email requires HTML'}  # TODO: Support plain text rendering
    to = (recipient.email,)
    from_email = settings.TT_DAILYEMAILBLAST_FROMEMAIL
    headers = {}  # ???
    email.send_email(subject, bodies, from_email, to, headers)
