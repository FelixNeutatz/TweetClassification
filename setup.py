# -*- coding: utf-8 -*-

from setuptools import setup, find_packages




with open('LICENSE') as f:
    license = f.read()

setup(
    name='tweetclassification',
    version='0.0.1',
    description='TweetClassification',
    long_description='description',
    author='Felix Neutatz',
    author_email='neutatz@gmail.com',
    url='https://github.com/FelixNeutatz/TweetClassification',
    license=license,
    include_package_data=True,
    install_requires=["pandas",
                      "flair",
                      "autogluon.multimodal"
                      ],
    packages=find_packages(exclude=('tests', 'docs'))
)

