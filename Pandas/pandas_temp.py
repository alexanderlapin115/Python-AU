from scipy import stats
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("temperature.csv")

df.plot(kind='bar')
df.plot.kde()

vals = df['temperature']

print(stats.kstest(vals, 'norm', (vals.mean(), vals.std()), N=len(df)))
plt.show()
