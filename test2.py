import pandas as pd
from sklearn.model_selection import train_test_split
# Data ingestion
DATASET_LOC = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/dataset.csv"
df = pd.read_csv(DATASET_LOC)
#print(df.head())

# print(df.tag.value_counts())


# from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()
import warnings; warnings.filterwarnings("ignore")
from wordcloud import WordCloud, STOPWORDS
# ## Exploratory data analysis
# all_tags = Counter(df.tag)
# print(all_tags)
# all_tags.most_common(n=None)


# # Plot tag frequencies
# tags, tag_counts = zip(*all_tags.most_common())
# plt.figure(figsize=(10, 3))
# ax = sns.barplot(x=list(tags), y=list(tag_counts))
# ax.set_xticklabels(tags, rotation=0, fontsize=12)
# plt.title("Tag distribution", fontsize=16)
# plt.ylabel("# of projects", fontsize=14)
# plt.show()


# Most frequent tokens for each tag
tag="natural-language-processing"
plt.figure(figsize=(10, 3))
subset = df[df.tag==tag]
text = subset.title.values
cloud = WordCloud(
    stopwords=STOPWORDS, background_color="black", collocations=False,
    width=500, height=300).generate(" ".join(text))
plt.axis("off")
plt.imshow(cloud)