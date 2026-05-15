import wave
import struct
import wav

def wav_to_binary_samples(filename, num_samples=50):
    with wave.open(filename, 'rb') as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        frames = wf.readframes(num_samples)

        fmt = "<" + "h" * (len(frames) // sampwidth)
        samples = struct.unpack(fmt, frames)

        left_channel = samples[::n_channels]

        binary_samples = [format(sample & 0xFFFF, '016b') for sample in left_channel]

    return binary_samples

def show_segment_embedding(wav_in, wav_stego, bit_string, window=2):
    import numpy as np

    orig_data, _, n_channels, _, _ = wav.read_wav_amplitudes(wav_in)
    stego_data, _, _, _, _ = wav.read_wav_amplitudes(wav_stego)

    left_orig = orig_data[:, 0]
    left_stego = stego_data[:, 0]

    n_frames = len(left_orig)
    num_bits = len(bit_string)
    segment_size = n_frames // num_bits

    print("\nТочки встраивания (с окрестностью):\n")
    count = 0
    for i in range(num_bits):
        index = i * segment_size + segment_size // 2

        print(f"\nБит{i} = {bit_string[i]} | Сегмент [{i * segment_size} : {(i+1)*segment_size}]")
        print(f"Центральный индекс: {index}")

        print("idx\tОригинал (bin)\t\tСтего (bin)\t\tИзменение")
        
        for j in range(index - window, index + window + 1):
            if j < 0 or j >= n_frames:
                continue

            o = format(int(left_orig[j]) & 0xFFFF, '016b')
            s = format(int(left_stego[j]) & 0xFFFF, '016b')
            if j == index:
                mark = "<<< ВСТРАИВАНИЕ"
                diff = f"{o[:-1]}[{o[-1]}]"
                print(f"{j}\t{diff}\t{s[:-1]}[{s[-1]}]\t{mark}")
            else:
                mark = ""
                diff = o if o == s else f"{o} != {s}"
                print(f"{j}\t{diff}\t{s}\t{mark}")

        count += 1
        if count == 8:
            break
            