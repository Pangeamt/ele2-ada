import audiomentations

from da_utils.get_filename import get_filename
from da_utils.get_extension import get_extension


def add_noise(audio, sr):
    # Background noise parameters
    transformation = audiomentations.AddBackgroundNoise(
        sounds_path="noises/",
        noise_rms="relative",
        min_snr_in_db=6,
        max_snr_in_db=30,
        p=1,
    )
    # Add a background noise
    noise_audio = transformation(audio, sample_rate=sr)
    # Get the applied noise and the parameters used
    noise_file_path = transformation.parameters["noise_file_path"]
    noise_type = get_filename(noise_file_path)
    extension = get_extension(noise_file_path)
    noise_file = f"{noise_type}.{extension}"
    noise_param = transformation.parameters["snr_in_db"]
    return noise_audio, noise_file, noise_param
