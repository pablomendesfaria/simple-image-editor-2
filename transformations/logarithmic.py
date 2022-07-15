"""
Logarithmic
"""
import numpy as np


<<<<<<< HEAD
def log_transform(parent, ui_function, pixels):
    """
    Faz a transformação logaritmica em uma imagem, usando de uma constante * a operação de log na base 10 do pixel + 1
    :param ui_function:
=======
def log_transform(parent, pixels):
    """
    Faz a transformação logaritmica em uma imagem, usando de uma constante * a operação de log na base 10 do pixel + 1
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    c = 255/np.log10(255+1)
    min_nonzero = np.min(pixels[np.nonzero(pixels)])
    pixels[pixels == 0] = min_nonzero
    pixels = np.log10(pixels) * c
    pixels = pixels.astype(int)

<<<<<<< HEAD
    ui_function.set_image(parent, pixels, False, True)
=======
    parent.set_image(pixels, has_filter=True)
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
