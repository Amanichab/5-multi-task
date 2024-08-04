import numpy as np
import torch


def set_seeds(seed: int = 42):
    """Set random seeds for reproducibility."""
    np.random.seed(seed)
    torch.manual_seed(seed)


def gauss(x, mean, std):
    return np.exp(-(((x - mean) / std) ** 2))


def measure_uniformity_A(T: float, P: float, F: float) -> tuple:
    """
    Synthetic objectiv function for measuring the uniformity of a component produced
    with CVD on Device A.

    Parameters:
    -----------
    T : float
        Process temperature in °C (600-1100).
    P : float
        Process pressure in Torr (5-300).
    F : float
        Total gas flow rate in sccm (10-700).

    Returns:
    --------
    tuple
        (percent uniformity, measurement error)
    """

    u = (
        gauss(T, 700, 350)
        + gauss(T, 850, 75)
        + gauss(T, 1100, 400)
        + gauss(P, 270, 200)
        + gauss(P, 65, 25)
        + gauss(P, 10, 200)
    )

    u *= gauss(F, 206, 400) + 0.1
    u /= 5.5

    return u, np.random.uniform(0, 0.01, size=u.shape)


def measure_uniformity_B(T, P, F):
    """
    Synthetic objectiv function for measuring the uniformity of a component produced
    with CVD on Device B.

    Parameters:
    -----------
    T : float
        Process temperature in °C (600-1100).
    P : float
        Process pressure in Torr (5-300).
    F : float
        Total gas flow rate in sccm (10-700).

    Returns:
    --------
    tuple
        (percent uniformity, measurement error)
    """
    u = (
        gauss(T, 710, 300)
        + gauss(T, 900, 76)
        + gauss(T, 1000, 400)
        + gauss(P, 250, 200)
        + gauss(P, 90, 20)
        + gauss(P, 12, 100)
    )

    u *= gauss(F, 250, 400) + 0.1
    u /= 5.5

    return u, np.random.uniform(0, 0.01, size=u.shape)


def measure_uniformity_C(T, P, F):
    """
    Synthetic objectiv function for measuring the uniformity of a component produced
    with CVD on Device C.

    Parameters:
    -----------
    T : float
        Process temperature in °C (600-1100).
    P : float
        Process pressure in Torr (5-300).
    F : float
        Total gas flow rate in sccm (10-700).

    Returns:
    --------
    tuple
        (percent uniformity, measurement error)
    """
    u = (
        gauss(T, 710, 400)
        + gauss(T, 876, 50)
        + gauss(T, 1000, 400)
        + gauss(P, 250, 400)
        + gauss(P, 70, 30)
        + gauss(P, 12, 400)
    )

    u *= gauss(F, 230, 400) + 0.1
    u /= 5.5

    return u, np.random.uniform(0, 0.01, size=u.shape)
