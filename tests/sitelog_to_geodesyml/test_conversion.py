"""
Test text to GeodesyML site log conversion
"""

import os
import pytest

@pytest.mark.script_launch_mode('subprocess')
def test_sitelog_to_geodesyml(script_runner):
    """
    Convert all text site log files in tests/sitelog_to_geodesyml/input to GeodesyML
    and compare the generated ouput against the expected output in
    tests/sitelog_to_geodesyml/expected_ouput
    """

    input_sitelogs_dir = 'tests/sitelog_to_geodesyml/input/'
    generated_sitelogs_dir = 'tests/sitelog_to_geodesyml/generated_output/'
    expected_sitelogs_dir = 'tests/sitelog_to_geodesyml/expected_output/'

    if not os.path.exists(generated_sitelogs_dir):
        os.makedirs(generated_sitelogs_dir)

    for input_sitelog in os.walk(input_sitelogs_dir).next()[2]:

        geodesyml_sitelog_filename = os.path.splitext(input_sitelog)[0] + '.xml'
        generated_geodesyml_sitelog = generated_sitelogs_dir + geodesyml_sitelog_filename
        expected_geodesyml_sitelog = expected_sitelogs_dir + geodesyml_sitelog_filename

        return_status = script_runner.run(
            'sitelog-to-geodesyml',
            '-g', 'tests/logging.conf',
            '-l', input_sitelogs_dir + input_sitelog,
            '-x', generated_geodesyml_sitelog)

        print(return_status.stderr)
        assert return_status.success

        with open(generated_geodesyml_sitelog, 'r') as generated_sitelog:
            with open(expected_geodesyml_sitelog, 'r') as expected_sitelog:
                assert generated_sitelog.read() == expected_sitelog.read()
