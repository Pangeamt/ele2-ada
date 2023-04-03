from da_utils.add_noise import add_noise
from da_utils.transform import transform

def data_augmentation(audio, sr):
    # Add a background noise
    audio_noise, noise_type, noise_param = add_noise(audio=audio, sr=None)
    # Apply a transformation
    aug_audio, trans_applied, params = transform(audio=audio_noise, sr=sr)
    return aug_audio, sr, trans_applied, params, noise_type, noise_param