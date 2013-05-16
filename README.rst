tt_dailyemailblast
==================
Simple application for handling our daily emails to partners.

.. note::

  This could be a *lot* more complex and do all manner of
  awesome stuff like auto-generating the body based on stories that
  are in the CMS.  That's so much bigger than we need right now.

  This is definitely in the "works for what we need" camp, feel free
  to use it as an example of sending emails out using Celery, but
  probably not something to actually use.


Installation & Configuration
----------------------------
You can install this using `pip`_ like this::

    pip install tt_dailyemailblast

Once installed, you need to add it to your ``INSTALLED_APPS``.  You can do that
however you like or you can copy-and-paste this in after your
``INSTALLED_APPS`` are defined::

    INSTALLED_APPS += ['tt_dailyemailblast', ]

The next setting to configure is the **from** email address::

    TT_DAILYEMAILBLAST_FROMEMAIL = 'no-reply@texastribune.org'

``tt_dailyemailblast`` can accept any backend to suit your integration needs.

To send an email, you'll need a template for the **body**.
``tt_dailyemailblast`` will look for templates in your project in this order:

1. ``tt_dailyemailblast/<blast_type>/<recipient_list>/<recipient>.html``
2. ``tt_dailyemailblast/<blast_type>/<recipient_list>.html``
3. ``tt_dailyemailblast/<blast_type>.html``

If you need special context generated in that template, you can specify that
with the context backend setting::

    TT_DAILYEMAILBLAST_CONTEXT = 'tt.dailyemailblast.context_backend'

Finally, to actually send emails, ``tt_dailyemailblast`` will use the sync
backend by default. You can explicitly specify that with the setting::

    from tt_dailyemailblast.settings.sync import *

To use async Celery workers to send, add::

    from tt_dailyemailblast.settings.async import *


Usage
-----

Templates
~~~~~~~~~
Your templates should render to html. The context will get these variables:

* ``{{ blast }}`` - The ``DailyEmailBlast`` object.
* ``{{ recipient }}`` - The ``Recipient`` object.
* ``{{ recipient_list }}`` - The ``RecipientList`` object.

Context Backend
~~~~~~~~~~~~~~~
Your context backend should take the arguments:

* ``blast``
* ``recipient``
* ``recipient_list``

And should be patterened after this basic example::

    from tt_dailyemailblast.context_backends import basic

    def context_backend(blast, recipient, recipient_list):
        context = basic(blast, recipient, recipient_list)
        # modify context
        return context


Testing
-------

Testing is so easy! A one-armed driving bear could do it! Just follow these
steps:

1. Create a recipient list with only your email address
2. Create a blast
3. Make sure the blast has a template that will render
4. Fill in the ``Sent on`` and ``Sent completed on`` fields even though the
   blast has not been sent yet
5. Save the blast
6. Install ``pops``
7. Send the blast from the 'Send Now!' button

Example
-------
All of the usage is outlined, along with tests inside the ``example``
directory.  See that directory for more information on how to run the tests and
example project.

.. _pip: http://www.pip-installer.org/en/latest/

