import pytest
from src import app,flag_behaviours
from src.flag_descriptions import help_description, ascii_description
class TestClass:  
  
    def test_zero_arguments(self, capsys):
      with pytest.raises(SystemExit):
        app.parse_args(([], []))

        out = str(capsys.readouterr().out)
        assert help_description.strip() == out.strip()

