import numpy as np
import matplotlib.pyplot as plt

HARMONICS_COUNT = 6
MAX_FREQUENCY = 1700
DISCRETE_TIMES_COUNT = 1024

def rand_sig(harmonics_count, max_freq, discr_times_count):
	sig = np.zeros(discr_times_count)
	freq_start = max_freq / harmonics_count
	for harmonic_index in range(harmonics_count):
		amplitude = np.random.uniform(0.0, 1000.0)
		phase = np.random.uniform(-np.pi / 2, np.pi / 2)
		freq = freq_start * (harmonic_index + 1)
		for time in range(discr_times_count):
			sig[time] += amplitude * np.sin(freq * time + phase)
	return sig

def math_expectation(sig):
	sum = 0
	for i in range(len(sig)):
		sum += sig[i]
	return sum / len(sig)

def dispersion(sig):
	math_exp = math_expectation(sig)
	sum = 0
	for i in range(len(sig)):
		sum += (sig[i] - math_exp) ** 2
	return sum / (len(sig) - 1)

sig = rand_sig(HARMONICS_COUNT, MAX_FREQUENCY, DISCRETE_TIMES_COUNT)
M = math_expectation(sig)
D = dispersion(sig)

plt.plot(range(DISCRETE_TIMES_COUNT), sig)
plt.show()
print("Math expectation: ", M)
print("Dispersion: ", D)