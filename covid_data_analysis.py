import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dataset = pd.read_csv('/content/country_wise_latest.csv')

"""**All the figures represent weekly data**"""

dataset.head()

dataset.keys()

len(dataset['Country/Region'])

# To check is dataset has any missing values
dataset.isnull().values.any()

"""**Which region has seen the most deaths?**"""

# WHO region wise death
plt.figure(figsize=(15,8))
sns.set_theme(style="whitegrid")
hue="Active"
ax = sns.barplot(x="WHO Region", y="Deaths", capsize=.2, data=dataset)

"""**The Americas seems to be affected the most with 20k+ deaths at the peak while the average hovers around 10k**

===================================================================================================================

**Which region is the most active?**
"""

plt.figure(figsize=(15,8))
sns.set_theme(style="whitegrid")
hue="Active"
ax = sns.barplot(x="WHO Region", y="Active", capsize=.2, data=dataset)

plt.figure(figsize=(35,10))
sns.set_theme(style="whitegrid")
ax = sns.barplot(x='Country/Region', y="Active", capsize=.2, data=dataset[dataset['WHO Region']=='Americas'])

