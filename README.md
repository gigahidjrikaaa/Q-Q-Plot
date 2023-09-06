# Q-Q Plot for Most Streamed Spotify Songs 2023

This is a Q-Q plot for Most Streamed Spotify Songs 2023. The data is from [Kaggle](https://www.kaggle.com/code/rajatraj0502/most-streamed-spotify-songs-2023). 

## Insights

- Exponential Distribution: The data points align more closely with the 45-degree line when compared with an exponential distribution. This suggests that the "streams" data may follow an exponential distribution, which is often seen in "winner-takes-all" scenarios. Most songs have fewer streams, while a few have significantly more.

- Normal Distribution: The data deviates significantly from the normal distribution, especially at the tails. This was also supported by the skewness calculation. (Calculations are coming soon, I haven't had time to do them yet. Currently, it's just a quick deduction. Will also come with Descriptive Statistics.)

- Log-Normal and Gamma Distributions: The data points also deviate from the log-normal and gamma distributions, making them less suitable for modeling this specific dataset.

## Strategic Implications

The fit with an exponential distribution could imply that only a few tracks will receive the majority of streams. This has implications for both artists and platforms like Spotify. For artists, focusing on creating a few hit tracks could be more beneficial. For platforms, there may be a need to adjust recommendation algorithms to provide visibility to less popular tracks.
