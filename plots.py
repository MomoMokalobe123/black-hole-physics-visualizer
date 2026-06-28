import numpy as np
import matplotlib.pyplot as plt
from physics import escape_velocity, schwarzschild_radius, time_dilation

def plot_black_hole(mass_solar):

    r_s = schwarzschild_radius(mass_solar)

    r = np.linspace(1.05 * r_s, 10 * r_s, 600)

    v = escape_velocity(mass_solar, r)
    t = time_dilation(mass_solar, r)

    fig, ax = plt.subplots(2, 1, figsize=(8, 10))

    # ---------------- ESCAPE VELOCITY ----------------
    ax[0].plot(r, v)
    ax[0].axvline(r_s, linestyle="--")
    ax[0].axhline(3e8, linestyle="--")
    ax[0].axvspan(0, r_s, alpha=0.3, color="black")

    ax[0].set_title(f"Escape Velocity (Mass = {mass_solar} M☉)")
    ax[0].set_xlabel("Distance (m)")
    ax[0].set_ylabel("Velocity (m/s)")

    # ---------------- TIME DILATION ----------------
    ax[1].plot(r, t, color="purple")
    ax[1].axvline(r_s, linestyle="--")
    ax[1].axvspan(0, r_s, alpha=0.3, color="black")

    ax[1].set_title("Gravitational Time Dilation")
    ax[1].set_xlabel("Distance (m)")
    ax[1].set_ylabel("Time factor")

    plt.tight_layout()
    plt.show()