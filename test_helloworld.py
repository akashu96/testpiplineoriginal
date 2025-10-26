import sys
from io import StringIO
import pytest

def test_output(capsys):
    """Test that the script prints the expected output"""
    import helloworld
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\nThis is a simple Python script.\n"

def test_script_runs():
    """Test that the script runs without errors"""
    try:
        import helloworld
        assert True
    except Exception as e:
        pytest.fail(f"Script raised an exception: {e}")