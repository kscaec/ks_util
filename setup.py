from setuptools import setup

setup(
    name='ks_util',
    version='1.1.0',
    packages=['ks_util'],
    author='kscaec',
    author_email='kris@pt.lu',
    description='A collection of utility functions',
    long_description=open('README.md').read(),
    url='https://github.com/kscaec/ks_util',
    license='MIT',
    install_requires=['icecream>=2.1.4'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)