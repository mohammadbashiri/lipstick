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
    def __init__(self, filename, fps=30.0, dpi='figure', temp_dir_name="gifmaker_cache", keep_dir=False,):
        """
        Saves gif from added figures.

        Args:
            filename (str): full path and filename of the resulting gif (e.g. "sample.gif")
            fps (float, optional): Frames per second. Defaults to 30.0.
            dpi (int, optional): Dots per inch of each image. Defaults to 100. Choose 150 for high quality gifs.
            temp_dir_name (str, optional): Name of the temporary directory. Defaults to "gifmaker_cache".
            keep_dir (bool, optional): If True, the temporary directory is not deleted. Useful when trying to create videos with custom ffmpeg commands. Defaults to False.

        How to convert the gif to a video:
            - set keep_dir=True
            - after all the images are saved, navigate to the temporary directory
            - make sure ffmpeg is installed on your system
            - run the following command within the temporary directory:

                ffmpeg -framerate 30 -pattern_type glob -i '*.png' -c:v libx264 out.mp4

            - the video will be saved as "out.mp4" in the temporary directory, with 30 fps.
        """

        self.path = "/".join(filename.split(".")[0].split("/")[:-1])
        self.path = self.path if self.path else os.getcwd()
        self.name = filename.split(".")[0].split("/")[-1]
        self.fps = fps
        self.dpi = dpi
        self.temp_dir = temp_dir_name
        self.i = 0
        self.keep_dir = keep_dir

    def add(self, fig):
        fig.savefig(
            f"{self.temp_dir}/{self.name}" + str(self.i).zfill(4) + ".png",
            bbox_inches="tight",
            dpi=self.dpi,
        )
        plt.close()
        self.i += 1

    def save(self):
        fp_in = "{}/{}*.png".format(self.temp_dir, self.name)
        fp_out = "{}/{}.gif".format(self.path, self.name)

        imgs = [imageio.imread(f) for f in sorted(glob.glob(fp_in))]
        imageio.mimsave(fp_out, imgs, 'GIF', fps=self.fps)

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
        if not self.keep_dir:
            shutil.rmtree(self.temp_dir)