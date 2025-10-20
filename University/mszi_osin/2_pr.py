import random
import os
import hashlib
from pathlib import Path

file_size = 13
signature_size = 10
container_size = 31

file_path = "vo_13bit.bin"
container_path = "mem_chunk.bin"
signature_path = "signature.bin"

def create_random_file():
    num = random.getrandbits(file_size)

    with open(file_path, "wb") as f:
        f.write(num.to_bytes(2, "big"))

    print(f"Создан {file_path} — {file_size} случайных бит (на диске до целых байт).")
    print("Значение (int):", num, "битовое:", bin(num)[2:].zfill(file_size))


def create_container():
    size = container_size * 8  
    with open(container_path, "wb") as f:
        f.write(os.urandom(size))
    print(f"Создан {container_path} — {container_size} случайных Мбайт (на диске до целых Мбайт).")


def create_signature_from_file():
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    data = file.read_bytes()
    h = hashlib.sha256(data).digest()
    sig = h[:signature_size]

    with open(signature_path, "wb") as f:
        f.write(sig)

    return sig

def count_coincidence(precent):

    sig_bytes = Path(signature_path).read_bytes()
    cont_bytes = Path(container_path).read_bytes()

    sig_len_bits = len(sig_bytes) * 8
    cont_len_bits = len(cont_bytes) * 8
    hits = 0

    for shift in range(cont_len_bits - sig_len_bits + 1):
        match_count = 0
        for i in range(sig_len_bits):

            cont_byte_index = (shift + i) // 8
            cont_bit_index = 7 - ((shift + i) % 8) 

            sig_byte_index = i // 8
            sig_bit_index = 7 - (i % 8)

            cont_bit = (cont_bytes[cont_byte_index] >> cont_bit_index) & 1
            sig_bit = (sig_bytes[sig_byte_index] >> sig_bit_index) & 1

            if cont_bit == sig_bit:
                match_count += 1

        match_percent = match_count * 100 / sig_len_bits
        if match_percent >= precent:
            hits += 1

    return hits


create_container()
create_random_file()
create_signature_from_file()


d = {}

for i in range(100, 50, -1):
    d[i] = count_coincidence(i)
    if d[i] != 0:
        print(f"Первое ложное срабатываение возникло при {i}% совпадения ")

print(d)