# coding=utf-8
import sys
sys.path.append('.')
import pytest
import dict


@pytest.fixture(scope="session")
def util():
    return dict
