import sounddevice as sd
from scpicy.io.wavfile import write
import wavio as wv

freq = 44100

duration = 10

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

sd.wait()

write("songRecorded0.wav", freq, recording)

wv.write("songRecorded1.wav", recording, freq, sampwidth=2)