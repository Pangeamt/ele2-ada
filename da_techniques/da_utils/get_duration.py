def is_wav(file_path):
    import os
    with open(file_path, 'rb') as f:
        return f.read(4) == b'RIFF' and f.read(4) == (os.path.getsize(file_path) - 8).to_bytes(4, 'little') and f.read(4) == b'WAVE' and f.read(4) == b'fmt '

def is_flac(filename):
    import magic
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(filename)
    return file_type == 'audio/x-flac'

def is_mp3(filename):
    import magic
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(filename)
    return file_type == 'audio/mpeg'


def is_mp4(filename):
    import magic
    mime_type = magic.Magic(mime=True).from_file(filename)
    return mime_type == "audio/mp4" or mime_type == "audio/x-m4a" or mime_type == 'video/mp4'

def get_duration(audiofile):
    
    if is_wav(audiofile):
        import soundfile as sf
        return sf.info(audiofile).duration

    if is_mp3(audiofile):
        from mutagen.mp3 import MP3
        audio = MP3(audiofile)
        return audio.info.length
    
    if is_flac(audiofile):
        import utils.flacduration as flac
        return flac.get_flac_duration(audiofile)
    
    if is_mp4(audiofile):
        from pydub import AudioSegment
        audio_file = AudioSegment.from_file(audiofile, format="mp4")
        duration_ms = len(audio_file)
        dur = duration_ms / 1000
        return dur


    return 0