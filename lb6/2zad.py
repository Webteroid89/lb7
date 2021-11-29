from collections import Counter
import matplotlib.pyplot as plt
c = Counter("То что нас не убивает, делает нас сильнее!Зачем я тут?")
plt.bar(*zip(*c.most_common("!", "?")))
plt.show()