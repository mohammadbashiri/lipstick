import os
import glob
import shutil
import time
from pathlib import Path
from IPython import display
import matplotlib.pyplot as plt
import numpy as np
import imageio

def update_fig(fig, axes, sleep=0):
    display.clear_output(wait=True)
    display.display(fig)
    time.sleep(sleep)
    if isinstance(axes, list) or isinstance(axes, tuple):
        for ax in axes:
            ax.clear()
    elif isinstance(axes, np.ndarray):
        for ax in axes.flatten():
            ax.clear()
    else:
        axes.clear()
    plt.close()


class GifMaker:
    def __init__(self, filename, fps=30.0, dpi='figure', temp_dir_name="gifmaker_cache", keep_dir=False, loop=0):
        """
        Saves gif from added figures.

        Parameters
        ----------
        filename : str
            Full path and filename of the resulting gif (e.g. "sample.gif").
        fps : float, optional
            Frames per second. Defaults to 30.0.
        dpi : int or str, optional
            Dots per inch for each image. Defaults to the figure's dpi setting. Use higher dpi for better quality gifs.
        temp_dir_name : str, optional
            Temporary directory name. Defaults to "gifmaker_cache".
        keep_dir : bool, optional
            If True, the temporary directory is not deleted. Defaults to False.
        """
        self.filename = Path(filename)
        self.path = self.filename.parent if self.filename.parent != Path('.') else Path.cwd()
        self.name = self.filename.stem
        self.ext = self.filename.suffix or ".gif"
        self.fps = fps
        self.dpi = dpi
        self.temp_dir = Path(temp_dir_name)
        self.i = 0
        self.keep_dir = keep_dir
        self.loop = loop

        # Ensure the directory for output exists
        self.path.mkdir(parents=True, exist_ok=True)

    def add(self, fig):
        self.temp_dir.mkdir(exist_ok=True)  # Ensure temp directory exists
        fig.savefig(self.temp_dir / f"{self.name}{str(self.i).zfill(4)}.png",
                    bbox_inches="tight", dpi=self.dpi)
        plt.close(fig)
        self.i += 1

    def save(self):
        fp_in = str(self.temp_dir / f"{self.name}*.png")
        fp_out = self.path / f"{self.name}.gif"

        imgs = [imageio.imread(f) for f in sorted(glob.glob(fp_in))]
        imageio.mimsave(fp_out, imgs, 'GIF', fps=self.fps, loop=self.loop)
        print(f"GIF saved to {fp_out}")

    def show(self):
        fp_out = self.path / f"{self.name}.gif"
        return display.Image(filename=fp_out)

    def __enter__(self):
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
        self.temp_dir.mkdir(exist_ok=True)
        return self

    def __exit__(self, *kw):
        self.save()
        if not self.keep_dir:
            shutil.rmtree(self.temp_dir)
