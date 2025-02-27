import pytest
from project import (
    calculate_profit_margin, 
    calculate_break_even_point, 
    apply_discount, 
    calculate_tax,
    suggest_retail_price,
    project_annual_revenue,
    analyze_sales_trends
)


def test_calculate_profit_margin():
    assert calculate_profit_margin(50, 100) == 50.0
    assert calculate_profit_margin(30, 90) == 66.66666666666666
    with pytest.raises(ValueError):
        calculate_profit_margin(0, 100)
    with pytest.raises(ValueError):
        calculate_profit_margin(50, 0)


def test_calculate_break_even_point():
    assert calculate_break_even_point(1000, 100, 30) == 14.285714285714286
    with pytest.raises(ValueError):
        calculate_break_even_point(1000, 30, 30)


def test_apply_discount():
    assert apply_discount(100, 10) == 90.0
    assert apply_discount(200, 25) == 150.0
    with pytest.raises(ValueError):
        apply_discount(100, -5)
    with pytest.raises(ValueError):
        apply_discount(100, 105)


def test_calculate_tax():
    assert calculate_tax(100, 10) == 110.0
    assert calculate_tax(200, 5) == 210.0
    with pytest.raises(ValueError):
        calculate_tax(100, -5)


def test_suggest_retail_price():
    assert suggest_retail_price(50, 20) == 60.0
    assert suggest_retail_price(100, 50) == 150.0
    with pytest.raises(ValueError):
        suggest_retail_price(50, -10)


def test_project_annual_revenue():
    assert project_annual_revenue(5000) == 60000
    assert project_annual_revenue(10000) == 120000


def test_analyze_sales_trends():
    assert analyze_sales_trends([3000, 4000, 2500, 5000]) == (5000, 2500)
    with pytest.raises(ValueError):
        analyze_sales_trends([])
