from setuptools import setup, find_packages

setup(
    name="emmentalembed",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'biopython',
    ]
)