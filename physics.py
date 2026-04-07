import numpy as np
from scipy.interpolate import interp1d


class ArtemisNavigator:
    """Handles the movement and state of the capsule over time."""

    def __init__(self, spacecraft):
        self.sc = spacecraft

        # FIX: Convert Astropy Time to a plain NumPy array of seconds
        # We calculate the difference from the start time in seconds
        time_deltas = (self.sc.times - self.sc.times[0]).sec

        self.t_min = 0
        self.t_max = time_deltas[-1]

        # Now interp1d receives plain floats (seconds) and coordinate arrays
        self._get_pos = interp1d(
            time_deltas,
            self.sc.pos,
            axis=0,
            kind='cubic'
        )

    def get_position_at(self, seconds_from_start):
        """Returns the [x, y, z] position at a specific time offset."""
        t = np.clip(seconds_from_start, self.t_min, self.t_max)
        return self._get_pos(t)

    def get_distance_to_earth(self, seconds_from_start):
        pos = self.get_position_at(seconds_from_start)
        return np.linalg.norm(pos)