import numpy as np

array = [0, 1 + 4j, -2 + 3j, 4 - 2j, -5 - 6j, -2j, 3]
arrayn = np.array(array)
cs = 0.5 * (arrayn + np.conj(np.fliplr(arrayn)))

print(cs)
