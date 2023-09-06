import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Read the dataset (ISO-8859-1 encoding)
spotify_data = pd.read_csv('dataset/spotify-2023.csv', encoding='ISO-8859-1')

# Convert the "streams" column to numeric
spotify_data['streams'] = pd.to_numeric(spotify_data['streams'], errors='coerce')

# Generate the Q-Q plot
plt.figure(figsize=(10, 6))
res = stats.probplot(spotify_data['streams'], dist="norm", plot=plt)

# Add a 45-degree line that starts from the leftmost data point and ends at the rightmost data point
x_start, x_end = plt.xlim()
y_start, y_end = plt.ylim()

plt.plot([x_start, x_end], [y_start, y_end], 'r--', label='45-degree line')

plt.title("Q-Q Plot of Spotify Streams")
plt.xlabel("Theoretical Quantiles of Normal Distribution")
plt.ylabel("Ordered Spotify Stream Counts")
plt.legend()
plt.grid()
plt.show()
