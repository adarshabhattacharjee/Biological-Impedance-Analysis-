import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


frequencies = np.logspace(2, 6, 200)
omega = 2 * np.pi * frequencies

Rs_true = 100
Rm_true = 800
Cm_true = 1.2e-6


def impedance_model(f, Rs, Rm, Cm):
    omega = 2 * np.pi * f
    Z_parallel = 1 / (1/Rm + 1j * omega * Cm)
    Z_total = Rs + Z_parallel
    return Z_total


Z_true = impedance_model(frequencies, Rs_true, Rm_true, Cm_true)

noise_level = 5
Z_noisy = Z_true + noise_level * (np.random.randn(len(Z_true)) +
                                   1j*np.random.randn(len(Z_true)))


def fitting_function(f, Rs, Rm, Cm):
    Z = impedance_model(f, Rs, Rm, Cm)
    return np.concatenate([Z.real, Z.imag])


Z_data = np.concatenate([Z_noisy.real, Z_noisy.imag])

initial_guess = [120, 1000, 1e-6]

params, covariance = curve_fit(fitting_function,
                                frequencies,
                                Z_data,
                                p0=initial_guess)

Rs_est, Rm_est, Cm_est = params

print("True Parameters:")
print("Rs =", Rs_true)
print("Rm =", Rm_true)
print("Cm =", Cm_true)

print("\nEstimated Parameters:")
print("Rs =", Rs_est)
print("Rm =", Rm_est)
print("Cm =", Cm_est)

Z_fitted = impedance_model(frequencies, Rs_est, Rm_est, Cm_est)

plt.figure(figsize=(6,6))
plt.plot(Z_noisy.real, -Z_noisy.imag, '.', label="Noisy Data")
plt.plot(Z_fitted.real, -Z_fitted.imag, 'r', label="Fitted Model")
plt.xlabel("Real(Z)")
plt.ylabel("-Imag(Z)")
plt.title("Nyquist Plot: Data vs Fitted Model")
plt.legend()
plt.grid(True)
plt.show()