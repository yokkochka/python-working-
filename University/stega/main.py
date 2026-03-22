import cv2
import numpy as np
import random
from scipy.fftpack import dct, idct


# -----------------------------
# DCT
# -----------------------------

def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


# -----------------------------
# подготовка изображения
# -----------------------------

def prepare_image(img):

    h, w = img.shape[:2]

    h = (h // 8) * 8
    w = (w // 8) * 8

    img = img[:h, :w]

    size = min(h, w)

    return img[:size, :size]


# -----------------------------
# блоки 8x8
# -----------------------------

def split_blocks(channel):

    h, w = channel.shape
    blocks = []

    for i in range(0, h, 8):
        for j in range(0, w, 8):

            block = channel[i:i+8, j:j+8]
            blocks.append(dct2(block))

    return np.array(blocks), h, w


def merge_blocks(blocks, h, w):

    channel = np.zeros((h, w))

    k = 0

    for i in range(0, h, 8):
        for j in range(0, w, 8):

            channel[i:i+8, j:j+8] = idct2(blocks[k])
            k += 1

    return channel


# -----------------------------
# случайные среднечастотные коэффициенты
# -----------------------------

def random_coeff():

    while True:

        u = random.randint(1,6)
        v = random.randint(1,6)

        if 2 <= u+v <= 8:
            return u, v


# -----------------------------
# ВСТРАИВАНИЕ
# -----------------------------

def embed(container, output, text):

    img = cv2.imread(container)
    img = prepare_image(img)

    blue = img[:,:,0].astype(float)

    blocks, h, w = split_blocks(blue)

    bits = ''.join(format(ord(c),'08b') for c in text)

    P = 200

    xy = []

    for i,bit in enumerate(bits):

        block = blocks[i]

        u1,v1 = random_coeff()

        u2,v2 = random_coeff()

        while (u1==u2 and v1==v2):
            u2,v2 = random_coeff()

        xy.append((u1,v1,u2,v2))

        if bit == '1':

            while abs(block[u1,v1]) - abs(block[u2,v2]) >= -P:

                block[u1,v1] -= 1
                block[u2,v2] += 1

        else:

            while abs(block[u1,v1]) - abs(block[u2,v2]) <= P:

                block[u1,v1] += 1
                block[u2,v2] -= 1

        blocks[i] = block

    new_blue = merge_blocks(blocks,h,w)

    img[:,:,0] = np.clip(np.round(new_blue),0,255)

    cv2.imwrite(output,img)

    return xy


# -----------------------------
# ИЗВЛЕЧЕНИЕ
# -----------------------------

def extract(stego, xy):

    img = cv2.imread(stego)
    img = prepare_image(img)

    blue = img[:,:,0].astype(float)

    blocks, h, w = split_blocks(blue)

    bits=""

    for i,(u1,v1,u2,v2) in enumerate(xy):

        block = blocks[i]

        if abs(block[u1,v1]) > abs(block[u2,v2]):
            bits += "0"
        else:
            bits += "1"

    text=""

    for i in range(0,len(bits),8):

        byte = bits[i:i+8]
        text += chr(int(byte,2))

    return text


# -----------------------------
# main
# -----------------------------

def main():

    text = "YOKKO"

    xy = embed("A.bmp","B.bmp",text)

    decoded = extract("B.bmp",xy)

    with open("A.txt","w") as f:
        f.write(decoded)

    print("Извлеченный текст:",decoded)


if __name__ == "__main__":
    main()