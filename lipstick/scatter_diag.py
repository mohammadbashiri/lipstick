def scatter_diag(x, y, 
                 fig_kwgs=None, 
                 scatter_kwgs=None, 
                 diag_kwgs=None):
    
    fig_kwgs = fig_kwgs if fig_kwgs is not None else {}
    
    if fig_kwgs is not None:
        pass
    else:
        fig_kwgs = {'figsize': (5.5, 5.5)}
        
    fig, ax = plt.subplots(**fig_kwgs)

    # the scatter plot:
    scatter_kwgs = scatter_kwgs if scatter_kwgs is not None else {'c': 'k', 'ec': 'w', 'linewidth': .5}
    ax.scatter(x, y, **scatter_kwgs)
    ax.set_aspect(1.)
    
    min_lim = min(min(x), min(y))
    max_lim = max(max(x), max(y))
    
    diag_kwgs = diag_kwgs if diag_kwgs is not None else {'c': '.4', 'ls': '--'}
    ax.plot([min_lim, max_lim], [min_lim, max_lim], max_lim, **diag_kwgs)
    
    return fig, ax