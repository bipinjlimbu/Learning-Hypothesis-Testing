import numpy as np
from scipy import stats

group1 = np.array([12, 15, 14, 10, 13])
group2 = np.array([22, 25, 24, 20, 23])

t_statistic, p_value = stats.ttest_ind(group1, group2, equal_var=False)
print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")

significance_level = 0.05

if p_value < significance_level:
    print("Reject the null hypothesis: The means of the two groups are significantly different.")
else:
    print("Fail to reject the null hypothesis: The means of the two groups are not significantly different.")