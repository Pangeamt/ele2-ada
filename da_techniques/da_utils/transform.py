import audiomentations


def transform(audio, sr):
    # Transformations dictionary
    trans_dict = {
        audiomentations.augmentations.add_gaussian_noise.AddGaussianNoise: {
            "id": "gaussian_noise",
            "param": "amplitude",
        },
        audiomentations.augmentations.tanh_distortion.TanhDistortion: {
            "id": "tanh_distortion",
            "param": "distortion_amount",
        },
        audiomentations.augmentations.time_stretch.TimeStretch: {
            "id": "time_stretch",
            "param": "rate",
        },
    }

    # Select one of the given tranformations randomly
    oneof = audiomentations.SomeOf(
        1,
        [
            audiomentations.AddGaussianNoise(
                min_amplitude=0.01, max_amplitude=0.025, p=1
            ),
            audiomentations.TanhDistortion(
                min_distortion=0.01, max_distortion=0.70, p=1.0
            ),
            audiomentations.TimeStretch(
                min_rate=0.40, max_rate=1.80, leave_length_unchanged=False, p=1.0
            ),
        ],
    )
    # Apply the transformation selected
    aug_audio = oneof(audio, sample_rate=sr)
    # Get the information of the applied transformation
    trans = [
        t for t in oneof.transforms if t.serialize_parameters()["should_apply"] == True
    ][0]
    # Type of transformation
    trans_applied = trans_dict[trans.__class__]["id"]
    # Value of the parameter
    param = trans_dict[trans.__class__]["param"]
    param_val = trans.serialize_parameters()[param]
    params = {param: param_val}
    # Clip the audio so that its values are between -1 and 1
    result = audiomentations.Clip(p=1)(aug_audio, sample_rate=sr)
    return result, trans_applied, params
