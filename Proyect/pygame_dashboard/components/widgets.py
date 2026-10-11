"""
Widgets interactivos para el dashboard
"""
import pygame
import math
import random
from components.colors import *
from components.effects import *


class Widget:
    """Clase base para todos los widgets"""
    
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.hovered = False
        self.animation_progress = 0
        
    def handle_event(self, event):
        """Maneja eventos de mouse"""
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
    
    def update(self, dt):
        """Actualiza el estado del widget"""
        # Animación de hover
        if self.hovered and self.animation_progress < 1:
            self.animation_progress = min(1, self.animation_progress + 0.05)
        elif not self.hovered and self.animation_progress > 0:
            self.animation_progress = max(0, self.animation_progress - 0.05)
    
    def draw(self, surface):
        """Dibuja el widget (implementar en subclases)"""
        pass


class StatCard(Widget):
    """Tarjeta de estadística con valor y etiqueta"""
    
    def __init__(self, x, y, width, height, label, value, icon_color=NEON_CYAN):
        super().__init__(x, y, width, height)
        self.label = label
        self.value = value
        self.target_value = value
        self.icon_color = icon_color
        self.font_large = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 24)
        
    def set_value(self, value):
        """Establece un nuevo valor con animación"""
        self.target_value = value
    
    def update(self, dt):
        super().update(dt)
        
        # Animar cambio de valor
        if abs(self.value - self.target_value) > 0.1:
            self.value += (self.target_value - self.value) * 0.1
        else:
            self.value = self.target_value
    
    def draw(self, surface):
        # Color de fondo con efecto hover
        bg_color = WIDGET_HOVER if self.hovered else WIDGET_BG
        
        # Dibujar fondo con glow si está en hover
        if self.hovered:
            draw_glow_rect(surface, self.rect, bg_color, glow_size=15, alpha=80)
        else:
            draw_gradient_rect(surface, self.rect, bg_color, DARK_BLUE, border_radius=8)
        
        # Borde
        pygame.draw.rect(surface, self.icon_color, self.rect, 2, border_radius=8)
        
        # Dibujar icono decorativo (hexágono)
        icon_pos = (self.rect.x + 30, self.rect.y + 30)
        draw_hexagon(surface, icon_pos, 15, self.icon_color, width=2)
        
        # Dibujar valor
        value_text = f"{int(self.value)}"
        if self.hovered:
            draw_neon_text(surface, value_text, self.font_large, 
                          (self.rect.x + 20, self.rect.y + 50), self.icon_color)
        else:
            text_surface = self.font_large.render(value_text, True, self.icon_color)
            surface.blit(text_surface, (self.rect.x + 20, self.rect.y + 50))
        
        # Dibujar etiqueta
        label_surface = self.font_small.render(self.label, True, TEXT_SECONDARY)
        surface.blit(label_surface, (self.rect.x + 20, self.rect.y + self.rect.height - 35))


class ProgressBar(Widget):
    """Barra de progreso animada"""
    
    def __init__(self, x, y, width, height, label, max_value=100, color=NEON_CYAN):
        super().__init__(x, y, width, height)
        self.label = label
        self.value = 0
        self.target_value = 0
        self.max_value = max_value
        self.color = color
        self.font = pygame.font.Font(None, 20)
        
    def set_value(self, value):
        """Establece un nuevo valor"""
        self.target_value = min(value, self.max_value)
    
    def update(self, dt):
        super().update(dt)
        
        # Animar cambio de valor
        if abs(self.value - self.target_value) > 0.1:
            self.value += (self.target_value - self.value) * 0.08
        else:
            self.value = self.target_value
    
    def draw(self, surface):
        # Fondo
        bg_rect = self.rect.copy()
        pygame.draw.rect(surface, WIDGET_BG, bg_rect, border_radius=self.rect.height // 2)
        pygame.draw.rect(surface, WIDGET_BORDER, bg_rect, 2, border_radius=self.rect.height // 2)
        
        # Calcular ancho de la barra de progreso
        progress_ratio = self.value / self.max_value
        progress_width = int((self.rect.width - 8) * progress_ratio)
        
        if progress_width > 0:
            # Barra de progreso con gradiente
            progress_rect = pygame.Rect(self.rect.x + 4, self.rect.y + 4, 
                                       progress_width, self.rect.height - 8)
            
            # Gradiente de color
            color_start = self.color
            color_end = tuple(min(255, c + 50) for c in self.color)
            draw_gradient_rect(surface, progress_rect, color_start, color_end, 
                             border_radius=(self.rect.height - 8) // 2)
            
            # Efecto de glow en la barra
            if self.hovered:
                draw_glow_rect(surface, progress_rect, self.color, glow_size=8, alpha=100)
        
        # Texto de porcentaje
        percentage = int(progress_ratio * 100)
        text = f"{self.label}: {percentage}%"
        text_surface = self.font.render(text, True, TEXT_PRIMARY)
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.centery))
        surface.blit(text_surface, text_rect)


class CircularMeter(Widget):
    """Medidor circular tipo RPG"""
    
    def __init__(self, x, y, radius, label, max_value=100, color=NEON_MAGENTA):
        super().__init__(x - radius, y - radius, radius * 2, radius * 2)
        self.center = (x, y)
        self.radius = radius
        self.label = label
        self.value = 0
        self.target_value = 0
        self.max_value = max_value
        self.color = color
        self.font_large = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 18)
        
    def set_value(self, value):
        """Establece un nuevo valor"""
        self.target_value = min(value, self.max_value)
    
    def update(self, dt):
        super().update(dt)
        
        # Animar cambio de valor
        if abs(self.value - self.target_value) > 0.1:
            self.value += (self.target_value - self.value) * 0.08
        else:
            self.value = self.target_value
    
    def draw(self, surface):
        # Círculo de fondo
        pygame.draw.circle(surface, WIDGET_BG, self.center, self.radius)
        pygame.draw.circle(surface, WIDGET_BORDER, self.center, self.radius, 3)
        
        # Arco de progreso
        progress = self.value / self.max_value
        draw_progress_arc(surface, self.center, self.radius - 15, progress, self.color, width=12)
        
        # Efecto de glow si está en hover
        if self.hovered:
            draw_progress_arc(surface, self.center, self.radius - 15, progress, self.color, width=16)
        
        # Valor en el centro
        value_text = f"{int(self.value)}"
        value_surface = self.font_large.render(value_text, True, self.color)
        value_rect = value_surface.get_rect(center=self.center)
        surface.blit(value_surface, value_rect)
        
        # Etiqueta
        label_surface = self.font_small.render(self.label, True, TEXT_SECONDARY)
        label_rect = label_surface.get_rect(center=(self.center[0], self.center[1] + 25))
        surface.blit(label_surface, label_rect)
        
        # Valor máximo
        max_surface = self.font_small.render(f"/ {self.max_value}", True, TEXT_SECONDARY)
        max_rect = max_surface.get_rect(center=(self.center[0], self.center[1] + 40))
        surface.blit(max_surface, max_rect)


