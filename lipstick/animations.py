import os
import glob
import shutil
import time
from pathlib import Path
from PIL import Image
from IPython import display
import numpy as np
import matplotlib.pyplot as plt


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
    def __init__(self, filename, fps=30.0):
        """
        Saves gif from added figures.

        Args:
            filename (str): full path and filename of the resulting gif (e.g. "sample.gif")
            fps (float, optional): Frames per second. Defaults to 30.0.
        """

        self.path = "/".join(filename.split(".")[0].split("/")[:-1])
        self.path = self.path if self.path else os.getcwd()
        self.name = filename.split(".")[0].split("/")[-1]
        self.fps = fps
        self.temp_dir = "gifmaker_cache"
        self.i = 0

    def add(self, fig):
        fig.savefig(
            f"{self.temp_dir}/{self.name}" + str(self.i).zfill(4) + ".png",
            bbox_inches="tight",
        )
        plt.close()
        self.i += 1

    def save(self):

        fp_in = "{}/{}*.png".format(self.temp_dir, self.name)
        fp_out = "{}/{}.gif".format(self.path, self.name)

        imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]

        imgs[0].save(
            fp=fp_out,
            format="GIF",
            append_images=imgs[1:],
            save_all=True,
            duration=1000 / self.fps,
            loop=0,
        )

    def show(self):
        fp_out = "{}/{}.gif".format(self.path, self.name)
        return display.Image(filename=fp_out)

    def __enter__(self):
        if Path(self.temp_dir).exists():
            shutil.rmtree(self.temp_dir)
        os.mkdir(self.temp_dir)
        return self

    def __exit__(self, *kw):
        self.save()
        shutil.rmtree(self.temp_dir)
