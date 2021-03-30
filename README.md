# lipstick

## Examples

### Creating gif

``` python
import numpy as np
import matplotlib.pyplot as plt
from lipstick import GifMaker

with GifMaker("sample.gif") as g:
    
    for i in range(30): # go through the frames

        # create a figure
        fig, ax = plt.subplots(figsize=(2, 2), dpi=150)
        ax.imshow(np.random.rand(3, 3))
        ax.text(2, 2, i, ha='center', va='center')
        ax.set(xticks=[], yticks=[])
        
        # add the figure object to the GifMaker
        g.add(fig)
        
g.show()
```

Here is the results:
<p align="center">
  <img width="300" height="300" src="images/sample.gif">
</p>

---
- [ ] Scatter plot with histograms
  - hist per axis -> up and right ([link1](https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/scatter_hist.html#sphx-glr-gallery-lines-bars-and-markers-scatter-hist-py), [link2](https://matplotlib.org/3.1.0/gallery/axes_grid1/scatter_hist_locatable_axes.html#sphx-glr-gallery-axes-grid1-scatter-hist-locatable-axes-py))
  - hist for difference of axes -> hist on the diagonal
- [ ] scatter plot with diagonal line
- [ ] [annotated heatmaps](https://matplotlib.org/3.1.0/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py)
- [ ] [multi-column/row subplot layouts](https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/gridspec_multicolumn.html#sphx-glr-gallery-subplots-axes-and-figures-gridspec-multicolumn-py)
- [ ] [Zoom region inset axes](https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/zoom_inset_axes.html#sphx-glr-gallery-subplots-axes-and-figures-zoom-inset-axes-py)
- [ ] [Scatter plot on polar axis](https://matplotlib.org/3.1.0/gallery/pie_and_polar_charts/polar_scatter.html#sphx-glr-gallery-pie-and-polar-charts-polar-scatter-py)
- [ ] [math in plots](https://matplotlib.org/3.1.0/gallery/text_labels_and_annotations/usetex_demo.html#sphx-glr-gallery-text-labels-and-annotations-usetex-demo-py)
- [ ] [creating colormaps](https://matplotlib.org/3.1.0/gallery/color/custom_cmap.html#sphx-glr-gallery-color-custom-cmap-py)
- [ ] [Anchored Direction Arrow](https://matplotlib.org/3.1.0/gallery/axes_grid1/demo_anchored_direction_arrows.html#sphx-glr-gallery-axes-grid1-demo-anchored-direction-arrows-py)
- [ ] [rotated axis](https://matplotlib.org/3.1.0/gallery/axisartist/demo_floating_axes.html#sphx-glr-gallery-axisartist-demo-floating-axes-py)