class LineGraph(Widget):
    """Gráfico de líneas animado"""
    
    def __init__(self, x, y, width, height, label, max_points=50, color=NEON_GREEN):
        super().__init__(x, y, width, height)
        self.label = label
        self.data_points = []
        self.max_points = max_points
        self.color = color
        self.font = pygame.font.Font(None, 20)
        self.max_value = 100
        
    def add_value(self, value):
        """Añade un nuevo valor al gráfico"""
        self.data_points.append(value)
        if len(self.data_points) > self.max_points:
            self.data_points.pop(0)
        
        # Actualizar valor máximo
        if self.data_points:
            self.max_value = max(max(self.data_points), 1)
    
    def draw(self, surface):
        # Fondo
        draw_gradient_rect(surface, self.rect, WIDGET_BG, DARK_BLUE, border_radius=8)
        pygame.draw.rect(surface, WIDGET_BORDER, self.rect, 2, border_radius=8)
        
        # Etiqueta
        label_surface = self.font.render(self.label, True, TEXT_PRIMARY)
        surface.blit(label_surface, (self.rect.x + 10, self.rect.y + 10))
        
        # Dibujar gráfico
        if len(self.data_points) > 1:
            # Área del gráfico
            graph_rect = pygame.Rect(self.rect.x + 10, self.rect.y + 40, 
                                    self.rect.width - 20, self.rect.height - 50)
            
            # Calcular puntos
            points = []
            for i, value in enumerate(self.data_points):
                x = graph_rect.x + (i / (self.max_points - 1)) * graph_rect.width
                y = graph_rect.bottom - (value / self.max_value) * graph_rect.height
                points.append((x, y))
            
            # Dibujar área bajo la línea (relleno con gradiente)
            if len(points) > 1:
                # Crear polígono para el área
                area_points = points + [(graph_rect.right, graph_rect.bottom), 
                                       (graph_rect.left, graph_rect.bottom)]
                
                # Superficie temporal para el área
                area_surface = pygame.Surface((graph_rect.width, graph_rect.height), pygame.SRCALPHA)
                
                # Ajustar puntos relativos a la superficie
                relative_points = [(p[0] - graph_rect.x, p[1] - graph_rect.y) for p in area_points]
                
                # Dibujar área con transparencia
                color_with_alpha = (*self.color, 50)
                pygame.draw.polygon(area_surface, color_with_alpha, relative_points)
                
                surface.blit(area_surface, (graph_rect.x, graph_rect.y))
            
            # Dibujar línea principal
            pygame.draw.lines(surface, self.color, False, points, 3)
            
            # Dibujar puntos
            for point in points:
                pygame.draw.circle(surface, self.color, (int(point[0]), int(point[1])), 4)
                
                # Efecto de glow en el último punto
                if point == points[-1]:
                    for i in range(3, 0, -1):
                        alpha = 100 // i
                        glow_color = (*self.color, alpha)
                        pygame.draw.circle(surface, glow_color, (int(point[0]), int(point[1])), 4 + i * 2)


class Button(Widget):
    """Botón interactivo con efectos"""
    
    def __init__(self, x, y, width, height, text, color=NEON_CYAN, callback=None):
        super().__init__(x, y, width, height)
        self.text = text
        self.color = color
        self.callback = callback
        self.font = pygame.font.Font(None, 28)
        self.pressed = False
        
    def handle_event(self, event):
        super().handle_event(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed and self.hovered and self.callback:
                self.callback()
            self.pressed = False
    
    def draw(self, surface):
        # Color basado en el estado
        if self.pressed:
            bg_color = tuple(c // 2 for c in self.color)
        elif self.hovered:
            bg_color = self.color
        else:
            bg_color = WIDGET_BG
        
        # Dibujar fondo
        if self.hovered:
            draw_glow_rect(surface, self.rect, bg_color, glow_size=10, alpha=120)
        else:
            pygame.draw.rect(surface, bg_color, self.rect, border_radius=8)
        
        # Borde
        pygame.draw.rect(surface, self.color, self.rect, 2, border_radius=8)
        
        # Texto
        if self.hovered:
            draw_neon_text(surface, self.text, self.font, 
                          (self.rect.centerx - self.font.size(self.text)[0] // 2,
                           self.rect.centery - self.font.size(self.text)[1] // 2),
                          TEXT_PRIMARY, glow_size=3)
        else:
            text_surface = self.font.render(self.text, True, TEXT_PRIMARY)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)
