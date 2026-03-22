import wave
import numpy as np
import matplotlib.pyplot as plt

def analyze_wav(wav_file):
    with wave.open(wav_file, 'rb') as wav:
        channels = wav.getnchannels()       
        sample_rate = wav.getframerate()    
        sample_width = wav.getsampwidth() 
        n_frames = wav.getnframes()  
        duration = n_frames / sample_rate        

        bits_per_sample = sample_width * 8   

    info = [channels, sample_rate, bits_per_sample, n_frames]

    print("\nАнализ WAV файла")
    print(f"Каналы: {channels}")
    print(f"Частота дискретизации: {sample_rate} Гц")
    print(f"Бит на отсчет: {bits_per_sample}")
    print(f"Длительность: {duration:.02f} сек")
    # print(f"Количество отсчетов: {n_frames}")

    return info


# def read_wav_amplitudes(wav_file):
#     with wave.open(wav_file, 'rb') as wav:
#         n_channels = wav.getnchannels()
#         sample_rate = wav.getframerate()
#         n_frames = wav.getnframes()
#         sample_width = wav.getsampwidth()
#         raw_bytes = wav.readframes(n_frames)

#         if sample_width == 1:
#             dtype = np.uint8
#         elif sample_width == 2:
#             dtype = np.int16
#         else:
#             raise ValueError("Unsupported sample width")

#         audio_data = np.frombuffer(raw_bytes, dtype=dtype)

#         if n_channels > 1:
#             audio_data = audio_data.reshape(-1, n_channels)

#         t = np.arange(n_frames) / sample_rate

#     return audio_data, t, n_channels, sample_rate, sample_width


def read_wav_amplitudes(wav_file):
    with wave.open(wav_file, 'rb') as wav:
        n_channels = wav.getnchannels()
        sample_rate = wav.getframerate()
        n_frames = wav.getnframes()
        sample_width = wav.getsampwidth()
        raw_bytes = wav.readframes(n_frames)

        if sample_width == 1:
            dtype = np.uint8
        elif sample_width == 2:
            dtype = np.int16
        else:
            raise ValueError("Unsupported sample width")
        
        audio_data = np.frombuffer(raw_bytes, dtype=dtype).copy()

        if n_channels > 1:
            audio_data = audio_data.reshape(-1, n_channels)

        t = np.arange(n_frames) / sample_rate

    return audio_data, t, n_channels, sample_rate, sample_width


def plot_oscillogram_vertical(wav_file, title="Осциллограмма"):
    audio_data, t, n_channels, sample_rate, sample_width = read_wav_amplitudes(wav_file)
    
    fig, axes = plt.subplots(n_channels, 1, figsize=(12, 3*n_channels), sharex=True)
    
    if n_channels == 1:
        axes = [axes]
    
    for ch in range(n_channels):
        axes[ch].plot(t, audio_data[:, ch] if n_channels > 1 else audio_data, color='b')
        axes[ch].set_ylabel("Амплитуда")
        axes[ch].set_title(f"{title} - Канал {ch+1}")
        axes[ch].grid(True)
    
    axes[-1].set_xlabel("Время, с")  
    plt.tight_layout()
    plt.show()




def embed_lsb_left_channel(wav_in, wav_out, bit_string):
    """
    Встраивание битовой строки в WAV только в левый канал через LSB
    """
    audio_data, t, n_channels, sample_rate, sample_width = read_wav_amplitudes(wav_in)
    
    if n_channels < 1:
        raise ValueError("Файл должен содержать хотя бы 1 канал")
    
    
    
    left = audio_data[:, 0].copy()  
    n_frames = left.size
    num_bits = len(bit_string)
    
    segment_size = n_frames // num_bits
    print(f"\nКоличество отсчетов (левый канал): {n_frames}")
    print(f"Количество бит для скрытия: {num_bits}")
    print(f"Размер сегмента: {segment_size} отсчетов на 1 бит")

    if n_frames < num_bits:
        raise ValueError("Недостаточно места, встраивание невозможно")
        return 
    else:
        print("\nДостаточно места для встраивания")

    # Встраиваем LSB только в левый канал
    for i in range(num_bits):
        index = i * segment_size + segment_size // 2
        left[index] = np.int16((left[index] & ~1) | int(bit_string[i]))
    
    # Возвращаем левый канал на место
    audio_data[:, 0] = left

    # Сохраняем стего-файл
    with wave.open(wav_out, 'wb') as out:
        out.setnchannels(n_channels)
        out.setsampwidth(sample_width)
        out.setframerate(sample_rate)
        out.writeframes(audio_data.tobytes())

    print("\nВстраивание в левый канал завершено!")



def extract_lsb_left_channel(wav_file, num_bits):
    audio_data, t, n_channels, sample_rate, sample_width = read_wav_amplitudes(wav_file)
    
    left = audio_data[:, 0]  
    n_frames = left.size
    
    segment_size = n_frames // num_bits
    bits = ''
    for i in range(num_bits):
        index = i * segment_size + segment_size // 2
        bits += str(left[index] & 1)  # берем LSB

    # Преобразуем биты в текст
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        bytes_list.append(int(byte, 2))
    
    secret_text = bytes(bytes_list).decode('cp1251')
    return secret_text