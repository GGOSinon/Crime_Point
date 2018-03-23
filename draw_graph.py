import matplotlib.pyplot as plt

F = open('result.txt', 'r')

plot_x = []
plot_y = []
for line in F:
    print(line)
    x, y = line.split()
    plot_x.append(int(x))
    plot_y.append(float(y))

plt.plot(plot_x, plot_y)
plt.show()
