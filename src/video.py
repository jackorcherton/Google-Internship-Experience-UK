"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)
        self._flagged = None

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    @property
    def flags(self) -> str:
        """Returns if video has been flagged (if it isn't None is returned)"""
        return self._flagged

    def flag_video(self, flag_reason):
        self._flagged = flag_reason

    def __str__(self):
        """Returns title, ID and tags of a video"""
        videoDetails = f"{self._title} ({self._video_id}) [{' '.join(self._tags)}]"
        if self._flagged:
            videoDetails += (f" - FLAGGED (reason: {self._flagged})")
        return videoDetails