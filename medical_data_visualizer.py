import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.options.mode.chained_assignment = None

def draw_heat_map():
    df = pd.read_csv('medical_examination.csv')

    df = df[df['ap_lo'] <= df['ap_hi']]
    df = df[df['height'] >= df['height'].quantile(0.025)]
    df = df[df['height'] <= df['height'].quantile(0.975)]
    df = df[df['weight'] >= df['weight'].quantile(0.025)]
    df = df[df['weight'] <= df['weight'].quantile(0.975)]

    corr = df.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 10))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    fig.savefig('heatmap.png')
    return fig