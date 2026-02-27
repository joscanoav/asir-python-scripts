# 🛠️ asir-python-scripts

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![ASIR](https://img.shields.io/badge/Ciclo-ASIR-success.svg)
![Estado](https://img.shields.io/badge/Estado-En_desarrollo-orange.svg)

Bienvenido a la colección de scripts en Python para la monitorización, automatización y administración de sistemas operativos. Este repositorio está diseñado como material de apoyo práctico para el ciclo formativo de **Administración de Sistemas Informáticos en Red (ASIR)**.

---

## 🚀 ¿Qué incluye este repositorio?

Actualmente, el maletín de herramientas cuenta con los siguientes scripts de monitorización en tiempo real:

* **`graficaCPU.py`**: Monitor básico en ventana de escritorio usando `matplotlib` para visualizar los picos de estrés del procesador.
* **`dashboard_asir.py`**: Interfaz web moderna creada con `Streamlit` para proyectar el rendimiento (CPU y RAM) en el aula a través de la red local.
* **`terminal_asir.py`**: Clon visual tipo `htop` para la terminal de comandos construido con `Textual`.

---

## ⚙️ Requisitos e Instalación

Para que estos scripts funcionen en tu máquina local, necesitas tener Python instalado y descargar las dependencias necesarias.

**1. Clona este repositorio:**
```bash
git clone [https://github.com/TU_USUARIO/asir-python-scripts.git](https://github.com/TU_USUARIO/asir-python-scripts.git)
cd asir-python-scripts

2. Instala las librerías necesarias:
Se recomienda crear un entorno virtual, pero puedes instalarlas globalmente con:

Bash
pip install psutil matplotlib pandas streamlit textual
🖥️ Uso de los Scripts
1. Gráfica de Escritorio
Ejecuta el script de forma tradicional:

Bash
python graficaCPU.py
2. Dashboard Web (Streamlit)
Levanta el servidor web local con el siguiente comando. Una vez ejecutado, podrás acceder desde tu navegador o dar la IP a otros equipos de la misma red:

Bash
python -m streamlit run dashboard_asir.py
3. Monitor de Terminal (TUI)
Para disfrutar de la interfaz gráfica dentro de la consola:

Bash
python terminal_asir.py
(Nota para usuarios de Windows: Se recomienda ejecutar este comando desde CMD, PowerShell o Windows Terminal, evitando Git Bash para que los gráficos se rendericen correctamente).

🎓 Mensaje para los alumnos
Este código es abierto. Os animo a hacer un Fork del repositorio, "romper" el código, cambiar los colores de las gráficas, añadir nuevas métricas (como el uso de disco duro o la red) y experimentar. ¡Así es como realmente se aprende a administrar sistemas!


### 💡 Un par de ajustes antes de guardar:
1. En la sección de instalación, fíjate que puse `https://github.com/TU_USUARIO/asir-python-scripts.git`. ¡Acuérdate de cambiar la palabra `TU_USUARIO` por tu nombre de usuario real de GitHub (`joscanoav`) antes de guardar!
2. GitHub leerá todos esos símbolos de `#` y `*` y los convertirá automáticamente en títulos grandes, líneas separadoras y listas con viñetas. 

Para dejar el repositorio 100% como lo haría un profesional de DevOps, el siguiente paso l