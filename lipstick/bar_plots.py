import numpy as np
import matplotlib.pyplot as plt


def cumulative_bar(*arrays, linewidth=1, bar_color=None, fig_kws=None):
    """
    Cumulative bar plot.

    Args:
        arrays (iterable): an iterable of lists/arrays.
        linewidth (int, optional): Width for the lines between bars and around the bars. Defaults to 2.
        bar_color (str or list, optional): Colors for the bars: Defaults to None.. You can either provide:
            - a single color as a string or array of RGB values.
            - a list containing the colors for the bars of each array.
            - a list of lists containing the color of every single bar.
        fig_kws (dict, optional): arguments used for figure initialiyation. Defaults to None.

    Returns:
        (tuple): figure, axis
    """

    fig_kws = fig_kws if fig_kws is not None else {}
    fig, ax = plt.subplots(**fig_kws)

    default_color = "k"

    if bar_color is None:
        bar_color = [[default_color] * len(arr) for arr in arrays]
    elif not isinstance(bar_color, list):
        bar_color = [[bar_color] * len(arr) for arr in arrays]
    elif (len(bar_color) == len(arrays)) and not isinstance(bar_color[0], list):
        bar_color = [[bar_color[i]] * len(arr) for i, arr in enumerate(arrays)]

    for data_i, data in enumerate(arrays):

        height = np.concatenate((np.array([data[0]]), np.diff(data)))
        bottom = np.concatenate((np.array([0]), np.array(data[:-1])))

        total_width = 0.8
        single_bar_widths = 0.7 * total_width / len(data)
        linelength = total_width / len(data) - single_bar_widths
        x = data_i + np.concatenate(
            (np.array([0]), np.arange(1, len(data)) * total_width / len(data))
        )
        left_edges = x - single_bar_widths / 2
        right_edges = x + single_bar_widths / 2

        ax.bar(
            x,
            height,
            bottom=bottom,
            width=single_bar_widths,
            edgecolor=default_color,
            color=bar_color[data_i],
            linewidth=linewidth,
        )

        for i in range(len(data) - 1):
            plt.plot(
                [left_edges[i + 1], right_edges[i]],
                [data[i], data[i]],
                c=default_color,
                lw=linewidth,
            )

    ax.set(xticks=np.arange(len(arrays)))

    return fig, ax