from scipy import stats
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("mass.csv")

df.plot(kind='bar')
df.plot.kde()

vals = df['values']

print(stats.kstest(vals, 'norm', (vals.mean(), vals.std()), N=len(df)))
plt.show()
