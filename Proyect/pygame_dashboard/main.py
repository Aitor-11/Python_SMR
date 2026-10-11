"""
Dashboard tipo videojuego con Pygame
Un dashboard interactivo con efectos visuales, partículas y widgets animados
"""
import pygame
import sys
import random
import math
from components.colors import *
from components.particle_system import ParticleSystem, ConnectionLines
from components.effects import draw_scanline_effect, draw_neon_text, create_pulse_effect
from components.widgets import StatCard, ProgressBar, CircularMeter, LineGraph, Button


class GameDashboard:
    """Dashboard principal con todos los componentes"""
    
    def __init__(self, width=1400, height=900):
        pygame.init()
        
        # Configuración de la ventana
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Game Dashboard - Pygame")
        
        # Reloj para controlar FPS
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        
        # Sistema de partículas
        self.particle_system = ParticleSystem(width, height, num_particles=80)
        self.connection_lines = ConnectionLines(self.particle_system, max_distance=120)
        
        # Fuentes
        self.title_font = pygame.font.Font(None, 64)
        self.subtitle_font = pygame.font.Font(None, 28)
        
        # Widgets
        self.widgets = []
        self.setup_widgets()
        
        # Variables de simulación
        self.time_counter = 0
        self.update_interval = 60  # Actualizar valores cada 60 frames
        
    def setup_widgets(self):
        """Configura todos los widgets del dashboard"""
        margin = 30
        
        # Fila superior - Tarjetas de estadísticas
        card_width = 280
        card_height = 140
        card_y = 120
        
        self.stat_cards = [
            StatCard(margin, card_y, card_width, card_height, 
                    "Players Online", 1247, NEON_CYAN),
            StatCard(margin + card_width + 20, card_y, card_width, card_height,
                    "Active Servers", 42, NEON_MAGENTA),
            StatCard(margin + (card_width + 20) * 2, card_y, card_width, card_height,
                    "Total Matches", 8934, NEON_GREEN),
            StatCard(margin + (card_width + 20) * 3, card_y, card_width, card_height,
                    "Peak Today", 2156, NEON_ORANGE),
        ]
        self.widgets.extend(self.stat_cards)
        
        # Segunda fila - Barras de progreso
        bar_width = 580
        bar_height = 35
        bar_y = card_y + card_height + 40
        
        self.progress_bars = [
            ProgressBar(margin, bar_y, bar_width, bar_height, 
                       "CPU Usage", 100, NEON_CYAN),
            ProgressBar(margin + bar_width + 20, bar_y, bar_width, bar_height,
                       "Memory", 100, NEON_MAGENTA),
        ]
        self.widgets.extend(self.progress_bars)
        
        # Barras adicionales
        self.progress_bars.extend([
            ProgressBar(margin, bar_y + 50, bar_width, bar_height,
                       "Network", 100, NEON_GREEN),
            ProgressBar(margin + bar_width + 20, bar_y + 50, bar_width, bar_height,
                       "Disk I/O", 100, NEON_ORANGE),
        ])
        self.widgets.extend(self.progress_bars[2:])
        
        # Tercera fila - Medidores circulares
        meter_y = bar_y + 140
        meter_spacing = 200
        
        self.circular_meters = [
            CircularMeter(margin + 80, meter_y, 70, "Health", 100, NEON_GREEN),
            CircularMeter(margin + 80 + meter_spacing, meter_y, 70, "Energy", 100, NEON_CYAN),
            CircularMeter(margin + 80 + meter_spacing * 2, meter_y, 70, "Shield", 100, NEON_MAGENTA),
            CircularMeter(margin + 80 + meter_spacing * 3, meter_y, 70, "Ammo", 100, NEON_ORANGE),
            CircularMeter(margin + 80 + meter_spacing * 4, meter_y, 70, "XP", 100, NEON_PURPLE),
        ]
        self.widgets.extend(self.circular_meters)
        
        # Gráfico de líneas
        graph_y = meter_y + 120
        self.line_graph = LineGraph(margin, graph_y, 1180, 180, 
                                   "Performance Metrics", max_points=40, color=NEON_CYAN)
        self.widgets.append(self.line_graph)
        
        # Botones
        button_width = 180
        button_height = 50
        button_y = self.height - 80
        
        self.buttons = [
            Button(margin, button_y, button_width, button_height, 
                  "Refresh", NEON_CYAN, self.on_refresh_click),
            Button(margin + button_width + 20, button_y, button_width, button_height,
                  "Reset", NEON_MAGENTA, self.on_reset_click),
            Button(margin + (button_width + 20) * 2, button_y, button_width, button_height,
                  "Randomize", NEON_GREEN, self.on_randomize_click),
        ]
        self.widgets.extend(self.buttons)
    
    def on_refresh_click(self):
        """Callback para el botón Refresh"""
        print("Refreshing dashboard...")
        # Añadir burst de partículas
        self.particle_system.add_burst(self.width // 2, self.height // 2, 30, NEON_CYAN)
    
    def on_reset_click(self):
        """Callback para el botón Reset"""
        print("Resetting values...")
        for meter in self.circular_meters:
            meter.set_value(100)
        for bar in self.progress_bars:
            bar.set_value(0)
        self.particle_system.add_burst(self.width // 2, self.height // 2, 30, NEON_MAGENTA)
    
    def on_randomize_click(self):
        """Callback para el botón Randomize"""
        print("Randomizing values...")
        self.randomize_values()
        self.particle_system.add_burst(self.width // 2, self.height // 2, 30, NEON_GREEN)
    
    def randomize_values(self):
        """Actualiza los valores de los widgets con datos aleatorios"""
        # Actualizar tarjetas de estadísticas
        for card in self.stat_cards:
            card.set_value(random.randint(500, 3000))
        
        # Actualizar barras de progreso
        for bar in self.progress_bars:
            bar.set_value(random.randint(20, 95))
        
        # Actualizar medidores circulares
        for meter in self.circular_meters:
            meter.set_value(random.randint(30, 100))
        
        # Añadir punto al gráfico
        self.line_graph.add_value(random.randint(40, 100))
    
    def handle_events(self):
        """Maneja todos los eventos de Pygame"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.randomize_values()
                elif event.key == pygame.K_r:
                    self.on_reset_click()
            
            # Pasar eventos a los widgets
            for widget in self.widgets:
                widget.handle_event(event)
    
    def update(self, dt):
        """Actualiza el estado del dashboard"""
        # Actualizar sistema de partículas
        self.particle_system.update(dt)
        
        # Actualizar widgets
        for widget in self.widgets:
            widget.update(dt)
        
        # Actualizar valores periódicamente
        self.time_counter += 1
        if self.time_counter >= self.update_interval:
            self.time_counter = 0
            
            # Actualizar algunos valores aleatoriamente
            if random.random() > 0.5:
                random.choice(self.progress_bars).set_value(random.randint(20, 95))
            
            if random.random() > 0.7:
                random.choice(self.circular_meters).set_value(random.randint(30, 100))
            
            # Añadir punto al gráfico
            self.line_graph.add_value(random.randint(40, 100))
    
    def draw(self):
        """Dibuja todo el dashboard"""
        # Fondo
        self.screen.fill(BACKGROUND)
        
        # Dibujar líneas de conexión entre partículas
        self.connection_lines.draw(self.screen)
        
        # Dibujar partículas
        self.particle_system.draw(self.screen)
        
        # Título con efecto neón
        title_text = "GAME DASHBOARD"
        pulse_scale = create_pulse_effect(pygame.time.get_ticks(), speed=0.001)
        
        # Calcular posición del título
        title_width = self.title_font.size(title_text)[0]
        title_x = (self.width - title_width) // 2
        title_y = 30
        
        draw_neon_text(self.screen, title_text, self.title_font, 
                      (title_x, title_y), NEON_CYAN, glow_size=8)
        
        # Subtítulo
        subtitle_text = "Real-time System Monitor"
        subtitle_surface = self.subtitle_font.render(subtitle_text, True, TEXT_SECONDARY)
        subtitle_rect = subtitle_surface.get_rect(center=(self.width // 2, 85))
        self.screen.blit(subtitle_surface, subtitle_rect)
        
        # Dibujar todos los widgets
        for widget in self.widgets:
            widget.draw(self.screen)
        
        # Efecto de scanlines (opcional, comentar si reduce demasiado el rendimiento)
        draw_scanline_effect(self.screen, alpha=10)
        
        # FPS counter
        fps_text = f"FPS: {int(self.clock.get_fps())}"
        fps_surface = self.subtitle_font.render(fps_text, True, NEON_GREEN)
        self.screen.blit(fps_surface, (self.width - 100, 10))
        
        # Actualizar pantalla
        pygame.display.flip()
    
    def run(self):
        """Loop principal del dashboard"""
        print("=== Game Dashboard ===")
        print("Controls:")
        print("  SPACE - Randomize values")
        print("  R - Reset values")
        print("  ESC - Exit")
        print("  Mouse - Interact with widgets")
        print("\nStarting dashboard...")
        
        # Inicializar con algunos valores
        self.randomize_values()
        
        # Loop principal
        while self.running:
            # Delta time en milisegundos
            dt = self.clock.tick(self.fps)
            
            # Manejar eventos
            self.handle_events()
            
            # Actualizar
            self.update(dt)
            
            # Dibujar
            self.draw()
        
        # Cleanup
        pygame.quit()
        print("\nDashboard closed.")


def main():
    """Función principal"""
    dashboard = GameDashboard()
    dashboard.run()


if __name__ == "__main__":
    main()
