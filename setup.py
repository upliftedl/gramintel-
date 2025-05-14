from setuptools import setup, find_packages

setup(
    name='gramintel',
    version='1.0.0',
    packages=find_packages(),
    author='upliftedl',
    description='Extract Instagram metadata using username or ID and a session ID.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['argparse', 'requests', 'phonenumbers', 'pycountry', 'colorama'],
    url='https://github.com/abhishekjohns/gramintel',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['gramintel = gramintel.core:main'],
    },
)