from django.db import models
from django.template import Template
from django.util.text import slugify

from . import email


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


class DailyEmailBlast(NamedSlugMixin, models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    receipient_lists = models.ManyToManyField(ReceipientList,
            related_name='blasts')

    def send(self):
        for l in self.receipient_lists.all():
            l.send(self)

    def render(self, receipient, receipient_list):
        context = {
            'receipient': receipient,
            'receipient_list': receipient_list,
            'blast': self,
        }
        t = Template(get_template_names(self, receipient_list, receipient))
        return t.render(context)


def get_template_names(blast, receipient_list, receipient):
    return [
        'tt_dailyemailblast/%s/%s/%s.html' % (blast.slug, receipient_list.slug,
                receipient.slug),
        'tt_dailyemailblast/%s/%s.html' % (blast.slug, receipient_list.slug),
        'tt_dailyemailblast/%s.html' % blast.slug,
    ]
