import numpy as np
import wav 

def calculate_mse(original_wav, stego_wav):
    orig_data, _, _, _, _ = wav.read_wav_amplitudes(original_wav)
    stego_data, _, _, _, _ = wav.read_wav_amplitudes(stego_wav)
    
    orig_data = orig_data.astype(np.float64)
    stego_data = stego_data.astype(np.float64)
    
    mse = np.mean((orig_data - stego_data) ** 2)

    return mse

def calculate_nmse(original_wav, stego_wav):

    orig_data, _, _, _, _ = wav.read_wav_amplitudes(original_wav)
    stego_data, _, _, _, _ = wav.read_wav_amplitudes(stego_wav)
    
    orig_data = orig_data.astype(np.float64)
    stego_data = stego_data.astype(np.float64)

    nmse = np.sum((orig_data - stego_data)**2) / np.sum(orig_data**2)

    return nmse