import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
                   [6.4, 3.2, 1], [5.9, 3.0, 2]],
                  columns=['length', 'width', 'species'])
print(df)

df.plot.scatter(x='length',y='width')
df.plot.scatter(x='length',y='width',c='DarkBlue')
df.plot.scatter(x='length',y='width',color='y')
plt.show()




# import seaborn as sns
# sns.scatterplot(x='length',y='width',hue='species',data=df)
# plt.show()

# specific color=palette
# sns.scatterplot(x='length',y='width',hue='species',data=df,palette=['green','orange','brown'])
# plt.show()



