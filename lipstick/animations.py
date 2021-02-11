import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython import display


def imshow_gif(
    frames,
    fps,
    fig_kws=None,
    imshow_kws=None,
    show=True,
    repeat=True,
    repeat_delay=0.0,
    save=False,
    filename=None,
    ax_manipulator=None,
    tight_layout=True,
):

    ax_manipulator = ax_manipulator if ax_manipulator is not None else lambda x, i: x

    if not isinstance(frames, np.ndarray):
        raise TypeError("Input must be a numpy ndarray")

    if (frames.ndim != 3) and (frames.ndim != 5):
        raise ValueError(
            "input should either have three dimensions (frames, height, width) or five dimensions (n_rows, n_cols, frames, height, width)"
        )

    if frames.ndim == 5:
        n_rows, n_cols, n_frames, height, width = frames.shape
    else:
        n_rows, n_cols, n_frames, height, width = 1, 1, *frames.shape

    fig_kws = fig_kws if fig_kws is not None else {}
    fig, axes = plt.subplots(n_rows, n_cols, **fig_kws)

    axes = axes if frames.ndim == 5 else np.array([axes])
    frames = (
        frames[None, :]
        if frames.ndim == 3
        else frames.reshape(-1, n_frames, height, width)
    )

    imshow_kws = imshow_kws if imshow_kws is not None else {}

    ims = []
    for frame_i in range(n_frames):
        im_axes = []
        for image_i, ax in enumerate(axes.flat):
            im_ax = ax.imshow(frames[image_i, frame_i], **imshow_kws, animated=True)
            ax_manipulator(ax, image_i)
            im_axes.append(im_ax)

        ims.append(im_axes)

    anim = animation.ArtistAnimation(
        fig,
        ims,
        interval=1000 / fps,
        repeat=repeat,
        repeat_delay=repeat_delay,
        blit=True,
    )
    if tight_layout:
        fig.tight_layout()

    if save:
        anim.save(filename if ".gif" in filename else filename + ".gif")

    if show:
        video = anim.to_html5_video()
        html = display.HTML(video)
        display.display(html)
    plt.close()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython import display


def scatter_gif(
    xs,
    ys,
    fps,
    fig_kws=None,
    scatter_kws=None,
    show=True,
    repeat=True,
    repeat_delay=0.0,
    save=False,
    filename=None,
    ax_manipulator=None,
    tight_layout=True,
):

    ax_manipulator = ax_manipulator if ax_manipulator is not None else lambda x, i: x

    if (not isinstance(xs, np.ndarray)) or (not isinstance(ys, np.ndarray)):
        raise TypeError("Inputs must be a numpy ndarray")

    if xs.ndim != ys.ndim:
        raise ValueError("x and y should have same number dimensions")

    if (xs.ndim != 2) and (xs.ndim != 4):
        raise ValueError(
            "Input should either have two dimensions (frames, n_points) or four dimensions (n_rows, n_cols, frames, n_points)"
        )

    if xs.ndim == 4:
        n_rows, n_cols, n_frames, n_points = xs.shape
    else:
        n_rows, n_cols, n_frames, n_points = 1, 1, *xs.shape

    fig_kws = fig_kws if fig_kws is not None else {}
    fig, axes = plt.subplots(n_rows, n_cols, **fig_kws)

    axes = axes if xs.ndim == 4 else np.array([axes])

    if xs.ndim == 2:
        xs = xs[None, :]
        ys = ys[None, :]
    else:
        xs = xs.reshape(-1, n_frames, n_points)
        ys = ys.reshape(-1, n_frames, n_points)

    scatter_kws = scatter_kws if scatter_kws is not None else {}

    ims = []
    for frame_i in range(n_frames):
        im_axes = []
        for image_i, ax in enumerate(axes.flat):

            im_ax = ax.scatter(
                xs[image_i, frame_i], ys[image_i, frame_i], **scatter_kws, animated=True
            )
            ax_manipulator(ax, image_i)
            im_axes.append(im_ax)

        ims.append(im_axes)

    anim = animation.ArtistAnimation(
        fig,
        ims,
        interval=1000 / fps,
        repeat=repeat,
        repeat_delay=repeat_delay,
        blit=True,
    )
    if tight_layout:
        fig.tight_layout()

    if save:
        anim.save(filename if ".gif" in filename else filename + ".gif")

    if show:
        video = anim.to_html5_video()
        html = display.HTML(video)
        display.display(html)
    plt.close()