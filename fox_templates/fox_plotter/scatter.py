import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot


def create_single_scatter(df, x, y, hover_data=None,
                          trendline="ols",
                          title="",
                          labels=None, line_color="red"):
    fig = px.scatter(df, x=x, y=y,
                     hover_data=hover_data,
                     trendline=trendline,
                     title=title,
                     labels=labels)
    fig.update_layout(xaxis_range=[0, max(df.total_spend) + 10],
                      yaxis_range=[1, max(df.Sales) + 3],
                      title_x=0.5,
                      font=dict(size=18))
    fig.data[1].update(line_color=line_color)
    return fig
