from armstrong.utils.backends import GenericBackend
from django.db import models
from django.template import Context
from django.template.loader import select_template

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
        utils.dispatch_to_backend(
            'TT_DAILYEMAILBLAST_RECIPIENT',
            'tt_dailyemailblast.send_backends.sync.sync_recipient',
            self, recipient_list, blast)


class RecipientList(NamedSlugMixin, models.Model):
    name = models.CharField(max_length=255)
    recipients = models.ManyToManyField(Recipient, related_name='lists',
                                        editable=False)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.recipients.count())

    def send(self, blast):
        utils.dispatch_to_backend(
            'TT_DAILYEMAILBLAST_RECIPIENTLIST',
            'tt_dailyemailblast.send_backends.sync.sync_recipients_list',
            self, blast)


class DailyEmailBlastType(NamedSlugMixin, models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class DailyEmailBlast(models.Model):
    blast_type = models.ForeignKey(DailyEmailBlastType, related_name='blasts')
    created_on = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    recipient_lists = models.ManyToManyField(RecipientList,
            related_name='blasts', editable=False)
    sent_on = models.DateTimeField(null=True)
    send_completed_on = models.DateTimeField(null=True)

    class Meta:
        ordering = ('-created_on',)

    def __unicode__(self):
        return u'%s (%s)' % (self.blast_type, self.created_on)

    def send(self):
        utils.dispatch_to_backend(
            'TT_DAILYEMAILBLAST_BLASTBACKEND',
            'tt_dailyemailblast.send_backends.sync.sync_daily_email_blasts',
            self)

    def render(self, recipient, recipient_list):
        templates = utils.get_template_names(self, recipient_list, recipient)
        template = select_template(templates)
        context_data = self.get_context_data(recipient, recipient_list)
        context = Context(context_data)
        return template.render(context)

    def get_context_data(self, recipient, recipient_list):
        context_backend = GenericBackend('TT_DAILYEMAILBLAST_CONTEXT',
                defaults=['tt_dailyemailblast.context_backends.basic'])
        return context_backend.get_backend(self, recipient, recipient_list)
