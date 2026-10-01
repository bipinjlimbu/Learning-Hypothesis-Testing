import numpy as np
from scipy.stats import norm
import random

sample = np.array(random.sample(range(1, 100), 30))
population_mean = 50
population_std = 15
sample_mean = np.mean(sample)
sample_count = len(sample)

print(f"Sample Mean: {sample_mean}")
print(f"Sample Count: {sample_count}")
print(f"Population Mean: {population_mean}")
print(f"Population Std: {population_std}")

z_score = (sample_mean - population_mean) / (population_std / np.sqrt(sample_count))
print(f"Z-Score: {z_score}")

p_value = 2 * (1 - norm.cdf(abs(z_score)))
print(f"P-Value: {p_value}")

significance_level = 0.05

if p_value < significance_level:
    print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis: The sample mean is not significantly different from the population mean.")