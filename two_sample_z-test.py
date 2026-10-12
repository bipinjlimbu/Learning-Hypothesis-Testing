import numpy as np
from scipy.stats import norm
import random

group1 = np.array(random.sample(range(1, 100), 30))
group2 = np.array(random.sample(range(1, 100), 30))
mean1 = np.mean(group1)
mean2 = np.mean(group2)
population_std1 = np.std(group1, ddof=1)
population_std2 = np.std(group2, ddof=1)
len1 = len(group1)
len2 = len(group2)

z_score = (mean1 - mean2) / np.sqrt((population_std1**2 / len1) + (population_std2**2 / len2))
print(f"Z-Score: {z_score}")

p_value = 2 * (1 - norm.cdf(abs(z_score)))
print(f"P-Value: {p_value}")

significance_level = 0.05
print(f"Significance Level: {significance_level}")

if p_value < significance_level:
    print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis: The sample mean is not significantly different from the population mean.")