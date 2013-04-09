from django.db import models


class Receipient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)


class ReceipientList(models.Model):
    name = models.CharField(max_length=255)
    receipients = models.ManyToManyField(Receipient, related_name='lists')

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.receipients.count())


class DailyEmailBlast(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
