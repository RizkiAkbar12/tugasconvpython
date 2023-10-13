#identitas

print ('M RIzki Akbar')
print ('5009211128')
    

import numpy as np

# definsikan panjang sinyal dan kernel
def convolv(sinyal, kernel):
    panjang_signal = len(sinyal)
    panjang_kernel = len(kernel)

# mendefinisikan panjang konvolusi
    panjang_hasil = panjang_signal + panjang_kernel - 1
    hasil_manual = [0] * panjang_hasil

# mendefinisikan fungsi konvolusi nya
    for i in range(panjang_signal):
        for j in range(panjang_kernel):
            hasil_manual[i + j] += sinyal[i] * kernel[j]

    return hasil_manual


signal = [0, 5, 3, 7, 1, 4, 9]
kernel = [0, 6, 4, 7]

hasil_manual = convolv(signal, kernel)
hasil_numpy = np.convolve(signal, kernel).tolist()

print("Konvolusi Manual:", hasil_manual)
print("konvolusi numpy:", hasil_numpy)