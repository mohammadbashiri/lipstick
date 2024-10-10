import os
import matplotlib.pyplot as plt
import figrid as fg
import math

def add_axis(fig, main_ax, width=0.2, height=0.2, location=(0.7, 0.7), relative_to='ax'):
    """
    Add a new axis for a colorbar or barplot to an existing figure.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure object to add the new axis to.
    main_ax : matplotlib.axes.Axes
        The main axis that the new axis is related to.
    width : float, optional
        The width of the new axis (0 to 1), by default 0.2.
    height : float, optional
        The height of the new axis (0 to 1), by default 0.2.
    location : tuple of float, optional
        The (x, y) location of the new axis (0 to 1), by default (0.7, 0.7).
    relative_to : {'fig', 'ax'}, optional
        If 'fig', the axis is placed relative to the figure. If 'ax', it is placed relative to the main axis, by default 'ax'.

    Returns
    -------
    matplotlib.axes.Axes
        The newly created axis.
    
    Raises
    ------
    ValueError
        If `relative_to` is neither 'fig' nor 'ax'.
    """
    if relative_to == 'fig':
        new_ax = fig.add_axes([location[0], location[1], width, height])
    elif relative_to == 'ax':
        bbox = main_ax.get_position()
        new_x = bbox.x0 + location[0] * bbox.width
        new_y = bbox.y0 + location[1] * bbox.height
        new_ax = fig.add_axes([new_x, new_y, width * bbox.width, height * bbox.height])
    else:
        raise ValueError("relative_to must be either 'fig' or 'ax'")
    return new_ax

def place_axes_on_grid(axes_list, output_path=None, n_cols=3, figsize=None, figscale=1, row_spacing=0.05, col_spacing=0.05, dpi=300, fixed_grid=True, x_offsets=None, y_offsets=None):
    """
    Create a figure layout using figrid and save it as a vectorized format.

    Parameters
    ----------
    axes_list : list of callables
        List of functions that create plots. Each function should accept a figure and axis as arguments.
    output_path : str, optional
        Path to save the figure. If not provided, the figure is not saved, by default None.
    n_cols : int, optional
        Number of columns in the grid, by default 3.
    figsize : tuple of float, optional
        Overall size of the figure (width, height in inches). If not provided, `figscale` will be used to determine size.
    figscale : float, optional
        Scale factor to determine the figure size when `figsize` is not provided, by default 1.
    row_spacing : float, optional
        Vertical space between rows, by default 0.05.
    col_spacing : float, optional
        Horizontal space between columns, by default 0.05.
    dpi : int, optional
        Resolution in dots per inch, by default 300.
    fixed_grid : bool, optional
        Whether to maintain a fixed grid for the last row or allow dynamic resizing, by default True.
    x_offsets : list of float, optional
        List of horizontal offsets to adjust the x-positions of the axes, by default None.
    y_offsets : list of float, optional
        List of vertical offsets to adjust the y-positions of the axes, by default None.

    Returns
    -------
    tuple
        Returns a tuple (fig, axes) where:
        - fig is the figure object.
        - axes is a dictionary of axis objects, with keys 'ax_0', 'ax_1', ..., corresponding to the created axes.

    Raises
    ------
    ValueError
        If the lengths of `x_offsets` or `y_offsets` are less than the number of axes.
    """
    n_axes = len(axes_list)
    x_offsets = x_offsets if x_offsets is not None else [0] * n_axes
    y_offsets = y_offsets if y_offsets is not None else [0] * n_axes
    if len(x_offsets) < n_axes:
        raise ValueError("Please specify an offset for each axis object")
    if len(y_offsets) < n_axes:
        raise ValueError("Please specify an offset for each axis object")
    
    n_rows = math.ceil(n_axes / n_cols)
    figsize = figsize if figsize is not None else (n_cols * figscale, n_rows * figscale)
    row_spacing = row_spacing * figsize[0] / figsize[1]
    fig = plt.figure(figsize=figsize, dpi=dpi)

    max_col_spacing = (1 / n_cols) / 2
    max_row_spacing = (1 / n_rows) / 2
    col_spacing = min(col_spacing, max_col_spacing)
    row_spacing = min(row_spacing, max_row_spacing)

    if not fixed_grid and n_axes % n_cols != 0:
        last_row_cols = n_axes % n_cols
    else:
        last_row_cols = n_cols

    axes = {}
    for i in range(n_axes):
        row_idx = i // n_cols
        col_idx = i % n_cols

        if fixed_grid or row_idx < n_rows - 1:
            x_start = max(0, min(col_idx / n_cols + col_spacing, 1))
            x_end = max(0, min((col_idx + 1) / n_cols - col_spacing, 1))
            y_start = max(0, min(row_idx / n_rows + row_spacing, 1))
            y_end = max(0, min((row_idx + 1) / n_rows - row_spacing, 1))
        else:
            x_start = max(0, col_idx / last_row_cols + col_spacing)
            x_end = min(1, (col_idx + 1) / last_row_cols - col_spacing)
            y_start = max(0, min(row_idx / n_rows + row_spacing, 1))
            y_end = max(0, min((row_idx + 1) / n_rows - row_spacing, 1))

        y_end = y_end - min(0, y_end - y_start - .01)
        axes[f'ax_{i}'] = fg.place_axes_on_grid(fig, xspan=[x_start + x_offsets[i], x_end + x_offsets[i]], yspan=[y_start + y_offsets[i], y_end + y_offsets[i]])

    for i, plot_func in enumerate(axes_list):
        plot_func(fig, axes[f'ax_{i}'])

    # Ensure directory exists
    if output_path is not None:
        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        
        # Use os.path.splitext to safely extract file extension
        file_format = os.path.splitext(output_path)[-1].lstrip('.').lower() or 'pdf'
        fig.savefig(output_path, bbox_inches='tight', format=file_format, dpi=dpi)
        print(f"Vectorized grid saved to {output_path}")

    return fig, axes
