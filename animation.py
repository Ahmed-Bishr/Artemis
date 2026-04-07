import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from astropy.coordinates import get_body


class MissionAnimator:
    def __init__(self, navigator):
        self.nav = navigator
        plt.style.use('dark_background')
        self.fig = plt.figure(figsize=(15, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')

    def start(self, speed_multiplier=3600):
        # 1. Fetch Moon Data (White)
        moon_coords = get_body("moon", self.nav.sc.times)
        self.moon_pos = moon_coords.cartesian.xyz.to('km').value.T

        # 2. Setup Static Earth (Blue)
        self.ax.plot([0], [0], [0], 'bo', markersize=20, label="Earth")

        # 3. Setup Moon Marker (White)
        moon_point, = self.ax.plot([], [], [], 'wo', markersize=10, label="Moon")

        # 4. Setup Trajectory Line (White Trail)
        trajectory_line, = self.ax.plot([], [], [], 'w-', lw=1, alpha=0.5, label="Trajectory")

        # 5. Setup Spacecraft (Red)
        point, = self.ax.plot([], [], [], 'ro', markersize=6, label="Artemis II", zorder=10)

        # 6. Set axes limits based on the Moon's distance (~400,000 km)
        limit = 450000
        self.ax.set_xlim(-limit, limit)
        self.ax.set_ylim(-limit, limit)
        self.ax.set_zlim(-limit, limit)

        self.ax.set_xlabel("X (km)")
        self.ax.set_ylabel("Y (km)")
        self.ax.set_zlabel("Z (km)")
        self.ax.legend()

        self.history_x, self.history_y, self.history_z = [], [], []

        def update(frame):
            current_sec = frame * speed_multiplier
            pos = self.nav.get_position_at(current_sec)

            # Update Spacecraft History
            self.history_x.append(pos[0])
            self.history_y.append(pos[1])
            self.history_z.append(pos[2])

            # Update Spacecraft and Trail
            trajectory_line.set_data(self.history_x, self.history_y)
            trajectory_line.set_3d_properties(self.history_z)
            point.set_data([pos[0]], [pos[1]])
            point.set_3d_properties([pos[2]])

            # Update Moon Position
            # We use the frame index to pick the corresponding moon position
            m_pos = self.moon_pos[min(frame, len(self.moon_pos) - 1)]
            moon_point.set_data([m_pos[0]], [m_pos[1]])
            moon_point.set_3d_properties([m_pos[2]])

            return trajectory_line, point, moon_point

        ani = FuncAnimation(
            self.fig,
            update,
            frames=int(self.nav.t_max / speed_multiplier),
            interval=30,
            blit=False
        )
        plt.show()