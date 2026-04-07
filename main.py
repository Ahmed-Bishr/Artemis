from models import ArtemisCapsule, CelestialBody
from loader import TelemetryLoader
from plotter import MissionVisualizer
from astropy.coordinates import EarthLocation
from loader import TelemetryLoader
from models import ArtemisCapsule
from physics import ArtemisNavigator
from animation import MissionAnimator


def run_mission_analysis():
    # 1. Load Data
    data = TelemetryLoader.load_oem('Artemis_II_OEM_2026_04_07_Pre-Lunar-Flyby_to_EI.asc')
    artemis = ArtemisCapsule(data['times'], data['pos'], data['vel'])

    # 2. Initialize Objects
    artemis = ArtemisCapsule(data['times'], data['pos'], data['vel'])
    ksc = EarthLocation(lat=28.5, lon=-80.6)  # Kennedy Space
    nav = ArtemisNavigator(artemis)

    # 3. Visualize
    viz = MissionVisualizer()
    viz.plot_3d_trajectory(artemis)
    viz.plot_distance_profile(artemis)
    sim = MissionAnimator(nav)
    sim.start(speed_multiplier=7200)  # Move 2 hours every second


if __name__ == "__main__":
    run_mission_analysis()