"""A video player class."""

from .video_library import VideoLibrary
from random import choice

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self, currentlyPlaying = None):
        self._video_library = VideoLibrary()
        self.currentlyPlaying = currentlyPlaying #Stores details of currently playing video
        self.videoStatus = None #stores if video has been paused

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for videoDetails in sorted(self._video_library.get_all_videos(), key=lambda x: x.title):
          print(" ", videoDetails)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        videoDetails = self._video_library.get_video(video_id) #Attempts to fetch video info
        if videoDetails: #if the ID is valid
            if self.currentlyPlaying != None: #If something is playing
                self.stop_video()
            print("Playing video:", videoDetails.title) #start new video
            self.currentlyPlaying = videoDetails #save in currently playing
            self.videoStatus = "play" #sets video in playing mode
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.currentlyPlaying == None:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:",self.currentlyPlaying.title)
            self.currentlyPlaying = None #reset player
            self.videoStatus = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        videoIDchoices = [] 
        for video in self._video_library.get_all_videos():
            videoIDchoices.append(video.video_id) #store all video ID in tuple
        self.play_video(choice(videoIDchoices)) #pick a random one

    def pause_video(self):
        """Pauses the current video."""
        if self.videoStatus == None:
            print("Cannot pause video: No video is currently playing")
        elif self.videoStatus == "play":
            print("Pausing video:", self.currentlyPlaying.title)
            self.videoStatus = "pause"
        else:
            print("Video already paused:", self.currentlyPlaying.title)

    def continue_video(self):
        """Resumes playing the current video."""
        if self.videoStatus == None:
            print("Cannot continue video: No video is currently playing")
        elif self.videoStatus == "play":
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video:", self.currentlyPlaying.title)
            self.videoStatus = "play"

    def show_playing(self):
        """Displays video currently playing."""
        if self.currentlyPlaying == None:
            print("No video is currently playing")
        elif self.videoStatus == "pause":
            print(f'Currently playing: {self.currentlyPlaying} - PAUSED')
        else:
            print("Currently playing:",self.currentlyPlaying)

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
