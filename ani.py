import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Inizializza il grafico
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
line, = ax.plot(x, y)

# Funzione di aggiornamento che viene chiamata ad ogni passo dell'animazione
def update(num):
    # Calcola i nuovi dati
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x + num*np.pi/50)
    # Aggiorna i dati del grafico e ridisegna il grafico
    line.set_xdata(x)
    line.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    return line,

# Crea l'animazione
ani = animation.FuncAnimation(fig, update, frames=range(100), blit=True)
plt.show()
