import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuramos la figura y los ejes
fig, ax = plt.subplots()
x_data, y_data = [], []

def actualizar_grafica(frame):
    # Añadimos el "tick" de tiempo y el porcentaje actual de CPU
    x_data.append(frame)
    y_data.append(psutil.cpu_percent(interval=None))
    
    # Mantenemos solo los últimos 50 puntos para que la gráfica "avance"
    x_plot = x_data[-50:]
    y_plot = y_data[-50:]
    
    # Limpiamos y redibujamos
    ax.clear()
    ax.plot(x_plot, y_plot, color='blue', linewidth=2)
    ax.fill_between(x_plot, y_plot, color='blue', alpha=0.3) # Sombreado bajo la línea
    
    # Formato de la gráfica
    ax.set_ylim(0, 100)
    ax.set_title("Rendimiento de CPU en Tiempo Real (%)", fontsize=14, fontweight='bold')
    ax.set_ylabel("Uso de CPU (%)")
    ax.set_xlabel("Tiempo (segundos)")
    ax.grid(True, linestyle='--', alpha=0.6)

# Creamos la animación que se actualiza cada 1000 ms (1 segundo)
ani = animation.FuncAnimation(fig, actualizar_grafica, interval=1000, cache_frame_data=False)

plt.show()