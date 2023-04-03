import audiomentations
import librosa

# import pandas as pd
import utils.audiofun as af
from jiwer import wer
import numpy as np
import matplotlib.pyplot as plt
import time


transformation_dict = {
    "background_noise": {
        "param": "snr_in_db",
        "label": "SNR (dB)",
        "transformation": audiomentations.AddBackgroundNoise,
        "param_val": np.linspace(-10, 30, 81),
    },
    "gaussian_noise": {
        "param": "amplitude",
        "label": "Amplitude",
        "transformation": audiomentations.AddGaussianNoise,
        "param_val": np.linspace(0.01, 0.5, 99),
    },
    "gaussian_snr": {
        "param": "noise_std",
        "label": "Noise std.",
        "transformation": audiomentations.AddGaussianSNR,
        "param_val": np.linspace(-10, 30, 81),
    },
    "pitch_shifting": {
        "param": "num_semitones",
        "label": "No. of semitones",
        "transformation": audiomentations.PitchShift,
        "param_val": np.linspace(-12, 12, 97),
    },
    "tanh_distortion": {
        "param": "distortion_amount",
        "label": "Distortion level",
        "transformation": audiomentations.TanhDistortion,
        "param_val": np.linspace(0, 1, 101),
    },
    "time_stretch": {
        "param": "rate",
        "label": "Rate",
        "transformation": audiomentations.TimeStretch,
        "param_val": np.linspace(0.1, 3, 59),
    },
}

lang_dict = {
    "gallego": "gl",
    "catalan": "ca",
}


if __name__ == "__main__":
    import json
    import sys
    import whisper
    import tqdm
    import soundfile as sf
    from get_transcription import get_transcription


    id = sys.argv[1]

    with open('final_selected.json', 'r') as f:
        files = json.load(f)

    info = [file for file in files if file['id'] == int(id)][0]

    filename = info['filename']
    lang = lang_dict[info['language']]
    path = info['filename_full']
    reference = get_transcription(path, lang)

    t = sys.argv[2]
    transform = transformation_dict[t]

    # Load audio
    audio, sr = librosa.load(path, sr=None)

    # Lists to save results
    wer_list = list()
    params_list = list()
    transcriptions = list()

    # File to save the transcriptions
    f = open(f'performance/{lang}/transcriptions/{t}/{lang}_{filename.split(".")[0]}_{t}_trancriptions.tsv', "w")
    f.write(f'{transform["param"].capitalize()}\tWER\tTranscription\n')
    f.write(f'-10\t-10\t{reference}\n')

    # Load whisper model
    print("\nLoading whisper model...", end="\r")
    s = time.time()
    whisper_model = whisper.load_model("medium", device="cuda:1")
    print(f"Whisper model loaded in {round(time.time() - s, 2)}s\n")

    for i in tqdm.tqdm(transform["param_val"]):
        # Apply the transformation
        if t == "time_stretch":
            transformation = transform["transformation"](i, i, False, p=1)
        elif t == "background_noise":
            transformation = transform["transformation"](
                "noises/", i, i, "relative", p=1
            )
        else:
            transformation = transform["transformation"](i, i, p=1)

        # Get the transformed audio
        transformed_audio = transformation(audio, sample_rate=sr)

        sf.write(f"performance/tmp.wav", transformed_audio, sr)

        # Get the random parameters used
        params = transformation.serialize_parameters()

        # If the transformation was applied
        if params["should_apply"] == True:
            # Get the transcription using Whisper
            result = whisper_model.transcribe(
                f"performance/tmp.wav", language=lang
            )
            transcription = result["text"]

            # Calculate the WER value
            wer_val = round(wer(reference.lower(), transcription.lower()), 3)

            # Save the results
            wer_list.append(wer_val)
            params_list.append(params[transform["param"]])

            # Save the transcription
            # if transcription not in transcriptions:
            transcriptions.append(transcription)
            f.write(
                f'{round(params[transform["param"]], 3)}\t{wer_val}\t{transcription}\n'
            )

    # Close the file
    f.close()

    # Sort the results
    order = np.argsort(params_list)
    w_sorted = np.array(wer_list)[order]
    p_sorted = np.array(params_list)[order]

    # Visualize the results in a line plot
    ax = plt.subplot(111)
    plt.plot(p_sorted, w_sorted)
    plt.title(f'{" ".join([e.capitalize() for e in t.split("_")])}')
    plt.xlabel(transform["label"])
    plt.ylabel("WER")
    ax.title.set_fontsize(15)
    ax.xaxis.label.set_fontsize(12)
    ax.yaxis.label.set_fontsize(12)

    # Save the plot as an png image
    plt.savefig(f'performance/{lang}/figs/{t}/{lang}_{filename.split(".")[0]}_{t}.png')
