import pytest
import pandas as pd

from io import StringIO
from traffic_counter import TrafficCounter


@pytest.fixture
def traffic_counter():
    """Fixture: TrafficCounter initialized with sample test data"""
    data = StringIO(
        "\n".join([
            "2021-12-01T00:00:00 10",
            "2021-12-01T00:30:00 20",
            "2021-12-01T01:00:00 5",
            "2021-12-01T01:30:00 15",
            "2021-12-02T00:00:00 7",
            "2021-12-02T00:30:00 8",
        ])
    )
    return TrafficCounter(data)


def test_total_traffic_count(traffic_counter):
    assert traffic_counter.total_traffic_count() == 65


def test_daily_traffic_count(traffic_counter):
    totals = traffic_counter.daily_traffic_count()
    assert totals.loc[pd.to_datetime("2021-12-01").date()] == 50
    assert totals.loc[pd.to_datetime("2021-12-02").date()] == 15


def test_top_half_hours(traffic_counter):
    top = traffic_counter.top_half_hours(3)
    assert list(top["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")) == [
        "2021-12-01T00:30:00",
        "2021-12-01T01:30:00",
        "2021-12-01T00:00:00"
    ]
    assert list(top["traffic_count"]) == [20, 15, 10]


def test_least_ninety_min_window(traffic_counter):
    min_sum, window = traffic_counter.least_ninety_min_window()
    assert len(window) == 3
    assert min_sum == 35  # 10 + 20 + 5
    assert list(window["timestamp"]) == [
        pd.to_datetime("2021-12-01T00:00:00"),
        pd.to_datetime("2021-12-01T00:30:00"),
        pd.to_datetime("2021-12-01T01:00:00")
    ]

