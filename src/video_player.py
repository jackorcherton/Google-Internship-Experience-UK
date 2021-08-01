"""A video player class."""

from random import choice
from .video_library import VideoLibrary

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self, currently_playing = None):
        self._video_library = VideoLibrary()
        self.currently_playing = currently_playing #Stores details of currently playing video
        self.video_status = None #stores if video has been paused
        self.playlists = {}

    def number_of_videos(self):
        """Returns total number of videos"""
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for video_details in sorted(self._video_library.get_all_videos(), key=lambda x: x.title):
            print(" ", video_details)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video_details = self._video_library.get_video(video_id) #Attempts to fetch video info
        if video_details: #if the ID is valid
            if self.currently_playing is not None: #If something is playing
                self.stop_video()
            if video_details.flags:
                print(f"Cannot play video: Video is currently flagged"
                f" (reason: {video_details.flags})")
                return
            print("Playing video:", video_details.title) #start new video
            self.currently_playing = video_details #save in currently playing
            self.video_status = "play" #sets video in playing mode
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.currently_playing is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:",self.currently_playing.title)
            self.currently_playing = None #reset player
            self.video_status = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_choices = []
        for video in self._video_library.get_all_videos():
            if video.flags:
                continue #if a video is flagged, skip it
            video_choices.append(video.video_id) #store all video ID in tuple

        if video_choices:
            self.play_video(choice(video_choices)) #pick a random one
        else:
            print("No videos available")

    def pause_video(self):
        """Pauses the current video."""
        if self.video_status is None:
            print("Cannot pause video: No video is currently playing")
        elif self.video_status == "play":
            print("Pausing video:", self.currently_playing.title)
            self.video_status = "pause"
        else:
            print("Video already paused:", self.currently_playing.title)

    def continue_video(self):
        """Resumes playing the current video."""
        if self.video_status is None:
            print("Cannot continue video: No video is currently playing")
        elif self.video_status == "play":
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video:", self.currently_playing.title)
            self.video_status = "play"

    def show_playing(self):
        """Displays video currently playing."""
        if self.currently_playing is None:
            print("No video is currently playing")
        elif self.video_status == "pause":
            print(f'Currently playing: {self.currently_playing} - PAUSED')
        else:
            print("Currently playing:",self.currently_playing)

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if " " in playlist_name:
            print("Cannot create playlist: no whitespace allowed")
        elif playlist_name.lower() in [key.lower() for key in self.playlists]:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            print("Successfully created new playlist:", playlist_name)
            self.playlists[playlist_name] = []

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        valid_playlist_name = self.find_playlist_name(playlist_name)
        if valid_playlist_name:
            video_title = self._video_library.get_video(video_id)
            if video_title:
                #valid video ID
                if video_title.flags:
                    print(f"Cannot add video to {playlist_name}: "
                    f"Video is currently flagged (reason: {video_title.flags})")
                elif video_id in self.playlists[valid_playlist_name]:
                    print(f"Cannot add video to {playlist_name}: Video already added")
                else:
                    print(f"Added video to {playlist_name}: {video_title.title}")
                    self.playlists[valid_playlist_name].append(video_id)
            else:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        print(f"Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        if self.playlists:
            print("Showing all playlists:")
            for title in sorted(self.playlists.keys()):
                print(title)
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        valid_playlist_name = self.find_playlist_name(playlist_name)
        if valid_playlist_name:
            print(f"Showing playlist: {playlist_name}")
            videos = self.playlists[valid_playlist_name]
            if videos == []:
                print("No videos here yet")
            else:
                for video_info in videos:
                    print(self._video_library.get_video(video_info))
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        valid_playlist_name = self.find_playlist_name(playlist_name)
        if valid_playlist_name:
            if self._video_library.get_video(video_id):
                if video_id in self.playlists[valid_playlist_name]:
                    self.playlists[valid_playlist_name].remove(video_id)
                    print(f"Removed video from {playlist_name}: "
                    f"{self._video_library.get_video(video_id).title}")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")
        else:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        valid_playlist_name = self.find_playlist_name(playlist_name)
        if valid_playlist_name:
            if self.playlists[valid_playlist_name] == []:
                print(f"Showing playlist: {playlist_name}")
                print("No videos here yet.")
            else:
                self.playlists[valid_playlist_name].clear()
                print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        valid_playlist_name = self.find_playlist_name(playlist_name)
        if valid_playlist_name:
            self.playlists.pop(valid_playlist_name)
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        matched_results = []
        for video_details in sorted(self._video_library.get_all_videos(), key=lambda x: x.title):
            if search_term.lower() in video_details.title.lower() and not video_details.flags:
                matched_results.append(video_details.video_id)
        self.search_output(search_term, matched_results)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        matched_results = []
        for video_details in sorted(self._video_library.get_all_videos(), key=lambda x: x.title):
            for tags in video_details.tags:
                if video_tag.lower() in tags.lower()  and not video_details.flags:
                    matched_results.append(video_details.video_id)
                    break
        self.search_output(video_tag, matched_results)

    def flag_video(self, video_id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        video_details = self._video_library.get_video(video_id) #Attempts to fetch video info
        if video_details:
            if video_details.flags:
                print("Cannot flag video: Video is already flagged")
            else:
                if self.currently_playing == video_details:
                    self.stop_video()
                video_details.flag_video(flag_reason)
                print(f"Successfully flagged video: {video_details.title} "
                f"(reason: {video_details.flags})")
        else:
            print("Cannot flag video: Video does not exist")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        video_details = self._video_library.get_video(video_id) #Attempts to fetch video info
        if video_details:
            if video_details.flags:
                video_details.flag_video(None)
                print(f"Successfully removed flag from video: {video_details.title}")
            else:
                print("Cannot remove flag from video: Video is not flagged")

        else:
            print("Cannot remove flag from video: Video does not exist")

    def find_playlist_name(self, playlist_input):
        """Given a playlist name, checks validity and returns correct playlist name"""
        actual_playlist_names = list(self.playlists.keys())
        position = 0
        for list_name in actual_playlist_names:
            if list_name.lower() == playlist_input.lower():
                return actual_playlist_names[position]
            position += 1
        return None

    def search_output(self, search_term, matched_results):
        """Prints search results"""
        position = 1
        if matched_results != []:
            print(f"Here are the results for {search_term}:")
            for video_id in matched_results:
                print(f"{position}) {self._video_library.get_video(video_id)}")
                position += 1
            print("Would you like to play any of the above? "
            "If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            try:
                play = int(input())
                if play > len(matched_results):
                    raise ValueError #number is too high
            except ValueError:
                return
            self.play_video(matched_results[play-1])
        else:
            print(f"No search results for {search_term}")
