import numpy as np
import matplotlib.pyplot as plt
from time import time

HARMONICS_COUNT = 6
MAX_FREQUENCY = 1700
DISCRETE_TIMES_COUNT = 1024

def rand_sig_arrays(harmonics_count, max_freq, discr_times_count):
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

sig = rand_sig_arrays(HARMONICS_COUNT, MAX_FREQUENCY, DISCRETE_TIMES_COUNT)
M = math_expectation(sig)
D = dispersion(sig)

plt.plot(range(DISCRETE_TIMES_COUNT), sig)
plt.show()
print("Math expectation: ", M)
print("Dispersion: ", D)

def rand_sig_sets(harmonics_count, max_freq, discr_times_count):
	sig = set()
	freq_start = max_freq / harmonics_count
	for harmonic_index in range(harmonics_count):
		sig_point = 0
		amplitude = np.random.uniform(0.0, 1000.0)
		phase = np.random.uniform(-np.pi / 2, np.pi / 2)
		freq = freq_start * (harmonic_index + 1)
		for time in range(discr_times_count):
			sig_point += amplitude * np.sin(freq * time + phase)
		sig.add(sig_point)
	return sig

sig_gen_durations_arrays = np.zeros(DISCRETE_TIMES_COUNT)
sig_gen_durations_sets = np.zeros(DISCRETE_TIMES_COUNT)

for discr_times_count in range(DISCRETE_TIMES_COUNT):
	before = time()
	array_sig = rand_sig_arrays(HARMONICS_COUNT, MAX_FREQUENCY, discr_times_count)
	after = time()
	sig_gen_durations_arrays[discr_times_count] = after - before
	before = time()
	set_sig = rand_sig_sets(HARMONICS_COUNT, MAX_FREQUENCY, discr_times_count)
	after = time()
	sig_gen_durations_sets[discr_times_count] = after - before

plt.plot(range(DISCRETE_TIMES_COUNT), sig_gen_durations_arrays, label = "array signal gen time")
plt.plot(range(DISCRETE_TIMES_COUNT), sig_gen_durations_sets, label = "set signal gen time")
plt.legend()
plt.xlabel("Discrete times count")
plt.ylabel("Duration")
plt.show()
