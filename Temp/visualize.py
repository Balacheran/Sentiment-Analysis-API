import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Load the dataset
vad = pd.read_csv('vaders_with_sentiment.csv')

# Plot the count of reviews by score
ax1 = (vad['Score'].value_counts().sort_index()
       .plot(kind='bar',
             title='Count of Reviews by Stars',
             figsize=(5, 5)))
ax1.set_xlabel('Review Star')
plt.show()

# Sentiment distribution plot
w = vad['Sentiment'].value_counts()

# Corrected plotting using subplots
fig, ax2 = plt.subplots(figsize=(5, 5))
ax2.bar(w.index, w.values)
ax2.set_title('Sentiment Distribution')
ax2.set_xlabel('Sentiment Value')
plt.show()

# Compound score plot
fig, ax3 = plt.subplots(figsize=(5, 5))
sns.barplot(data=vad, x='Score', y='compound', ax=ax3)
ax3.set_title('Compound Score by Amazon Star Reviews')
plt.show()

# Multiple subplots for pos, neu, and neg
fig, axs = plt.subplots(1, 3, figsize=(12, 3))
sns.barplot(data=vad, x='Score', y='pos', ax=axs[0])
sns.barplot(data=vad, x='Score', y='neu', ax=axs[1])
sns.barplot(data=vad, x='Score', y='neg', ax=axs[2])

axs[0].set_title('Positive Reviews')
axs[1].set_title('Neutral Reviews')
axs[2].set_title('Negative Reviews')

plt.tight_layout()
plt.show()