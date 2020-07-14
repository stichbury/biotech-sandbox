
from pathlib import PurePosixPath
from typing import Any, Dict

from kedro.io import AbstractVersionedDataSet, Version
from kedro.io.core import get_protocol_and_path

import fsspec
import numpy as np
from PIL import Image


class ImageDataSet(AbstractVersionedDataSet):
    """``ImageDataSet`` loads / save image data from a given filepath as `numpy` array using Pillow.

    Example:
    ::

        >>> ImageDataSet(filepath='/img/file/path.png')
    """

    def __init__(self, filepath: str, version: Version = None):
        """Creates a new instance of ImageDataSet to load / save image data for given filepath.

        Args:
            filepath: The location of the image file to load / save data.
            version: The version of the dataset being saved and loaded.
        """
        protocol, path = get_protocol_and_path(filepath)
        self._protocol = protocol
        self._fs = fsspec.filesystem(self._protocol)

        super().__init__(
            filepath=PurePosixPath(path),
            version=version,
            exists_function=self._fs.exists,
            glob_function=self._fs.glob,
        )

    def _load(self) -> np.ndarray:
        """Loads data from the image file.

        Returns:
            Data from the image file as a numpy array
        """
        load_path = self._get_load_path()
        with self._fs.open(load_path, mode="r") as f:
            image = Image.open(f).convert('RGBA')
            return np.asarray(image)

    def _save(self, data: np.ndarray) -> None:
        """Saves image data to the specified filepath.
        """
        save_path = self._get_save_path()
        with self._fs.open(save_path, mode="wb") as f:
            image = Image.fromarray(data)
            image.save(f)

    def _describe(self) -> Dict[str, Any]:
        """Returns a dict that describes the attributes of the dataset.
        """
        return dict(
            filepath=self._filepath,
            version=self._version,
            protocol=self._protocol
        )
