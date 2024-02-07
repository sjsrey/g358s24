# %% [markdown]
# ---
# title: Palmer Penguins
# author: Norah Jones
# date: 3/12/23
# ---

# %%
# | echo: false
import pandas as pd

df = pd.read_csv("palmer-penguins.csv")

# %% [markdown]
"""
## Exploring the data

See @fig-bill-sizes for an exploration of bill sizes by species.
"""

# %%
# | label: fig-bill-sizes
# | fig-cap: Bill Sizes by Species

import matplotlib.pyplot as plt
import seaborn as sns

g = sns.FacetGrid(df, hue="species", height=3, aspect=3.5 / 1.5)
g.map(plt.scatter, "bill_length_mm", "bill_depth_mm").add_legend()
