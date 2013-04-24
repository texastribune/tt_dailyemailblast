import factory

from .. import models


class RecipientFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Recipient
    name = factory.Sequence(lambda n: 'Alice Example {0}'.format(n))
    email = factory.Sequence(lambda n: 'alice{0}@example.com'.format(n))


class RecipientListFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.RecipientList
    name = factory.Sequence(
            lambda n: 'Random Recipient List {0}'.format(n))
    recipients = factory.RelatedFactory(RecipientFactory)


class DailyEmailBlastTypeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.DailyEmailBlastType
    name = factory.Sequence(lambda n: 'Blast Type {0}'.format(n))


class DailyEmailBlastFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.DailyEmailBlast
    body = factory.Sequence(lambda n: 'Some random body {0}'.format(n))
    recipient_lists = factory.RelatedFactory(RecipientListFactory)
    blast_type = factory.SubFactory(DailyEmailBlastTypeFactory)
