import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.plotting import autocorrelation_plot

# STEP 1: Data Preparation
date_range = pd.date_range(start='2020-01-01', periods=36, freq='M')
sales_data = np.random.normal(loc=200, scale=20, size=36) + np.linspace(0, 100, 36)
df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})
df.set_index('Date', inplace=True)

# STEP 2: Data Exploration
print("\nBasic Statistics:\n", df.describe())

# Line plot to observe trends
plt.figure(figsize=(10, 4))
plt.plot(df, label='Sales')
plt.title('Time Series Data - Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

# STEP 3: Decomposition
decomposition = seasonal_decompose(df['Sales'], model='additive', period=12)

# STEP 4: Visualization of Decomposed Components
fig, axes = plt.subplots(4, 1, figsize=(9,7), sharex=True, constrained_layout=True)

axes[0].plot(decomposition.observed, color='blue')
axes[0].set_title('Observed')
axes[0].grid(True)

axes[1].plot(decomposition.trend, color='orange')
axes[1].set_title('Trend')
axes[1].grid(True)

axes[2].plot(decomposition.seasonal, color='green')
axes[2].set_title('Seasonality')
axes[2].grid(True)

axes[3].plot(decomposition.resid, color='red')
axes[3].set_title('Residuals')
axes[3].grid(True)

plt.suptitle('Decomposition of Time Series', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Leave space for the main title
plt.show()

# STEP 5: Autocorrelation Plot
plt.figure(figsize=(8, 4))
autocorrelation_plot(df['Sales'])
plt.title('Autocorrelation Plot')
plt.grid(True)
plt.show()

# STEP 6: Rolling Statistics
rolling_mean = df['Sales'].rolling(window=6).mean()
rolling_std = df['Sales'].rolling(window=6).std()

plt.figure(figsize=(10, 5))
plt.plot(df['Sales'], label='Original Sales')
plt.plot(rolling_mean, label='Rolling Mean (6)', color='orange')
plt.plot(rolling_std, label='Rolling Std Dev (6)', color='green')
plt.title('Rolling Mean and Standard Deviation')
plt.legend()
plt.grid(True)
plt.show()

# STEP 7: Interpretation
print("\nInterpretation:")
print("The graphs show trends, seasonality, and the variability over time.")
print("Autocorrelation indicates how current values relate to past values.")