def sync_dailyemailblasts(blast):
    for l in blast.receipient_lists.all():
        l.send(blast)


def sync_receipientlist(receipient_list, blast):
    for r in receipient_list.receipients.all():
        r.send(receipient_list, blast)


def sync_receipient(receipient, receipient_list, blast):
    email.send_email(blast.render(receipient, receipient_list))
