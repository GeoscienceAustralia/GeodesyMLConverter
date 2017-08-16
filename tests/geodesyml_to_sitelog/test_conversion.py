"""
Test GeodesyML to text site log conversion
"""

import os
import pytest

@pytest.mark.script_launch_mode('subprocess')
def test_geodesyml_to_sitelog(script_runner):
    """
    Convert all GeodesyML site log files in tests/geodesyml_to_sitelog/input to text
    and compare the generated ouput against the expected output in
    tests/geodesyml_to_sitelog/expected_ouput
    """

    input_sitelogs_dir = 'tests/geodesyml_to_sitelog/input/'
    generated_sitelogs_dir = 'tests/geodesyml_to_sitelog/generated_output/'
    expected_sitelogs_dir = 'tests/geodesyml_to_sitelog/expected_output/'

    if not os.path.exists(generated_sitelogs_dir):
        os.makedirs(generated_sitelogs_dir)

    for input_sitelog in os.walk(input_sitelogs_dir).next()[2]:

        text_sitelog_filename = os.path.splitext(input_sitelog)[0] + '.log'
        generated_text_sitelog = generated_sitelogs_dir + text_sitelog_filename
        expected_text_sitelog = expected_sitelogs_dir + text_sitelog_filename

        return_status = script_runner.run(
            'geodesyml-to-sitelog',
            '-x', input_sitelogs_dir + input_sitelog,
            '-l', generated_text_sitelog)

        print(return_status.stderr)
        assert return_status.success

        with open(generated_text_sitelog, 'r') as generated_sitelog:
            with open(expected_text_sitelog, 'r') as expected_sitelog:
                assert generated_sitelog.read() == expected_sitelog.read()
