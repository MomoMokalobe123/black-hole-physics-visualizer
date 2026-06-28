# physics.py

import numpy as np
from constants import G, c, M_sun


# convert solar masses to kg
def to_kg(mass_solar):
    return mass_solar * M_sun


# Schwarzschild radius
def schwarzschild_radius(mass_solar):
    M = to_kg(mass_solar)
    return (2 * G * M) / (c**2)


# escape velocity at distance r
def escape_velocity(mass_solar, r):
    M = to_kg(mass_solar)
    return np.sqrt((2 * G * M) / r)


# gravitational time dilation
def time_dilation(mass_solar, r):
    r_s = schwarzschild_radius(mass_solar)
    return np.sqrt(1 - r_s / r)