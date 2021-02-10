def scatter_hist(x, y, 
                 diag_on=False,
                 x_hist_height=1.,
                 y_hist_width=1.,
                 fig_kwgs=None, 
                 scatter_kwgs=None,
                 diag_kwgs=None,
                 hist_kwgs=None,
                 binwidth=0.1):

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    
    fig_kwgs = fig_kwgs if fig_kwgs is not None else {}
    
    if fig_kwgs is not None:
        pass
    else:
        fig_kwgs = {'figsize': (5.5, 5.5)}
        
    fig, axScatter = plt.subplots(**fig_kwgs)

    # the scatter plot:
    scatter_kwgs = scatter_kwgs if scatter_kwgs is not None else {'s':10, 'color': 'k'}
    axScatter.scatter(x, y, **scatter_kwgs)
    axScatter.set_aspect(1.)
    
    if diag_on:
        min_lim = min(min(x), min(y))
        max_lim = max(max(x), max(y))

        diag_kwgs = diag_kwgs if diag_kwgs is not None else {'c': '.4', 'ls': '--'}
        axScatter.plot([min_lim, max_lim], [min_lim, max_lim], max_lim, **diag_kwgs)

    # create new axes on the right and on the top of the current axes
    # The first argument of the new_vertical(new_horizontal) method is
    # the height (width) of the axes to be created in inches.
    divider = make_axes_locatable(axScatter)
    axHistx = divider.append_axes("top", x_hist_height, pad=0.1, sharex=axScatter)
    axHisty = divider.append_axes("right", y_hist_width, pad=0.1, sharey=axScatter)

    # make some labels invisible
    axHistx.xaxis.set_tick_params(labelbottom=False)
    axHisty.yaxis.set_tick_params(labelleft=False)
    
    if hist_kwgs is not None:
        if 'bins' not in hist_kwgs.keys():
            min_lim = min(min(x), min(y))
            max_lim = max(max(x), max(y))
            drange = max_lim - min_lim
            bins = np.arange(min_lim - .1*drange, max_lim + .1*drange + binwidth, binwidth)
    else:
        min_lim = min(min(x), min(y))
        max_lim = max(max(x), max(y))
        drange = max_lim - min_lim
        bins = np.arange(min_lim - .1*drange, max_lim + .1*drange + binwidth, binwidth)
        hist_kwgs = {'color': 'k'}
        
        print(bins[:5])
    
    axHistx.hist(x, bins=bins, **hist_kwgs)
    axHisty.hist(y, bins=bins, orientation='horizontal', **hist_kwgs)
    
    return fig, axScatter, axHistx, axHisty