import pytest,random
from src import app,flag_behaviours
from src.flag_descriptions import help_description, ascii_description
class TestClass:  
    random.seed(5) #for ascii tests
    def test_zero_arguments(self, capsys):
      with pytest.raises(SystemExit):
        app.parse_args(([], []))

      out = str(capsys.readouterr().out)
      assert help_description.strip() == out.strip()
        
    def test_help_flag_zero_greetings(self, capsys):
      with pytest.raises(SystemExit):
          app.parse_args(([], ["--help"]))
      out = str(capsys.readouterr().out)
      assert help_description.strip() == out.strip()
      
      with pytest.raises(SystemExit):
          app.parse_args(([], ["-h"]))
      out = str(capsys.readouterr().out)
      assert help_description.strip() == out.strip()
      
      with pytest.raises(SystemExit):
          app.parse_args(([], ["-h","--help"]))
      out = str(capsys.readouterr().out)
      assert help_description.strip() == out.strip()
      
    def test_ascii_flag_zero_greetings(self, capsys):
      with pytest.raises(SystemExit):
          app.parse_args(([], ["--ascii"]))
      out = str(capsys.readouterr().out)
      assert ascii_description.strip() == out.strip()
      
      with pytest.raises(SystemExit):
          app.parse_args(([], ["-a"]))
      out = str(capsys.readouterr().out)
      assert ascii_description.strip() == out.strip()
      
      with pytest.raises(SystemExit):
          app.parse_args(([], ["-a","--ascii"]))
      out = str(capsys.readouterr().out)
      assert ascii_description.strip() == out.strip()
            
    def test_ascii_flag_with_help_flag_zero_greetings(self, capsys):
      with pytest.raises(SystemExit):
          app.parse_args(([], ["--ascii","-h"]))
      out = str(capsys.readouterr().out)
      assert ascii_description.strip() == out.strip()
      
      with pytest.raises(SystemExit):
          app.parse_args(([], ["-a","-h"]))
      out = str(capsys.readouterr().out)
      assert ascii_description.strip() == out.strip()
      
      with pytest.raises(SystemExit):
          app.parse_args(([], ["-a","--ascii","-h"]))
      out = str(capsys.readouterr().out)
      assert ascii_description.strip() == out.strip()
      
      with pytest.raises(SystemExit):        
          app.parse_args(([], ["-a","--ascii","-h","--help"]))
      out = str(capsys.readouterr().out)
      assert ascii_description.strip() == out.strip()
      
    def test_deafult_behaviour(self,capsys):
      with pytest.raises(SystemExit):
        app.parse_args((["file_path","greeting"],[]))
      out = str(capsys.readouterr().out)
      assert "hello greeting" == out.strip()
      


