from armstrong.utils.backends import GenericBackend
from django.db import models
from django.template import Template
try:
    from django.utils.text import slugify
except ImportError:
    from django.template.defaultfilters import slugify


from . import utils


class NamedSlugMixin(object):
    @property
    def slug(self):
        return slugify(self.name)


class Recipient(NamedSlugMixin, models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)

    def send(self, recipient_list, blast):
        utils.dispatch_to_backend('TT_DAILYEMAILBLAST_RECIPIENT',
                'tt_dailyemailblast.send_backends.sync.recipient',
                self, recipient_list, blast)


class RecipientList(NamedSlugMixin, models.Model):
    name = models.CharField(max_length=255)
    recipients = models.ManyToManyField(Recipient, related_name='lists',
                                        editable=False)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.recipients.count())

    def send(self, blast):
        utils.dispatch_to_backend('TT_DAILYEMAILBLAST_RECIPIENTLIST',
                'tt_dailyemailblast.send_backends.sync.recipient_list',
                self, blast)


class DailyEmailBlastType(NamedSlugMixin, models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class DailyEmailBlast(models.Model):
    blast_type = models.ForeignKey(DailyEmailBlastType, related_name='blasts')
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    recipient_lists = models.ManyToManyField(RecipientList,
            related_name='blasts')

    def __unicode__(self):
        return u'%s (%s)' % (self.blast_type, self.created_on)

    def send(self):
        utils.dispatch_to_backend('TT_DAILYEMAILBLAST_BLASTBACKEND',
                'tt_dailyemailblast.send_backends.sync.daily_email_blasts',
                self)

    def render(self, recipient, recipient_list):
        context = self.get_context_data(recipient, recipient_list)
        t = Template(utils.get_template_names(self, recipient_list,
                recipient))
        return t.render(context)

    def get_context_data(self, recipient, recipient_list):
        context_backend = GenericBackend('TT_DAILYEMAILBLAST_CONTEXT',
                defaults=['tt_dailyemailblast.context_backend.basic'])
        return context_backend(self, recipient, recipient_list)
