\class Track:
    """
    A class representing a music track with playback controls.

    This class stores track metadata (title, duration, artist, year) and provides
    methods for controlling playback: play, pause, and stop. Tracks maintain
    their own playback state as they are played.

    Attributes:
        __title (str): The title of the track.
        __duration (int): The duration of the track in seconds.
        __artist (str): The name of the artist.
        __year (int): The release year of the track.
        __is_playing (bool): Flag indicating if the track is currently playing.
        __is_paused (bool): Flag indicating if the track is currently paused.
    """
    def __init__(self, title: str, duration: int,
                 artist: str, year: int) -> None:
        """
        Initialize a Track instance.

        Args:
            title (str): The title of the track.
            duration (int): The duration of the track in seconds.
            artist (str): The name of the artist.
            year (int): The release year of the track.
        """
        self.__title = title
        self.__duration = duration
        self.__artist = artist
        self.__year = year

        self.__is_playing = False
        self.__is_paused = False

    @property
    def title(self) -> str:
        """
        Get the track title.

        Returns:
            str: The title of the track.
        """
        return self.__title

    @property
    def duration(self) -> int:
        """
        Get the track duration.

        Returns:
            int: The duration of the track in seconds.
        """
        return self.__duration

    @property
    def artist(self) -> str:
        """
        Get the track artist.

        Returns:
            str: The name of the artist.
        """
        return self.__artist

    @property
    def year(self) -> int:
        """
        Get the track release year.

        Returns:
            int: The release year of the track.
        """
        return self.__year

    def play(self) -> None:
        """
        Start playing the track.

        If the track is not already playing, sets its state to playing,
        clears any paused state, and prints a message.
        """
        if not self.__is_playing:
            self.__is_playing = True
            self.__is_paused = False
            print(f'Играет: {self.__title}')

    def pause(self) -> None:
        """
        Pause the currently playing track.

        If the track is playing and not already paused, sets its state to paused
        and prints a message.
        """
        if self.__is_playing and not self.__is_paused:
            self.__is_paused = True
            print(f'Пауза: {self.__title}')

    def stop(self) -> None:
        """
        Stop the currently playing track.

        If the track is playing, sets its state to stopped (not playing, not paused)
        and prints a message.
        """
        if self.__is_playing:
            self.__is_playing = False
            self.__is_paused = False
            print(f'Остановлено: {self.__title}')

    def __repr__(self) -> str:
        """
        Return a string representation of the track.

        Returns:
            str: A formatted string with title, artist, and year.
        """
        return f'{self.__title} ({self.__artist}, {self.__year})'


class Album:
    """
    A class representing a music album containing multiple tracks.

    This class manages a collection of tracks, providing methods to add, remove,
    display, and play tracks from the album. It keeps track of the currently
    playing track and allows controlling its playback.

    Attributes:
        __name (str): The name of the album.
        __artist (str): The artist of the album.
        __year (int): The release year of the album.
        _tracks (list[Track]): List of tracks in the album.
        _current_track (Track | None): The currently playing track, or None.
    """
    def __init__(self, name: str, artist: str, year: int) -> None:
        """
        Initialize an Album instance.

        Args:
            name (str): The name of the album.
            artist (str): The artist of the album.
            year (int): The release year of the album.
        """
        self.__name = name
        self.__artist = artist
        self.__year = year
        self._tracks = []
        self._current_track = None

    @property
    def name(self) -> str:
        """
        Get the album name.

        Returns:
            str: The name of the album.
        """
        return self.__name

    @property
    def tracks(self) -> list['Track']:
        """
        Get the list of tracks in the album.

        Returns:
            list[Track]: A list containing all tracks in the album.
        """
        return self._tracks

    def add_track(self, track: Track):
        """
        Add a track to the album.

        Args:
            track (Track): The track to add to the album.
        """
        self._tracks.append(track)

    def remove_track(self, title: str):
        """
        Remove a track from the album by its title.

        Args:
            title (str): The title of the track to remove.
        """
        self._tracks = [t for t in self._tracks if t.title != title]

    def show_tracks(self):
        """
        Display all tracks in the album with their numbers.

        Prints each track with an index number starting from 1.
        """
        for i, track in enumerate(self._tracks, start=1):
            print(f'{i}. {track}')

    def play_track(self, index: int):
        """
        Play a track from the album by its index.

        Stops any currently playing track before starting the new one.

        Args:
            index (int): The zero-based index of the track to play.
        """
        if 0 <= index < len(self._tracks):
            if self._current_track:
                self._current_track.stop()

            self._current_track = self._tracks[index]
            self._current_track.play()
        else:
            print('Неверный номер трека')

    def pause(self):
        """
        Pause the currently playing track.

        Does nothing if no track is currently playing.
        """
        if self._current_track:
            self._current_track.pause()

    def stop(self):
        """
        Stop the currently playing track and clear the current track reference.

        Does nothing if no track is currently playing.
        """
        if self._current_track:
            self._current_track.stop()
            self._current_track = None
