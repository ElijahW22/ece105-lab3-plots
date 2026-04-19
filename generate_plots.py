"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np


def generate_data(seed):
    """Generate synthetic sensor temperature data and timestamps.

    Parameters
    ----------
    seed : int
        Seed used to initialize ``np.random.default_rng`` for reproducible
        sensor data generation.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of shape ``(200,)`` containing Sensor A temperatures in degrees
        Celsius, sampled from a normal distribution with mean 25 and standard
        deviation 3.
    sensor_b : numpy.ndarray
        Array of shape ``(200,)`` containing Sensor B temperatures in degrees
        Celsius, sampled from a normal distribution with mean 27 and standard
        deviation 4.5.
    timestamps : numpy.ndarray
        Array of shape ``(200,)`` containing uniformly spaced timestamps from
        0 to 10 seconds (inclusive).
    """
    rng = np.random.default_rng(seed)
    n_readings = 200

    timestamps = np.linspace(0, 10, n_readings)
    sensor_a = rng.normal(loc=25, scale=3, size=n_readings)
    sensor_b = rng.normal(loc=27, scale=4.5, size=n_readings)

    return sensor_a, sensor_b, timestamps
