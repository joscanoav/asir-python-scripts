from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label, ProgressBar
from textual.containers import Vertical
import psutil

class MonitorASIR(App):
    """Nuestra propia versión de htop para clase de ASIR."""
    
    # CSS integrado para darle estilo a la consola
    CSS = """
    Screen {
        align: center middle;
    }
    #contenedor-principal {
        width: 70%;
        height: auto;
        border: solid green;
        padding: 1 2;
        background: $surface;
    }
    Label {
        margin-top: 1;
        text-style: bold;
    }
    """

    # Atajos de teclado para los alumnos
    BINDINGS = [("q", "quit", "Salir del monitor")]

    def compose(self) -> ComposeResult:
        """Aquí construimos las 'piezas' de la interfaz."""
        yield Header(show_clock=True) # Cabecera con la hora
        
        with Vertical(id="contenedor-principal"):
            yield Label("💻 Uso de CPU:", id="texto_cpu")
            yield ProgressBar(total=100, id="barra_cpu", show_eta=False)
            
            yield Label("🧠 Uso de Memoria RAM:", id="texto_ram")
            yield ProgressBar(total=100, id="barra_ram", show_eta=False)
            
        yield Footer() # Pie de página con los atajos de teclado

    def on_mount(self) -> None:
        """Esto se ejecuta nada más abrir la aplicación."""
        # Configuramos un temporizador que actualiza los datos cada segundo (1.0)
        self.set_interval(1.0, self.actualizar_metricas)

    def actualizar_metricas(self) -> None:
        """Función que lee el sistema y actualiza las barras."""
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        
        # Actualizamos los textos
        self.query_one("#texto_cpu", Label).update(f"💻 Uso de CPU: {cpu}%")
        self.query_one("#texto_ram", Label).update(f"🧠 Uso de Memoria RAM: {ram}%")
        
        # Actualizamos las barras de progreso
        self.query_one("#barra_cpu", ProgressBar).update(progress=cpu)
        self.query_one("#barra_ram", ProgressBar).update(progress=ram)

if __name__ == "__main__":
    app = MonitorASIR()
    app.run()