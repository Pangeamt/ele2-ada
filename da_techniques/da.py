import json
import librosa
import secrets
import time
import tqdm

import soundfile as sf

from da_utils.data_augmentation import data_augmentation
from da_utils.get_audios import get_audios
from da_utils.get_duration import get_duration


lang_dict_iso3 = {
    "catalan": "cat",
    "galician": "gal",
    "asturian": "ast",
    "euskera": "eus",
}


def da(path, n):
    s = time.time()
    audios = get_audios(path)
    audios_info = list()
    for audio_metadata in tqdm.tqdm(audios):
        audio, sr = librosa.load(audio_metadata["filename"], sr=None)
        lang = lang_dict_iso3[audio_metadata["language"]]
        lang_en = audio_metadata["language"]
        for _ in range(n):
            (
                da_audio,
                sr,
                trans_applied,
                params,
                noise_type,
                noise_param,
            ) = data_augmentation(audio, sr)
            hash_id = secrets.token_hex(nbytes=8)

            filename = f"ADA/{lang}_ADA_{hash_id}.wav"
            sf.write(f"{filename}", da_audio, sr)
            duration = get_duration(f"{filename}")
            info = {
                "id": hash_id,
                "id_parent": audio_metadata["id"],
                "source_text": audio_metadata["source_text"],
                "duration": duration,
                "speaker": [
                    {
                        "label": "speaker_1",
                        "user_id": audio_metadata["speaker"][0]["user_id"],
                        "gender": audio_metadata["speaker"][0]["gender"],
                        "age_range": audio_metadata["speaker"][0]["age_range"],
                    }
                ],
                "type": audio_metadata["type"],
                "filename": filename,
                "language": lang_en,
                "audio_format": {"extension": "wav", "sample_rate": sr},
                "ADA": {
                    "augment_1": {
                        "name": "background_noise",
                        "noise": noise_type.split("-")[0],
                        "filename:": f"noises/{noise_type}",
                        "parameters": {
                            "snr_in_db": noise_param,
                            "rms_noise": "relative",
                        },
                    },
                    "augment_2": {
                        "name": trans_applied,
                        "parameters": {
                            list(params.keys())[0]: list(params.values())[0]
                        },
                    },
                },
            }

            audios_info.append(info)

    with open(f"{lang}_ADA_metadata.json", "w") as outfile:
        json.dump(audios_info, outfile, ensure_ascii=False, indent=4)

    print(f"{round(time.time() - s, 2)}s")
    return


if __name__ == "__main__":
    import sys

    path = sys.argv[1]
    n = int(sys.argv[2])

    da(path, n)
