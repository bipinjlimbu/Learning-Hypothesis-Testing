import numpy as np
from scipy.stats import chi2_contingency
import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')
contingency_table = pd.crosstab(df['sex'], df['survived'])
print("Contingency Table:")
print(contingency_table)
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"\nChi-Square: {chi2}")
print(f"P-Value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print(f"\nExpected Frequencies: {expected}")

significance_level = 0.05
if p_value < significance_level:
    print("Reject the null hypothesis: There is a significant association between sex and survival.")
else:
    print("Fail to reject the null hypothesis: There is no significant association between sex and survival.")