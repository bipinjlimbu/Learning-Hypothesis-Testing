import seaborn as sns
import pandas as pd
from scipy.stats import f_oneway

df = sns.load_dataset('titanic')

class1 = df[df['pclass'] == 1]['age'].dropna()
class2 = df[df['pclass'] == 2]['age'].dropna()
class3 = df[df['pclass'] == 3]['age'].dropna()

f_statistic, p_value = f_oneway(class1, class2, class3)
print(f"F-Statistic: {f_statistic}")
print(f"P-Value: {p_value}")

significance_level = 0.05
if p_value < significance_level:
    print("Reject the null hypothesis: There is a significant difference in mean ages among the three passenger classes.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in mean ages among the three passenger classes.")