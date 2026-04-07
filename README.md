# Artemis II Trajectory Analyzer

A Python tool for loading, analysing, and visualising the trajectory of NASA's **Artemis II** lunar mission from real telemetry data in NASA OEM (Orbit Ephemeris Message) format.

---

## Key Features

- **Telemetry loading** – parses NASA OEM `.asc` files into structured position/velocity arrays.
- **3-D trajectory plot** – scatter plot of the spacecraft path colour-coded by speed.
- **Distance profile** – time-series chart of Earth–capsule distance with the Apollo 13 distance record as a reference line.
- **Live animation** – real-time 3-D animation of the capsule moving along its trajectory with a configurable time-acceleration multiplier.
- **Sky-coordinate transforms** – converts spacecraft positions to `AltAz` frame as seen from any ground station via Astropy.

---

## Tech Stack

| Library | Purpose |
|---|---|
| Python 3.x | Core language |
| [NumPy](https://numpy.org/) | Vector maths and array operations |
| [SciPy](https://scipy.org/) | Cubic spline interpolation of the trajectory |
| [Matplotlib](https://matplotlib.org/) | Static plots and `FuncAnimation` animations |
| [Astropy](https://www.astropy.org/) | Time handling and astronomical coordinate transforms |

---

## Data Source

The trajectory data used in this project is based on official NASA ephemeris files.
- **Download Ephemeris Data:** [NASA Artemis II Real-Time Tracking](https://www.nasa.gov/missions/artemis/artemis-2/track-nasas-artemis-ii-mission-in-real-time/)

---

## Prerequisites

- Python **3.8** or later
- `pip` (comes with Python)

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/Ahmed-Bishr/Artemis.git
cd Artemis

# 2. (Recommended) create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install numpy scipy matplotlib astropy
```

> There is no `requirements.txt` yet. The four packages above are everything that is needed.

---

## Usage

Place the OEM telemetry file in the project root (the file is already expected at the path shown in `main.py`):

```
Artemis_II_OEM_2026_04_07_Pre-Lunar-Flyby_to_EI.asc
```

Then run the analysis:

```bash
python main.py
```

This will:
1. Load position and velocity vectors from the OEM file.
2. Open a static 3-D trajectory plot.
3. Open a static distance-profile chart.
4. Start a real-time animated 3-D visualisation (2 hours of mission time per second of animation by default).

---

## Project Structure

```
Artemis/
├── main.py        # Entry point – orchestrates loading, analysis, and visualisation
├── loader.py      # TelemetryLoader  – reads NASA OEM files
├── models.py      # ArtemisCapsule, CelestialBody – trajectory data models
├── physics.py     # ArtemisNavigator – cubic-spline interpolation of position over time
├── plotter.py     # MissionVisualizer – static 3-D and distance plots
├── animation.py   # MissionAnimator  – animated 3-D trajectory
└── README.md
```

---

## Contributing

1. Fork the repository and create a feature branch.
2. Make your changes and ensure the analysis still runs correctly (`python main.py`).
3. Open a pull request describing your changes.

---

## License

This project does not currently specify a license. Please contact the repository owner before reusing or redistributing the code.
