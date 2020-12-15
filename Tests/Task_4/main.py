from ohe import fit_transform
import pytest


def test_ft():
    cities = ["Moscow", "New York", "Moscow", "London"]
    exp_transformed_cities = [
        ("Moscow", [0, 0, 1]),
        ("New York", [0, 1, 0]),
        ("Moscow", [0, 0, 1]),
        ("London", [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_ft_empty():
    assert fit_transform([]) == []


def test_subject():
    subject = ["Python", "Statistic", "SQL", "SQL", "ML", "Python"]
    exp_transformed_subject = [
        ("Python", [0, 0, 0, 1]),
        ("Statistic", [0, 0, 1, 0]),
        ("SQL", [0, 1, 0, 0]),
        ("SQL", [0, 1, 0, 0]),
        ("ML", [1, 0, 0, 0]),
        ("Python", [0, 0, 0, 1]),
    ]
    assert fit_transform(subject) == exp_transformed_subject
