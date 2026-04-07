import matplotlib.pyplot as plt


class MissionVisualizer:
    def __init__(self, theme_color="black"):
        plt.style.use('dark_background')
        self.fig_color = theme_color

    def plot_3d_trajectory(self, spacecraft, moon_coords=None):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')

        # Plot Spacecraft
        sc = ax.scatter(spacecraft.pos[:, 0], spacecraft.pos[:, 1], spacecraft.pos[:, 2],
                        c=spacecraft.speeds, cmap='viridis')

        # Plot Earth at origin
        ax.plot([0], [0], [0], 'go', markersize=10, label="Earth")

        plt.colorbar(sc, label='Speed (km/s)')
        ax.set_title("Artemis II Trajectory")
        plt.show()

    def plot_distance_profile(self, spacecraft):
        plt.figure(figsize=(10, 4))
        plt.plot(spacecraft.times.to_datetime(), spacecraft.distances, color='cyan')
        plt.axhline(400171, color='red', linestyle='--', label='Apollo 13 Record')
        plt.ylabel("Distance (km)")
        plt.legend()
        plt.show()
