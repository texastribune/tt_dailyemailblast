tt_dailyemailblast
==================
Simple application for handling our daily emails to partners.

.. note:: This could be a *lot* more complex and do all manner of
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

Now you're ready to start using ``tt_dailyemailblast``.


Usage
-----
*TODO*


Example
-------
All of the usage is outlined, along with tests inside the ``example``
directory.  See that directory for more information on how to run the tests and
example project.

.. _pip: http://www.pip-installer.org/en/latest/

