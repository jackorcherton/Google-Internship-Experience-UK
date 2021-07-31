"""A video player class."""

from .video_library import VideoLibrary
from random import choice

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self, currentlyPlaying = None):
        self._video_library = VideoLibrary()
        self.currentlyPlaying = currentlyPlaying #Stores details of currently playing video
        self.videoStatus = None #stores if video has been paused
        self.playlists = {}

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
        if " " in playlist_name:
            print("Cannot create playlist: no whitespace allowed")
        elif playlist_name.lower() in [x.lower() for x in self.playlists.keys()]:
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
        validPlaylistName = self.findPlaylistName(playlist_name)
        if validPlaylistName:
            videoTitle = self._video_library.get_video(video_id)
            if videoTitle:
                #valid video ID
                if video_id in self.playlists[validPlaylistName]:
                    print(f"Cannot add video to {playlist_name}: Video already added")
                else:
                    print(f"Added video to {playlist_name}: {videoTitle.title}")
                    self.playlists[validPlaylistName].append(video_id)
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
        validPlaylistName = self.findPlaylistName(playlist_name)
        if validPlaylistName:
            print(f"Showing playlist: {playlist_name}")
            videos = self.playlists[validPlaylistName]
            if videos == []:
                print("No videos here yet")
            else:
                #print([self._video_library.get_video(x) for x in videos])
                for videoInfo in videos:
                    print(self._video_library.get_video(videoInfo))
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        validPlaylistName = self.findPlaylistName(playlist_name)
        if validPlaylistName:
            if self._video_library.get_video(video_id):
                if video_id in self.playlists[validPlaylistName]:
                    self.playlists[validPlaylistName].remove(video_id)
                    print(f"Removed video from {playlist_name}: {self._video_library.get_video(video_id).title}")
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
        validPlaylistName = self.findPlaylistName(playlist_name)
        if validPlaylistName:
            if self.playlists[validPlaylistName] == []:
                print(f"Showing playlist: {playlist_name}")
                print("No videos here yet.")
            else:
                self.playlists[validPlaylistName].clear()
                print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        validPlaylistName = self.findPlaylistName(playlist_name)
        if validPlaylistName:
            self.playlists.pop(validPlaylistName)
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        matchedResults = []
        for videoDetails in sorted(self._video_library.get_all_videos(), key=lambda x: x.title):
            if search_term.lower() in videoDetails.title.lower():
                matchedResults.append(videoDetails.video_id)
        self.search_output(search_term, matchedResults)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        matchedResults = []
        for videoDetails in sorted(self._video_library.get_all_videos(), key=lambda x: x.title):
            for tags in videoDetails.tags:
                if video_tag.lower() in tags.lower():
                    matchedResults.append(videoDetails.video_id)
                    break
        self.search_output(video_tag, matchedResults)

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


    def findPlaylistName(self, playlistInput):
        """Given a playlist name, checks validity and returns correct playlist name"""
        actualPlaylistNames = list(self.playlists.keys())
        position = 0
        for listName in actualPlaylistNames:
            if listName.lower() == playlistInput.lower():
                return actualPlaylistNames[position]
            position += 1

    def search_output(self, search_term, matchedResults):
        """Prints search results"""
        position = 1
        if matchedResults != []:
            print(f"Here are the results for {search_term}:")
            for videoID in matchedResults:
                print(f"{position}) {self._video_library.get_video(videoID)}")
                position += 1
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            try:
                play = int(input())
                if play > len(matchedResults):
                    raise ValueError #number is too high
            except ValueError:
                return
            self.play_video(matchedResults[play-1])
        else:
            print(f"No search results for {search_term}")