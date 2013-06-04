from setuptools import setup, find_packages

version = __import__('genjson').__version__

setup(
    name="django-generic-json-views",
    version=version,
    url='https://github.com/bbengfort/django-generic-json-views',
    license='Apache',
    description='Class based generic views that render JSON data.',
    long_description=open('README.md').read(),
    author='Benjamin Bengfort',
    author_email='benjamin@bengfort.com',
    maintainer='Benjamin Bengfort',
    maintainer_email='benjamin@bengfort.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
