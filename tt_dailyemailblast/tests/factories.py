import factory

from .. import models


class ReceipientFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Receipient
    name = factory.LazyAttribute(lambda n: 'Alice Example {0}'.format(n))
    email = factory.LazyAttribute(lambda n: 'alice{0}@example.com'.format(n))


class ReceipientListFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.ReceipientList
    name = factory.LazyAttribute(
            lambda n: 'Random Receipient List {0}'.format(n))
    receipients = factory.RelatedFactory(ReceipientFactory)


class DailyEmailBlastTypeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.DailyEmailBlastType
    name = factory.LazyAttribute(lambda n: 'Blast Type {0}'.format(n))


class DailyEmailBlastFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.DailyEmailBlast
    body = factory.LazyAttribute(lambda n: 'Some random body {0}'.format(n))
    receipient_lists = factory.RelatedFactory(ReceipientListFactory)
    blast_type = factory.SubFactory(DailyEmailBlastTypeFactory)
