import pytest
from src import app,flag_behaviours
from src.flag import Flag
import sys
class TestClass:  
    help_flag = Flag(flag_behaviours.help_flag_fn,"help_flag",takes_argument=False)
    ascii_flag = Flag(flag_behaviours.ascii_flag_fn,"ascii_flag",takes_argument=True)
    result = ""
    def test_zero_arguments(self, capsys):
        help_description = """Usage: greeting [OPTION]... [ARG]

Print a greeting.

If ARG is provided, prints "greeting ARG".
If no ARG is given, desiplay --help text

Options:
  -h, --help              display this help and exit
  -a, --ascii string      displays the greeting in a cool way
"""
        with pytest.raises(SystemExit):
            app.parse_args(([], []))

        out = str(capsys.readouterr().out)
        assert help_description.strip() == out.strip()

