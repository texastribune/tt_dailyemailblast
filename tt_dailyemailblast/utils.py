from armstrong.utils.backends import GenericBackend


def get_template_names(blast, receipient_list, receipient):
    return [
        'tt_dailyemailblast/%s/%s/%s.html' % (blast.blast_type.slug,
                receipient_list.slug, receipient.slug),
        'tt_dailyemailblast/%s/%s.html' % (blast.blast_type.slug,
                receipient_list.slug),
        'tt_dailyemailblast/%s.html' % blast.blast_type.slug,
    ]


def dispatch_to_backend(backend, default, *args):
    GenericBackend(backend, defaults=[default, ])(*args)
