import matplotlib.pyplot as plt


class MissionVisualizer:
    def __init__(self, theme_color="black"):
        plt.style.use('dark_background')
        self.fig_color = theme_color

    def plot_3d_trajectory(self, spacecraft, moon_coords=None):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')

        # Plot Spacecraft path in Red
        ax.plot(spacecraft.pos[:, 0], spacecraft.pos[:, 1], spacecraft.pos[:, 2],
                color='red', label='Artemis II Path', alpha=0.7)

        # Plot Earth at origin in Blue
        ax.plot([0], [0], [0], 'bo', markersize=15, label="Earth")

        ax.set_title("Artemis II Trajectory")
        ax.legend()
        plt.show()

    def plot_distance_profile(self, spacecraft):
        plt.figure(figsize=(10, 4))
        plt.plot(spacecraft.times.to_datetime(), spacecraft.distances, color='cyan')
        plt.axhline(400171, color='red', linestyle='--', label='Apollo 13 Record')
        plt.ylabel("Distance (km)")
        plt.legend()
        plt.show()
