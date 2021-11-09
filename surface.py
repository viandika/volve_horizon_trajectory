from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.interpolate import griddata


def regrid(df, step=64):
    x1 = np.linspace(df["X"].min(), df["X"].max(), step)
    y1 = np.linspace(df["Y"].min(), df["Y"].max(), step)
    x2, y2 = np.meshgrid(x1, y1)
    z2 = griddata((df["X"], df["Y"]), df["Z"], (x2, y2), method='cubic')
    return x2, y2, z2


# Read data from a csv
horizon_dir = Path(r"D:\codes\python\volve_things\horizon")
bcu = pd.read_csv(horizon_dir / "BCU.csv")
hugin_base = pd.read_csv(horizon_dir / "Hugin_Base.csv")
hugin_top = pd.read_csv(horizon_dir / "Hugin_Fm_top.csv")
shetland = pd.read_csv(horizon_dir / "SHETLAND.csv")
ty = pd.read_csv(horizon_dir / "Ty.csv")

bcu_x, bcu_y, bcu_z = regrid(bcu)
hugin_base_x, hugin_base_y, hugin_base_z = regrid(hugin_base)
hugin_top_x, hugin_top_y, hugin_top_z = regrid(hugin_top)
shetland_x, shetland_y, shetland_z = regrid(shetland)
ty_x, ty_y, ty_z = regrid(ty)

fig = go.Figure(
    data=[
        go.Surface(
            z=-bcu_z,
            x=bcu_x,
            y=bcu_y,
            # opacity=1,
            # intensity=z2,
            # colorscale="Viridis",
        ),
        go.Surface(
            z=-hugin_base_z,
            x=hugin_base_x,
            y=hugin_base_y,
            #     opacity=1,
            #     intensity=-hugin_base["Z"],
            #     colorscale="Viridis",
        ),
        go.Surface(
            z=-hugin_top_z,
            x=hugin_top_x,
            y=hugin_top_y,
            #     opacity=1,
            #     intensity=-hugin_top["Z"],
            #     colorscale="Viridis",
        ),
        go.Surface(
            z=-shetland_z,
            x=shetland_x,
            y=shetland_y,
            #     opacity=1,
            #     intensity=-shetland["Z"],
            #     colorscale="Viridis",
        ),
        go.Surface(
            z=-ty_z,
            x=ty_x,
            y=ty_y,
            #     opacity=1,
            #     intensity=-ty["Z"],
            #     colorscale="Viridis",
        ),
    ]
)

# fig.show()
fig.write_html("plot.html")
