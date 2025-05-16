from setuptools import setup, find_packages

setup(
    name='gramintel',
    version='1.0.0',
    author='upliftedl',
    description='Instagram OSINT metadata extractor (Toutatis fork)',
    packages=find_packages(),
    install_requires=['argparse'],
    entry_points={
        'console_scripts': [
            'gramintel=gramintel.core:main'
        ]
    },
    license='GPLv3',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ]
)
