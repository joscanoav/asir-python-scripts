import streamlit as st
import psutil
import time
import pandas as pd

# Configuración básica de la página web
st.set_page_config(page_title="Monitor ASIR", page_icon="🖥️", layout="wide")

st.title("🖥️ Dashboard de Rendimiento del Servidor")
st.markdown("Monitorización en tiempo real. Creado con Python y Streamlit.")

# Creamos dos columnas para los "marcadores" (métricas)
col1, col2 = st.columns(2)
marcador_cpu = col1.empty()
marcador_ram = col2.empty()

# Espacio reservado para la gráfica
grafica_espacio = st.empty()

# Listas para guardar el historial de los últimos 50 segundos
historial_cpu = []
historial_ram = []

st.markdown("---")
st.info("💡 Para detener el servidor, pulsa 'Detener' arriba a la derecha o haz Ctrl+C en la terminal.")

# Bucle infinito para actualizar la web en tiempo real
while True:
    # 1. Extraer datos del sistema
    cpu_actual = psutil.cpu_percent(interval=0.5)
    ram_actual = psutil.virtual_memory().percent
    
    # 2. Actualizar los marcadores numéricos
    marcador_cpu.metric(label="Uso de CPU", value=f"{cpu_actual} %")
    marcador_ram.metric(label="Uso de RAM", value=f"{ram_actual} %")
    
    # 3. Guardar en el historial
    historial_cpu.append(cpu_actual)
    historial_ram.append(ram_actual)
    
    # Mantener solo los últimos 50 registros para que la gráfica no se sature
    if len(historial_cpu) > 50:
        historial_cpu.pop(0)
        historial_ram.pop(0)
        
    # 4. Dibujar la gráfica
    # Convertimos los datos a una tabla (DataFrame) que Streamlit entiende perfectamente
    datos_grafica = pd.DataFrame({
        "CPU (%)": historial_cpu,
        "RAM (%)": historial_ram
    })
    
    # Actualizamos el espacio de la gráfica
    grafica_espacio.line_chart(datos_grafica, height=400)
    
    # Pausa de medio segundo antes de la siguiente actualización
    time.sleep(0.5)