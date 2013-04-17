from . import email


def sync_daily_email_blasts(blast):
    for l in blast.recipients_lists.all():
        l.send(blast)


def sync_recipients_list(recipients_list, blast):
    for r in recipients_list.recipientss.all():
        r.send(recipients_list, blast)


def sync_recipients(recipients, recipients_list, blast):
    email.send_email(blast.render(recipients, recipients_list))
