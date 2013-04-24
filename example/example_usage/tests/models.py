import datetime

from django.test import TestCase

from tt_dailyemailblast import models
from tt_dailyemailblast.tests import factories


class DailyEmailBlastTestCase(TestCase):
    def setUp(self):
        self.blast_type = factories.DailyEmailBlastTypeFactory.create()

    def test_unicode_output(self):
        created_on = datetime.datetime.now()
        blast = models.DailyEmailBlast.objects.create(
                body='Some random blast', blast_type=self.blast_type)
        expected_pattern = '^%s \(%04d-%02d-%02d.*\)$' % (blast.blast_type.name,
                created_on.year, created_on.month, created_on.day)
        self.assertRegexpMatches(unicode(blast), expected_pattern)
