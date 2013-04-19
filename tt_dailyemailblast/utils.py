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
    """Configure a GenericBackend and call it with `*args`.

    :param backend: Django setting name for the backend.
    :param default: Module path to the default backend.
    """
    GenericBackend(backend, defaults=[default, ]).get_backend(*args)
