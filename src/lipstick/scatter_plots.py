import numpy as np
import matplotlib.pyplot as plt


def scatter_diag(x, y, scatter_kws=None, diag_kws=None, ax=None, share_ticks=False):
    """
    Scatter plot with diagonal line.

    Returns:
        tuple: fig, ax
    """

    if ax is not None:
        ax = ax
        fig = plt.gcf()
    else:
        fig, ax = plt.subplots()

    # the scatter plot:
    scatter_kws = (
        scatter_kws
        if scatter_kws is not None
        else {"c": "k", "ec": "w", "linewidth": 0.5}
    )
    ax.scatter(x, y, **scatter_kws)
    ax.set_aspect(1.0)

    diag_kws = diag_kws if diag_kws is not None else {"c": ".4", "ls": "--"}

    if share_ticks:
        tick_idx = np.where(
            [
                len(ax.get_xticks()) > len(ax.get_yticks()),
                len(ax.get_xticks()) <= len(ax.get_yticks()),
            ]
        )[0].item()
        ticks = [ax.get_xticks(), ax.get_yticks()][tick_idx]
        ax.set(xticks=ticks, yticks=ticks)

        min_lim = ticks.min()
        max_lim = ticks.max()
        ax.plot([min_lim, max_lim], [min_lim, max_lim], max_lim, **diag_kws)

    else:
        min_lim = min(min(x), min(y))
        max_lim = max(max(x), max(y))
        ax.plot([min_lim, max_lim], [min_lim, max_lim], max_lim, **diag_kws)

    return fig, ax


def scatter_hist(
    x,
    y,
    diag_on=False,
    x_hist_height=1.0,
    y_hist_width=1.0,
    fig_kws=None,
    scatter_kws=None,
    diag_kws=None,
    hist_kws=None,
    binwidth=0.1,
):
    """
    Scatter plot with histograms of x and y data.

    Returns:
        tuple: fig, (scatter_axis, hist_x_axis, hist_y_axis)
    """

    from mpl_toolkits.axes_grid1 import make_axes_locatable

    fig_kws = fig_kws if fig_kws is not None else {}

    if fig_kws is not None:
        pass
    else:
        fig_kws = {"figsize": (5.5, 5.5)}

    fig, axScatter = plt.subplots(**fig_kws)

    # the scatter plot:
    scatter_kws = scatter_kws if scatter_kws is not None else {"s": 10, "color": "k"}
    axScatter.scatter(x, y, **scatter_kws)
    axScatter.set_aspect(1.0)

    if diag_on:
        min_lim = min(min(x), min(y))
        max_lim = max(max(x), max(y))

        diag_kws = diag_kws if diag_kws is not None else {"c": ".4", "ls": "--"}
        axScatter.plot([min_lim, max_lim], [min_lim, max_lim], max_lim, **diag_kws)

    # create new axes on the right and on the top of the current axes
    # The first argument of the new_vertical(new_horizontal) method is
    # the height (width) of the axes to be created in inches.
    divider = make_axes_locatable(axScatter)
    axHistx = divider.append_axes("top", x_hist_height, pad=0.1, sharex=axScatter)
    axHisty = divider.append_axes("right", y_hist_width, pad=0.1, sharey=axScatter)

    # make some labels invisible
    axHistx.xaxis.set_tick_params(labelbottom=False)
    axHisty.yaxis.set_tick_params(labelleft=False)

    if hist_kws is not None:
        if "bins" not in hist_kws.keys():
            min_lim = min(min(x), min(y))
            max_lim = max(max(x), max(y))
            drange = max_lim - min_lim
            bins = np.arange(
                min_lim - 0.1 * drange, max_lim + 0.1 * drange + binwidth, binwidth
            )
    else:
        min_lim = min(min(x), min(y))
        max_lim = max(max(x), max(y))
        drange = max_lim - min_lim
        bins = np.arange(
            min_lim - 0.1 * drange, max_lim + 0.1 * drange + binwidth, binwidth
        )
        hist_kws = {"color": "k"}

        print(bins[:5])

    axHistx.hist(x, bins=bins, **hist_kws)
    axHisty.hist(y, bins=bins, orientation="horizontal", **hist_kws)

    return fig, (axScatter, axHistx, axHisty)