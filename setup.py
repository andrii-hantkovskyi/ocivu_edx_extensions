"""
Setup file for ocivu_edx_extensions Django plugin.
"""

from setuptools import setup

from utils import get_version, load_requirements


with open("README.rst", "r") as fh:
    README = fh.read()

APP_NAME = "ocivu_edx_extensions = ocivu_edx_extensions.apps:OcivuEdxExtensionsConfig"

setup(
    name='ocivu_edx_extensions',
    version=get_version('ocivu_edx_extensions', '__init__.py'),
    author='Raccoon Gang',
    author_email='contact@raccoongang.com',
    description='Open Civil University Edx Extensions',
    license='AGPL',
    long_description=README,
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
    ],
    packages=[
        'ocivu_edx_extensions',
    ],
    include_package_data=True,
    install_requires=load_requirements('requirements/base.txt'),
    zip_safe=False,
    entry_points={"lms.djangoapp": [APP_NAME]},
)
