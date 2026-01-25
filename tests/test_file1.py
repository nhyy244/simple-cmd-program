from unittest.mock import Mock, call
import pytest
import random
import art
from src import app,flag_behaviours
from src.app import flag_map
from src.flag_descriptions import help_description, ascii_description

@pytest.fixture(autouse=True)
def reset_flags(): # Reset mutable state on the shared Flag objects
    seen = set()
    for flag_obj in flag_map.values():
        if flag_obj in seen:
            continue
        seen.add(flag_obj)
        flag_obj.is_used = False
    yield

def test_zero_arguments(capsys):
  with pytest.raises(SystemExit):
    app.parse_args([], [])

  out = str(capsys.readouterr().out)
  assert help_description.strip() == out.strip()
    
def test_help_flag_zero_greetings(capsys):
  with pytest.raises(SystemExit):
      app.parse_args([], ["--help"])
  out = str(capsys.readouterr().out)
  assert help_description.strip() == out.strip()
  
  with pytest.raises(SystemExit):
      app.parse_args([], ["-h"])
  out = str(capsys.readouterr().out)
  assert help_description.strip() == out.strip()
  
  with pytest.raises(SystemExit):
      app.parse_args([], ["-h","--help"])
  out = str(capsys.readouterr().out)
  assert help_description.strip() == out.strip()
  
def test_ascii_flag_zero_greetings(capsys):
  with pytest.raises(SystemExit):
      app.parse_args([], ["--ascii"])
  out = str(capsys.readouterr().out)
  assert ascii_description.strip() == out.strip()
  
  with pytest.raises(SystemExit):
      app.parse_args([], ["-a"])
  out = str(capsys.readouterr().out)
  assert ascii_description.strip() == out.strip()
  
  with pytest.raises(SystemExit):
      app.parse_args([], ["-a","--ascii"])
  out = str(capsys.readouterr().out)
  assert ascii_description.strip() == out.strip()
        
def test_ascii_flag_with_help_flag_zero_greetings(capsys):
  with pytest.raises(SystemExit):
      app.parse_args([], ["--ascii","-h"])
  out = str(capsys.readouterr().out)
  assert ascii_description.strip() == out.strip()
  
  with pytest.raises(SystemExit):
      app.parse_args([], ["-a","-h"])
  out = str(capsys.readouterr().out)
  assert ascii_description.strip() == out.strip()
  
  with pytest.raises(SystemExit):
      app.parse_args([], ["-a","--ascii","-h"])
  out = str(capsys.readouterr().out)
  assert ascii_description.strip() == out.strip()
  
  with pytest.raises(SystemExit):        
      app.parse_args([], ["-a","--ascii","-h","--help"])
  out = str(capsys.readouterr().out)
  assert ascii_description.strip() == out.strip()
  
def test_deafult_behaviour(capsys):
  with pytest.raises(SystemExit):
    app.parse_args(["file_path","greeting"],[])
  out = str(capsys.readouterr().out)
  assert "hello greeting" == out.strip()
  
def test_deafult_behaviour_multiple_greetings(capsys):
  greetings = ["file_path","greeting1","greeting2","greeting3"]
  with pytest.raises(SystemExit):
    app.parse_args(greetings,[])
  out = str(capsys.readouterr().out).strip().split('\n')
  greetings.pop(0)
  for i, deafult_behaviour_res in enumerate(out):
    assert deafult_behaviour_res == f"hello {greetings[i]}"
    
def test_ascii_flag():
  greetings = ["file_path","greeting1"]
  mock_fn = Mock()
  flag_map['-a'].fn = mock_fn #-a and --ascii is the same object
  with pytest.raises(SystemExit):
    app.parse_args(greetings,["-a",])
  mock_fn.assert_called_once_with(greetings[1],None)

def test_ascii_flag2():
  greetings = ["file_path","greeting1"]
  mock_fn = Mock()
  flag_map['-a'].fn = mock_fn 
  with pytest.raises(SystemExit):
    app.parse_args(greetings,["-a","--ascii"])
  mock_fn.assert_called_once_with(greetings[1],None)

def test_ascii_flag_multiple_greetings():
  greetings = ["file_path","greeting1","greeting2","greeting3"]
  mock_fn = Mock()
  flag_map['-a'].fn = mock_fn
  with pytest.raises(SystemExit):
    app.parse_args(greetings,["-a","--ascii"])
  mock_fn.call_count = len(greetings[1:])
  mock_fn.assert_has_calls(
     [call("greeting1",None),call("greeting2",None),call("greeting3",None)],
     any_order=False)

def test_unknown_argument(capsys):
  with pytest.raises(SystemExit):
    app.parse_args([],["-zulul"])
  out = str(capsys.readouterr().out)
  assert out.strip() == "-zulul unknown. Use -h(--help) to see supported flags"
  
def test_unknown_argument2(capsys):
  with pytest.raises(SystemExit):
    app.parse_args(["file_path","greeting"],["-zulul"])
  out = str(capsys.readouterr().out)
  assert out.strip() == "-zulul unknown. Use -h(--help) to see supported flags"
  


    
    
      


