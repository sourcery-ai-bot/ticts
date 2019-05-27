from datetime import timedelta

import pytest

from ticts import TimeSeries
from ticts.pandas_ext import timestamp_converter

CURRENT = timestamp_converter('2019-01-01')
ONEHOUR = timedelta(hours=1)
HALFHOUR = timedelta(minutes=30)
ONEMIN = timedelta(minutes=1)


@pytest.fixture
def smalldict():
    dct = dict()
    for i in range(10):
        dct[CURRENT + i * ONEHOUR] = i
    return dct


@pytest.fixture
def smallts(smalldict):
    return TimeSeries(smalldict)


@pytest.fixture
def smallts_withdefault(smalldict):
    return TimeSeries(smalldict, default=10)


@pytest.fixture
def otherict():
    return {
        CURRENT + 2 * ONEHOUR: 1000,
        CURRENT + 2 * ONEHOUR + 30 * ONEMIN: 2000,
        CURRENT + 4 * ONEHOUR: 3000,
    }


@pytest.fixture
def conditionalts():
    dct = {
        CURRENT + 2 * ONEHOUR: True,
        CURRENT + 3 * ONEHOUR: False,
    }
    return TimeSeries(dct, default=True)


@pytest.fixture
def otherts(otherict):
    return TimeSeries(otherict)


@pytest.fixture
def otherts_withdefault(otherict):
    return TimeSeries(otherict, default=900)


@pytest.fixture
def emptyts():
    return TimeSeries()


@pytest.fixture
def emptyts_withdefault():
    return TimeSeries(default=10)
