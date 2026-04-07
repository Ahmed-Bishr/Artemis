import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class MissionAnimator:
    def __init__(self, navigator):
        self.nav = navigator
        plt.style.use('dark_background')
        self.fig = plt.figure(figsize=(30, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')

    def start(self, speed_multiplier=3600):
        """
        speed_multiplier: How many mission seconds pass per real second.
        Default 3600 = 1 hour of mission time per second of animation.
        """
        # Set up plot elements
        self.ax.plot([0], [0], [0], 'go', markersize=30, label="Earth")
        line, = self.ax.plot([], [], [], 'w-', alpha=0.3)  # Path trail
        point, = self.ax.plot([], [], [], 'ro', markersize=5, label="Artemis II")

        # Set axes limits based on trajectory
        limit = np.max(np.abs(self.nav.sc.pos))
        self.ax.set_xlim(-limit, limit)
        self.ax.set_ylim(-limit, limit)
        self.ax.set_zlim(-limit, limit)

        def update(frame):
            current_sec = frame * speed_multiplier
            pos = self.nav.get_position_at(current_sec)

            point.set_data([pos[0]], [pos[1]])
            point.set_3d_properties([pos[2]])
            return point,

        ani = FuncAnimation(self.fig, update, frames=int(self.nav.t_max / speed_multiplier),
                            interval=50, blit=True)
        plt.legend()
        plt.show()