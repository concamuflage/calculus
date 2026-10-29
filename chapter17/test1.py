import matplotlib
matplotlib.use('TkAgg')   # interactive window

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


# =========================
# FUNCTIONS
# =========================

a, b = 0, 2
xx = np.linspace(a, b, 500)

f = lambda x: np.exp(-x**2)
g = lambda x: np.sin(x)/2 + 0.5


# =========================
# VOLUME
# =========================

volumeNum = np.pi * spi.simpson(
    np.abs(f(xx)**2 - g(xx)**2),
    x=xx
)

print('Volume =', volumeNum)


# =========================
# 2D PLOT
# =========================

fig1, ax1 = plt.subplots(figsize=(6, 5))

ax1.plot(
    xx,
    f(xx),
    'k',
    label=r'$f(x)=e^{-x^2}$'
)

ax1.plot(
    xx,
    g(xx),
    '--',
    color=[.7, .7, .7],
    label=r'$g(x)=\sin(x)/2+0.5$'
)

ax1.fill_between(
    xx,
    f(xx),
    g(xx),
    color='k',
    alpha=.2
)

ax1.set(
    xlabel='x',
    ylabel='y',
    xlim=(a, b),
    title='2D area to revolve'
)

ax1.legend()

fig1.tight_layout()


# =========================
# 3D COORDINATES
# =========================

theta = np.linspace(0, 2*np.pi, 120)

X, Theta = np.meshgrid(xx, theta)

# inner and outer radius at each x
r_inner = np.minimum(f(X), g(X))
r_outer = np.maximum(f(X), g(X))


# inner surface
Y_inner = r_inner * np.cos(Theta)
Z_inner = r_inner * np.sin(Theta)

# outer surface
Y_outer = r_outer * np.cos(Theta)
Z_outer = r_outer * np.sin(Theta)


# =========================
# INTERACTIVE 3D PLOT
# =========================

fig2 = plt.figure(figsize=(9, 7))

ax2 = fig2.add_subplot(
    111,
    projection='3d'
)


# -------------------------
# OUTER BOUNDARY
# -------------------------

ax2.plot_surface(
    X,
    Y_outer,
    Z_outer,
    color='0.35',
    alpha=.65,
    linewidth=0
)


# -------------------------
# INNER BOUNDARY
# very transparent
# -------------------------

ax2.plot_surface(
    X,
    Y_inner,
    Z_inner,
    color='0.85',
    alpha=.12,
    linewidth=0
)


# =========================
# ADD CROSS-SECTIONS
# =========================

# These washer-shaped slices make it obvious
# which part is solid and which part is empty.

slice_positions = np.linspace(a, b, 9)

for x0 in slice_positions:

    inner = min(f(x0), g(x0))
    outer = max(f(x0), g(x0))

    r = np.linspace(inner, outer, 25)
    theta_slice = np.linspace(0, 2*np.pi, 100)

    R, T = np.meshgrid(r, theta_slice)

    X_slice = np.full_like(R, x0)

    Y_slice = R * np.cos(T)
    Z_slice = R * np.sin(T)

    ax2.plot_surface(
        X_slice,
        Y_slice,
        Z_slice,
        color='0.55',
        alpha=.30,
        linewidth=0
    )


# =========================
# END CAPS
# =========================

for x0 in [a, b]:

    inner = min(f(x0), g(x0))
    outer = max(f(x0), g(x0))

    r = np.linspace(inner, outer, 40)
    theta_cap = np.linspace(0, 2*np.pi, 120)

    R, T = np.meshgrid(r, theta_cap)

    X_cap = np.full_like(R, x0)

    Y_cap = R * np.cos(T)
    Z_cap = R * np.sin(T)

    ax2.plot_surface(
        X_cap,
        Y_cap,
        Z_cap,
        color='0.25',
        alpha=.85,
        linewidth=0
    )


# =========================
# AXES
# =========================

ax2.set(
    xlabel='X',
    ylabel='Y',
    zlabel='Z',
    title=rf'Solid of revolution   $V \approx {volumeNum:.3f}$'
)

ax2.view_init(
    elev=25,
    azim=-60
)

fig2.tight_layout()


# =========================
# SHOW
# =========================

plt.show(block=True)