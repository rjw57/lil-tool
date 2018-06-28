from setuptools import setup, find_packages

setup(
    name='liltool',
    packages=find_packages(),
    install_requires=[
        'docopt',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'lil=liltool.cli:main',
        ],
    },
)
