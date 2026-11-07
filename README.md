# WaveStrain

Explore wave dynamics in OptoDAS fiber-optic recordings. The processing and
visualization workflows are adapted from the BeaverFiber template: plot known
wave events as waterfalls and noise/signal spectra, export them to SEG-Y, or
play recordings as a scrolling waterfall. Recordings are read only. This is
an event-inspection starting point, not an automatic wave detector.

## Setup (Windows and Linux)

Install [Pixi](https://pixi.sh), open a terminal in the project folder, and run:

```sh
pixi install
```

Copy `.env_example` to `.env` (`Copy-Item .env_example .env` in PowerShell,
or `cp .env_example .env` on Linux). Edit `.env` to point to your recordings
and event list:

```dotenv
data_folder = "data/recordings"
event_list = "data/events.csv"
```

Use forward slashes for Windows paths, e.g. `C:/DAS/recordings`. Relative
paths are resolved from the project root, even when called from another working
directory. The `.env` file is local and is not committed.

Recordings must be OptoDAS `.hdf5` files with `data` (time × channel),
`header/time` (UTC Unix seconds), `header/dt`, `header/channels`, and
`cableSpec/sensorDistances`. Subfolders are searched recursively.

## Plot wave events

Create a CSV with `Test-ID`, `Date`, and time columns. For example:

```csv
Test-ID,Date,Wave time
WAVE-001,2026-01-01,12:00:00
```

Dates may be `YYYY-MM-DD` or `DD-MM-YYYY`; times must be `HH:MM:SS`.
Edit `view_events.py` to select the test IDs and exact measurement column
names in your CSV. Set `TIME_DELTA` to the difference between the event-list
clock and UTC (UTC = event time − `TIME_DELTA`), and adjust the noise and signal
window lengths, fiber range and optional bandpass to suit your recordings.
Run:

```sh
pixi run view-events
```

Waterfall/PSD plots are saved in `outputs/`. Set `WRITE_SEGY = True` to also
export the filtered samples as SEG-Y (one trace per channel). Set
`SHOW_PLOTS = True` to display plots interactively.

## Play recordings

Edit `waterfall_stream.py` to choose start and stop times, their `TIMEZONE`
(e.g. `UTC` or `Europe/Amsterdam`), and the fiber and display settings:

```sh
pixi run waterfall-stream
```

Press Space or click Pause to pause; close the window to stop. The optional
streaming bandpass is causal; the event-plot bandpass is zero-phase.
