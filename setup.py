from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

from dsacheck import __version__ as VERSION

setup(name="DsaCheck",
      version=VERSION,
      author = "Adelux",
      author_email = "luc stepniewski at adelux.fr",
      download_url = "http://code.google.com/p/dsacheck",
      license = "GPL",
      keywords = "debian deb python packages dpkg",
      description = "DsaCheck checks if your Debian system is up to date according to DSA security advisories.",
      long_description = """
DsaCheck checks if your Debian system is up to date according to DSA security advisories.""",

      url = "http://code.google.com/p/dsacheck",
      packages = find_packages(exclude=['tests','ez_setup']),
      scripts = ["dsaCheck", ],
      entry_points = {
          'console_scripts': [
              'dsaCheck = dsacheck.dsacheck:main'
            ]
          },

      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],

      test_suite = "nose.collector",
      )
