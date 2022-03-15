from lucidsonicdreams.main import LucidSonicDream

L = LucidSonicDream(song="ifeelspace.mp3")

L.hallucinate(
    "Abstract2.mp4",
    speed_fpm=10,
    pulse_react=0.7,
    motion_react=0.5,
    contrast_strength=0.5,
    flash_strength=0.6,
    motion_randomness=0.9,
    duration=5,
)
