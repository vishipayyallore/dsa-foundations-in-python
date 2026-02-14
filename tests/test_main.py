"""Tests for src.main entry point."""

import pytest

from src.main import main


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    """main() prints the project greeting to stdout."""
    main()
    captured = capsys.readouterr()
    assert "dsa-foundations-in-python" in captured.out
    assert "Hello" in captured.out
