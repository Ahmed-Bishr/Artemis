from datetime import datetime
import numpy as np


class TelemetryLoader:
    """Static utility to load NASA OEM files."""

    @staticmethod
    def load_oem(file_path):
        # Skip headers and load columns
        raw_data = np.loadtxt(file_path, skiprows=20, dtype=str)
        times = [datetime.fromisoformat(t) for t in raw_data[:, 0]]
        vectors = raw_data[:, 1:].astype(float)

        return {
            "times": times,
            "pos": vectors[:, :3],
            "vel": vectors[:, 3:]
        }