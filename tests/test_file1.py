import pytest
import random
import art
from src import app,flag_behaviours
from src.flag_descriptions import help_description, ascii_description
class TestClass:  
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
      
    def test_deafult_behaviour_multiple_greetings(self,capsys):
      greetings = ["file_path","greeting1","greeting2","greeting3"]
      with pytest.raises(SystemExit):
        app.parse_args((greetings,[]))
      out = str(capsys.readouterr().out).strip().split('\n')
      greetings.pop(0)
      for i, deafult_behaviour_res in enumerate(out):
        assert deafult_behaviour_res == f"hello {greetings[i]}"
        
    def test_ascii_flag(self,capsys):# TODO mock randomness or do not test for randomness at all. will have problems with seed for multiple ascii greetings
      greetings = ["file_path","greeting1"]
      with pytest.raises(SystemExit):
        random.seed(5) #for ascii tests
        app.parse_args((greetings,["-a"]))
      out = str(capsys.readouterr().out)
      random.seed(5) #for ascii tests
      expected_res = art.text2art(f"hello {greetings[1]}", font='random')  
      assert expected_res.strip() == out.strip()
    
      


