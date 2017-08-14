"""
Test GeodesyML converter console scripts.

We run each test in a subprocess, so pyxb wouldn't see the conflicting
GeodesyML bindings for sitelog-to-geodesyml and geodesyml-to-sitelog.
"""

import pytest

@pytest.mark.script_launch_mode('subprocess')
def test_sitelog_to_geodesyml(script_runner):
    """
    Test sitelog_to_geodesyml console script.
    """

    return_status = script_runner.run(
        'sitelog-to-geodesyml',
        '-g', 'tests/logging.conf',
        '-l', 'tests/text_site_logs/alic_20170223.log')

    print(return_status.stdout)
    print(return_status.stderr)
    assert return_status.success

@pytest.mark.script_launch_mode('subprocess')
def test_geodesyml_to_sitelog(script_runner):
    """
    Test geodesyml-to-sitelog console script.
    """

    return_status = script_runner.run(
        'geodesyml-to-sitelog',
        '-x', 'tests/xml_site_logs/alic_20170223.xml')

    print(return_status.stdout)
    print(return_status.stderr)
    assert return_status.success
    assert return_status.stdout == '\n\tSite log file "alic_20170223.log" has been successfully generated\n'
    assert return_status.stderr == ''
