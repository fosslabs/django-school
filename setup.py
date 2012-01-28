import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read() 

setup(
    name = "django-school",
    version = "0.1",
    license = "BSD",
    description = "App for making learning courses.",
    long_description = read("README"),
    url = "https://github.com/fosslabs/django-school",
    author = "Azat Khasanshin, Radik Fattakhov",
    author_email = "azatkhasanshin@gmail.com",
    packages = find_packages("src"),
    package_dir = {"": "src"},
    install_requires = ["setuptools"],
    classifiers = [
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
