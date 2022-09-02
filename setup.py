try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'SHT',
      version           = '1.0.0',
      author            = 'EmbdEzaz9',
      author_email      = 'sendtoezaz@gmail.com',
      description       = 'Library for accessing the SHT series temperature and humidity sensors like the SHT21/SHT31 on any Riscv Architech.',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/EmbdEzaz9/Sht21-Sensor.git',
      dependency_links  = [],
      install_requires  = [],
      packages          = find_packages())
