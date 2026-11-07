"""Plot known wave events. Edit the settings, then run: pixi run view-events."""

from datetime import timedelta
from pathlib import Path

from wavestrain import plot_events
from wavestrain.plot_event import env_path

DATA_FOLDER = env_path("data_folder")
EVENT_LIST = env_path("event_list")
OUTPUT_DIR = Path(__file__).parent / "outputs"

TEST_IDS = ["WAVE-001"]
MEASUREMENTS = ["Wave time"]
TIME_DELTA = timedelta(0)  # UTC = event-list time - TIME_DELTA.
NOISE_SECONDS = 10
SIGNAL_SECONDS = 10
FIBER_RANGE_M = None
NORMALIZE_CHANNELS = False
BANDPASS_HZ = None
INTERPOLATION = "kaiser"
CLIP_QUANTILE = 0.8
SHOW_PLOTS = False
WRITE_SEGY = False

plot_events(
    TEST_IDS,
    measurements=MEASUREMENTS,
    time_delta=TIME_DELTA,
    noise_seconds=NOISE_SECONDS,
    signal_seconds=SIGNAL_SECONDS,
    fiber_range_m=FIBER_RANGE_M,
    normalize_channels=NORMALIZE_CHANNELS,
    bandpass_hz=BANDPASS_HZ,
    interpolation=INTERPOLATION,
    clip_quantile=CLIP_QUANTILE,
    data_folder=DATA_FOLDER,
    event_list=EVENT_LIST,
    output_dir=OUTPUT_DIR,
    show=SHOW_PLOTS,
    write_segy=WRITE_SEGY,
)
