import numpy as np
import matplotlib.pyplot as plt


def cumulative_bar(
    left_data,
    right_data,
    left_color="navy",
    right_color="darkorange",
    width=0.2,
    center_diff=0.3,
    fig_kws=None,
):

    fig_kws = fig_kws if fig_kws is not None else {}
    fig, ax = plt.subplots(**fig_kws)

    ind = np.arange(left_data.shape[0])

    # left (reference) data bar plot
    ax.bar(ind, left_data, width, color=left_color, edgecolor="k")

    # right data bar plot
    ax.bar(
        ind + center_diff,
        right_data - left_data,
        width,
        bottom=left_data,
        color=right_color,
        edgecolor="k",
    )

    for ind, tip in enumerate(left_data):
        ax.plot(
            [ind - width / 2, ind + width / 2 + center_diff], [tip, tip], c="k", lw=1
        )

    # plot a reference line (maybe 0)
    ax.plot(
        [0 - width, left_data.shape[0] - 1 + 2 * width + center_diff],
        [0, 0],
        c="k",
        ls="--",
        zorder=0,
    )

    return fig, ax