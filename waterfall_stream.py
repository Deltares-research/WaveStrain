"""Play recordings as a scrolling waterfall. Edit settings, then run: pixi run waterfall-stream."""

from wavestrain import stream_waterfall

START_DATETIME = "2026-01-01 12:00:00"
STOP_DATETIME = "2026-01-01 12:05:00"
TIMEZONE = "UTC"
FIBER_RANGE_M = None
NORMALIZE_CHANNELS = False
BANDPASS_HZ = None
INTERPOLATION = "kaiser"
CLIP_QUANTILE = 0.8
DISPLAY_SECONDS = 10
PLAYBACK_SPEED = 4.0
FPS = 60
MAX_TIME_ROWS = 1000
PREFETCH_BLOCKS = 4

stream_waterfall(
    START_DATETIME,
    STOP_DATETIME,
    timezone_name=TIMEZONE,
    fiber_range_m=FIBER_RANGE_M,
    normalize_channels=NORMALIZE_CHANNELS,
    bandpass_hz=BANDPASS_HZ,
    interpolation=INTERPOLATION,
    clip_quantile=CLIP_QUANTILE,
    display_seconds=DISPLAY_SECONDS,
    playback_speed=PLAYBACK_SPEED,
    fps=FPS,
    max_time_rows=MAX_TIME_ROWS,
    prefetch_blocks=PREFETCH_BLOCKS,
)
