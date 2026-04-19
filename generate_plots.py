"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.
import numpy as np
import matplotlib.pyplot as plt


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

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot Sensor A and Sensor B temperatures against time on an Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings in degrees Celsius.
    sensor_b : numpy.ndarray
        Sensor B temperature readings in degrees Celsius.
    timestamps : numpy.ndarray
        Time values in seconds for each reading.
    ax : matplotlib.axes.Axes
        Existing Matplotlib Axes object to modify in place.

    Returns
    -------
    None
        This function modifies ``ax`` directly and does not return a value.
    """
    ax.scatter(timestamps, sensor_a, alpha=0.7, s=25, label="Sensor A")
    ax.scatter(timestamps, sensor_b, alpha=0.7, s=25, label="Sensor B")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (C)")
    ax.set_title("Sensor Readings vs Time")
    ax.legend()
    return None

# Create plot_histogram(sensor_a, sensor_b, ax) that draws the overlaid
# histogram from the notebook onto the given Axes object.
# Use 30 bins, transparency, and vertical dashed mean lines.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid Sensor A and Sensor B histograms on an Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings in degrees Celsius.
    sensor_b : numpy.ndarray
        Sensor B temperature readings in degrees Celsius.
    ax : matplotlib.axes.Axes
        Existing Matplotlib Axes object to modify in place.

    Returns
    -------
    None
        This function modifies ``ax`` directly and does not return a value.
    """
    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)

    ax.hist(sensor_a, bins=30, alpha=0.5, label="Sensor A")
    ax.hist(sensor_b, bins=30, alpha=0.5, label="Sensor B")
    ax.axvline(mean_a, linestyle="--", linewidth=2, label="Sensor A Mean")
    ax.axvline(mean_b, linestyle="--", linewidth=2, label="Sensor B Mean")
    ax.set_xlabel("Temperature (C)")
    ax.set_ylabel("Count")
    ax.set_title("Temperature Distribution: Sensor A vs Sensor B")
    ax.legend()
    return None


def plot_boxplot(sensor_a, sensor_b, ax):
    """Plot side-by-side Sensor A and Sensor B box plots on an Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings in degrees Celsius.
    sensor_b : numpy.ndarray
        Sensor B temperature readings in degrees Celsius.
    ax : matplotlib.axes.Axes
        Existing Matplotlib Axes object to modify in place.

    Returns
    -------
    None
        This function modifies ``ax`` directly and does not return a value.
    """
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))

    ax.boxplot([sensor_a, sensor_b], labels=["Sensor A", "Sensor B"])
    ax.axhline(overall_mean, linestyle="--", linewidth=2, label="Overall Mean")
    ax.set_xlabel("Sensor")
    ax.set_ylabel("Temperature (deg C)")
    ax.set_title("Sensor Temperature Distributions (Box Plot)")
    ax.legend()
    return None

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.


def main():
    """Generate sensor data, create plots, and save a combined figure.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Saves ``sensor_analysis.png`` and does not return a value.
    """
    sensor_a, sensor_b, timestamps = generate_data(seed=1234)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])

    fig.tight_layout()
    fig.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
