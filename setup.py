import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('git-github-reflog').read(),
    re.M
    ).group(1)

setup(
    name='git-github-reflog',
    version=version,
    description='reflog like interaction with Github',
    long_description=
    "A git extension for viewing the event log of a Github project.",
    url='https://github.com/criswell/github-reflog',
    author='Sam Hart',
    author_email='hartsn@gmail.com',

    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities'
    ],
    keywords='git github development',

    install_requires=[
        'requests', 'colorama'
    ],

    scripts=['git-github-reflog']
)
