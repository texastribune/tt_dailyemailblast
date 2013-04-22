from .. import email


def sync_daily_email_blasts(blast):
    for l in blast.recipient_lists.all():
        l.send(blast)


def sync_recipient_list(recipients_list, blast):
    for r in recipients_list.recipients.all():
        r.send(recipients_list, blast)


def sync_recipient(recipient, recipients_list, blast):
    email.send_email(blast.render(recipient, recipients_list))
