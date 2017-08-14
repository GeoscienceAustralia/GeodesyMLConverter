"Setup.py for GeodesyML Converter"

#pylint: disable=line-too-long

from distutils.command.build import build
from subprocess import check_call
from setuptools import setup

class GenerateBindings(build):
    "Generate GeodesyML bindings."

    def run(self):
        check_call(['cd GeodesyMLToSiteLog && ./generate-bindings-for-geodesymltositelog.sh'], shell=True)
        check_call(['cd SiteLogToGeodesyML && ./generate-bindings-for-sitelogtogeodesyml.sh'], shell=True)
        build.run(self)

setup(
    name='geodesyml_converter',
    version='0.1',
    license='Creative Commons 4.0',
    packages=['GeodesyMLToSiteLog', 'SiteLogToGeodesyML'],
    cmdclass={
        'build': GenerateBindings,
    },
    entry_points={
        'console_scripts': [
            'geodesyml-to-sitelog=GeodesyMLToSiteLog.geodesymltositelog:main',
            'sitelog-to-geodesyml=SiteLogToGeodesyML.sitelogtogeodesyml:main',
            ],
    },
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'pytest-console-scripts'
    ],
    install_requires=[
        'iso3166',
        'pyxb',
    ],
)
