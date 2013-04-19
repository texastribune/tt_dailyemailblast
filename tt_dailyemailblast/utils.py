from armstrong.utils.backends import GenericBackend


def get_template_names(blast, recipient_list, recipient):
    return [
        'tt_dailyemailblast/%s/%s/%s.html' % (blast.blast_type.slug,
                recipient_list.slug, recipient.slug),
        'tt_dailyemailblast/%s/%s.html' % (blast.blast_type.slug,
                recipient_list.slug),
        'tt_dailyemailblast/%s.html' % blast.blast_type.slug,
    ]


def dispatch_to_backend(backend, default, *args):
    GenericBackend(backend, defaults=[default, ])(*args)
