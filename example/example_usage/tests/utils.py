from django.test import TestCase

from tt_dailyemailblast import utils
from tt_dailyemailblast.tests import factories


def with_test_names(func):
    def inner(self, *args, **kwargs):
        for name in ['alice', 'bob']:
            func(self, name, *args, **kwargs)
    return inner


class get_template_namesTestCase(TestCase):
    def setUp(self):
        self.blast = factories.DailyEmailBlastFactory.create()
        alice = factories.RecipientFactory.create(name='Alice')
        bob = factories.RecipientFactory.create(name='Bob')
        recipient_list = factories.RecipientListFactory.create()
        recipient_list.recipients = [alice, bob]
        self.blast.recipient_lists = [recipient_list, ]

        self.template_names_for_alice = utils.get_template_names(self.blast,
                recipient_list, alice)
        self.template_names_for_bob = utils.get_template_names(self.blast,
                recipient_list, bob)

    @with_test_names
    def test_uses_full_recipient_as_first_name(self, name):
        expected = 'tt_dailyemailblast/%s/%s/%s.html' % (
                self.blast.blast_type.slug,
                self.blast.recipient_lists.all()[0].slug, name)
        actual = getattr(self, 'template_names_for_%s' % name)[0]
        self.assertEqual(expected, actual, msg='expected slug for %s' % name)

    @with_test_names
    def test_uses_type_and_list_in_slug_as_second_fallback(self, name):
        recipient_list = self.blast.recipient_lists.all()[0]
        expected = 'tt_dailyemailblast/%s/%s.html' % (
                self.blast.blast_type.slug, recipient_list.slug)
        actual = getattr(self, 'template_names_for_%s' % name)[1]
        self.assertEqual(expected, actual, msg='expected slug for %s' %
                recipient_list)

    @with_test_names
    def test_uses_blast_type_as_final_fallback(self, name):
        expected = 'tt_dailyemailblast/%s.html' % self.blast.blast_type.slug
        actual = getattr(self, 'template_names_for_%s' % name)[-1]
        self.assertEqual(expected, actual, msg='expected slug for %s' %
                self.blast.blast_type)
