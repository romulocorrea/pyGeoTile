from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='pyGeoTile',
    version='0.1.0',
    description='Python package to handle tiles and points of the different projections, in particular WGS 84 '
                '(Latitude, Longitude), Spherical Mercator (Meters), Pixel Pyramid and Tiles (TMS, Google, QuadTree)',
    long_description=readme,
    author='Samuel Kurath',
    author_email='geometalab@hsr.ch',
    url='https://github.com/geometalab/pyGeoTile',
    license='',
    packages=find_packages(exclude=('tests', 'docs'))
)