import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_body
from astropy.time import Time
from astropy.coordinates import get_body

class CelestialBody:
    """Base class for Earth and Moon."""
    def __init__(self, name, location=None):
        self.name = name
        self.location = location # EarthLocation for ground stations

class ArtemisCapsule:
    """Handles the trajectory data logic."""
    def __init__(self, times, positions, velocities):
        self.times = Time(times)
        self.pos = positions  # km
        self.vel = velocities # km/s
        self.distances = np.linalg.norm(self.pos, axis=1)
        self.speeds = np.linalg.norm(self.vel, axis=1)

    def get_sky_coords(self):
        return SkyCoord(x=self.pos[:,0]*u.km, y=self.pos[:,1]*u.km,
                        z=self.pos[:,2]*u.km, representation_type='cartesian',
                        frame='gcrs', obstime=self.times)

    def to_altar(self, observer_location):
        frame = AltAz(location=observer_location, obstime=self.times)
        return self.get_sky_coords().transform_to(frame)


    def get_moon_trajectory(times):
        """Fetches Moon GCRS positions for a list of Astropy Times."""
        moon_coords = get_body("moon", times)
        # Return as [N, 3] array of km for consistent math with your spacecraft
        return moon_coords.cartesian.xyz.to('km').value.T