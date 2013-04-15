from django.db import models
from django.template import Template
try:
    from django.utils.text import slugify
except ImportError:
    from django.template.defaultfilters import slugify


from . import email
from . import utils


class NamedSlugMixin(object):
    @property
    def slug(self):
        return slugify(self.name)


class Receipient(NamedSlugMixin, models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)

    def send(self, receipient_list, blast):
        email.send_email(blast.render(self, receipient_list))


class ReceipientList(NamedSlugMixin, models.Model):
    name = models.CharField(max_length=255)
    receipients = models.ManyToManyField(Receipient, related_name='lists')

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.receipients.count())

    def send(self, blast):
        for r in self.receipients.all():
            r.send(blast)


class DailyEmailBlastType(NamedSlugMixin, models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class DailyEmailBlast(models.Model):
    blast_type = models.ForeignKey(DailyEmailBlastType, related_name='blasts')
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    receipient_lists = models.ManyToManyField(ReceipientList,
            related_name='blasts')

    def __unicode__(self):
        return u'%s (%s)' % (self.blast_type, self.created_on)

    def send(self):
        for l in self.receipient_lists.all():
            l.send(self)

    def render(self, receipient, receipient_list):
        context = self.get_context_data(receipient, receipient_list)
        t = Template(utils.get_template_names(self, receipient_list,
                receipient))
        return t.render(context)

    def get_context_data(self, receipient, receipient_list):
        return {
            'receipient': receipient,
            'receipient_list': receipient_list,
            'blast': self,
        }
