import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Read the dataset (assuming ISO-8859-1 encoding)
spotify_data = pd.read_csv('dataset/spotify-2023.csv', encoding='ISO-8859-1')

# Convert the "streams" column to numeric (if needed)
spotify_data['streams'] = pd.to_numeric(spotify_data['streams'], errors='coerce')

# Generate Q-Q plots for different distributions with shape parameters if needed
distributions = {
    'norm': {},
    'expon': {},
    'lognorm': {'s': 0.954},
    'gamma': {'a': 1.99}
}

plt.figure(figsize=(15, 10))

for i, (dist, params) in enumerate(distributions.items()):
    plt.subplot(2, 2, i+1)
    stats.probplot(spotify_data['streams'], dist=dist, sparams=params.values(), plot=plt)
    
    # Add a 45-degree line to show the correctness of the distribution
    x_start, x_end = plt.xlim()
    y_start, y_end = plt.ylim()
    plt.plot([x_start, x_end], [y_start, y_end], 'r--', label='45-degree line')
    
    plt.title(f"Q-Q Plot of Spotify Streams with {dist.capitalize()} Distribution")
    plt.xlabel(f"Theoretical Quantiles of {dist.capitalize()} Distribution")
    plt.ylabel("Ordered Spotify Stream Counts")
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.show()
