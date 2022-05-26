import matplotlib.pyplot as plt
import numpy as np

y = np.array([78,21,0.93,0.04,0.029])
my_labels = ["nitrogen","oxygen","Argon","carbon dioxide","others"]
plt.pie(y)
plt.legend(my_labels, title = "air compositions",loc ="best")
plt.show()