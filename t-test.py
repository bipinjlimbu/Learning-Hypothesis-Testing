import numpy as np
from scipy import stats
import random

population_mean = 25
sample = np.array(random.sample(range(1,50),10))
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)
sample_count = len(sample)

print(f"Sample Mean:{sample_mean}")
print(f"Sample Standard Deviation:{sample_std}")
print(f"Sample Count:{sample_count}")

t_value = (sample_mean - population_mean)/(sample_std/np.sqrt(sample_count))
print(f"T-Value:{t_value}")

p_value = 2 * (1 - stats.t.cdf(abs(t_value), df=sample_count-1))
print(f"P-Value:{p_value}")

significance_level = 0.05

if p_value < significance_level:
    print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis: The sample mean is not significantly different from the population mean.")