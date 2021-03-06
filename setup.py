from distutils.core import setup
import os

# Stolen from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('tt_dailyemailblast'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len('tt_dailyemailblast/'):]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(
    name='tt_dailyemailblast',
    version='0.5.2',
    description='Texas Tribune: tt_dailyemailblast',
    author='Tribune Tech',
    author_email='tech@texastribune.org',
    url='http://github.com/texastribune/tt_dailyemailblast/',
    packages=packages,
    package_data={'tt_dailyemailblast': data_files},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
