from __future__ import absolute_import, print_function

from ..pyautoupdate.launcher import Launcher
from .pytest_skipif import needinternet
from .pytest_makevers import fixture_update_dir

import os
import sys

import pytest

@needinternet
def test_check_get_new(fixture_update_dir):
    """Test that gets new version from internet"""
    package=fixture_update_dir("0.0.1")
    launch = Launcher('filling up the boring replacements',
                      r'http://rlee287.github.io/pyautoupdate/testing/')
    launch._get_new()
    with open(os.path.abspath("downloads/extradir/blah.py"), "r") as file_code:
        file_text=file_code.read()
    assert "new version" in file_text

@needinternet
def test_check_get_invalid_archive(fixture_update_dir):
    """Test that gets new version from internet"""
    package=fixture_update_dir("0.0.1")
    launch = Launcher('what file? hahahaha',
                      r'http://rlee287.github.io/pyautoupdate/testing2/',
                      newfiles="project.tar.gz")
    launch._get_new()
    assert os.path.isfile("project.tar.gz.dump")
    os.remove("project.tar.gz.dump")
