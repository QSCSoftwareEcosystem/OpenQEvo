"""Tests for recommendation execution helpers."""

import numpy as np
import pytest
from scipy.linalg import expm

import openqevo


def test_execute_recommendation_runs_exact_method():
    term = np.array([[1, 0], [0, -1]], dtype=complex)

    result = openqevo.execute_recommendation(
        {"method_name": "exact"},
        terms=[term],
        t=0.25,
    )

    np.testing.assert_allclose(result, expm(-1j * term * 0.25))


def test_execute_recommendation_accepts_embedded_terms_and_time():
    term = np.array([[1, 0], [0, -1]], dtype=complex)

    result = openqevo.execute_recommendation(
        {
            "method_name": "exact",
            "terms": [term],
            "t": 0.25,
        }
    )

    np.testing.assert_allclose(result, expm(-1j * term * 0.25))


def test_execute_recommendation_uses_recommendation_parameters():
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)

    result = openqevo.execute_recommendation(
        {"method_name": "trotter_s1", "parameters": {"steps": 4}},
        terms=[x, z],
        t=0.5,
    )

    assert result.shape == (2, 2)


def test_execute_recommendation_allows_parameter_overrides():
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)

    result = openqevo.execute_recommendation(
        {"method": "trotter_s2", "parameters": {"steps": 1}},
        terms=[x, z],
        t=0.5,
        steps=2,
    )

    assert result.shape == (2, 2)


def test_execute_recommendation_rejects_non_executable_context_method():
    with pytest.raises(NotImplementedError, match="No registered OpenQEvo method"):
        openqevo.execute_recommendation(
            {"method_name": "mitiq_zne"},
            terms=[],
            t=1.0,
        )


def test_execute_recommendation_rejects_mismatched_execution_method():
    with pytest.raises(ValueError, match="execution.method_name"):
        openqevo.execute_recommendation(
            {
                "method_name": "exact",
                "execution": {
                    "implemented": True,
                    "method_name": "trotter_s1",
                },
            },
            terms=[],
            t=1.0,
        )


def test_execute_recommendation_requires_terms_t_and_required_parameters():
    term = np.eye(2, dtype=complex)

    with pytest.raises(ValueError, match="'terms' is required"):
        openqevo.execute_recommendation({"method_name": "exact"}, t=1.0)

    with pytest.raises(ValueError, match="'t' is required"):
        openqevo.execute_recommendation({"method_name": "exact"}, terms=[term])

    with pytest.raises(ValueError, match="steps"):
        openqevo.execute_recommendation(
            {"method_name": "trotter_s1"},
            terms=[term],
            t=1.0,
        )
