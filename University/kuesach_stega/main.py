import wav
import fin

def read_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()
    
def text_to_bits(text):
    b = text.encode('cp1251') 
    bits = ''.join(format(byte, '08b') for byte in b)
    return bits

def bits_to_text(bits):
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        bytes_list.append(int(byte, 2))
    return bytes(bytes_list).decode('cp1251')

def print_symbol_bits(text, bits):
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        bytes_list.append(byte)
    for i, j in zip(text, bytes_list):
        print(f"{i} -> {j}")



def main():
    wav_file = 'b.wav'
    stego_file = 'stego.wav'
    text_file = 'a.txt'

    secret_text = read_text(text_file)
    print(f'В текстовом контейнере: {secret_text}')

    print("\nКодирование каждой буквы:")
    bytes_secret_text = text_to_bits(secret_text)

    print(bytes_secret_text)
    print_symbol_bits(secret_text, bytes_secret_text)

    num_bits = len(bytes_secret_text)

    print(f"Количество бит для встраивания: {num_bits}")

    channels, sample_rate, bits_per_sample, n_frames = wav.analyze_wav(wav_file)

    # wav.plot_oscillogram_vertical(wav_file, title="Осциллограмма до встраивания")

    wav.embed_lsb_left_channel(wav_file, stego_file, bytes_secret_text)

    extracted = wav.extract_lsb_left_channel(stego_file, num_bits)
    print("Извлеченный текст:", extracted)

    # wav.plot_oscillogram_vertical(wav_file, title="Осциллограмма до встраивания")

    print("\n-----------Оценки-----------\n")

    print(f"Среднеквадратическая ошибка (MSE): {fin.calculate_mse(wav_file, stego_file)}")

    print(f"\nНормированная среднеквадратическая ошибка (NMSE): {fin.calculate_nmse(wav_file, stego_file)}")

if __name__ == "__main__":
    main()



