"""
Efectos visuales para el dashboard
"""
import pygame
import math
from components.colors import *


def draw_glow_rect(surface, rect, color, glow_size=10, alpha=100):
    """Dibuja un rectángulo con efecto de glow/brillo"""
    # Crear superficie temporal con transparencia
    glow_surface = pygame.Surface((rect.width + glow_size * 2, rect.height + glow_size * 2), pygame.SRCALPHA)
    
    # Dibujar múltiples rectángulos con alpha decreciente
    for i in range(glow_size, 0, -2):
        current_alpha = int(alpha * (1 - i / glow_size))
        glow_rect = pygame.Rect(glow_size - i, glow_size - i, rect.width + i * 2, rect.height + i * 2)
        pygame.draw.rect(glow_surface, (*color, current_alpha), glow_rect, border_radius=8)
    
    # Dibujar rectángulo principal
    main_rect = pygame.Rect(glow_size, glow_size, rect.width, rect.height)
    pygame.draw.rect(glow_surface, color, main_rect, border_radius=8)
    
    # Blit en la superficie principal
    surface.blit(glow_surface, (rect.x - glow_size, rect.y - glow_size))


def draw_gradient_rect(surface, rect, color_top, color_bottom, border_radius=0):
    """Dibuja un rectángulo con gradiente vertical"""
    # Crear superficie temporal
    gradient_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    
    # Dibujar gradiente línea por línea
    for y in range(rect.height):
        # Interpolar entre los dos colores
        ratio = y / rect.height
        color = tuple(int(color_top[i] * (1 - ratio) + color_bottom[i] * ratio) for i in range(3))
        
        pygame.draw.line(gradient_surface, color, (0, y), (rect.width, y))
    
    # Aplicar border radius si es necesario
    if border_radius > 0:
        mask_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(mask_surface, (255, 255, 255, 255), mask_surface.get_rect(), border_radius=border_radius)
        gradient_surface.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    
    surface.blit(gradient_surface, (rect.x, rect.y))


def draw_neon_text(surface, text, font, pos, color, glow_size=5):
    """Dibuja texto con efecto neón"""
    # Dibujar glow
    for i in range(glow_size, 0, -1):
        alpha = int(150 * (1 - i / glow_size))
        glow_color = (*color, alpha)
        
        # Crear superficie temporal para el glow
        text_surface = font.render(text, True, color)
        glow_surface = pygame.Surface((text_surface.get_width() + i * 2, text_surface.get_height() + i * 2), pygame.SRCALPHA)
        
        # Dibujar texto con blur simulado
        for offset_x in range(-i, i + 1, 2):
            for offset_y in range(-i, i + 1, 2):
                temp_text = font.render(text, True, glow_color)
                glow_surface.blit(temp_text, (i + offset_x, i + offset_y))
        
        surface.blit(glow_surface, (pos[0] - i, pos[1] - i))
    
    # Dibujar texto principal
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)
    
    return text_surface.get_rect(topleft=pos)


def draw_scanline_effect(surface, alpha=20):
    """Dibuja efecto de líneas de escaneo tipo CRT"""
    width, height = surface.get_size()
    scanline_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    
    # Dibujar líneas horizontales
    for y in range(0, height, 4):
        pygame.draw.line(scanline_surface, (0, 0, 0, alpha), (0, y), (width, y), 2)
    
    surface.blit(scanline_surface, (0, 0))


def draw_hexagon(surface, center, size, color, width=0):
    """Dibuja un hexágono (útil para diseños futuristas)"""
    points = []
    for i in range(6):
        angle = math.pi / 3 * i
        x = center[0] + size * math.cos(angle)
        y = center[1] + size * math.sin(angle)
        points.append((x, y))
    
    pygame.draw.polygon(surface, color, points, width)


def draw_progress_arc(surface, center, radius, progress, color, width=10):
    """Dibuja un arco de progreso circular"""
    # Crear superficie temporal
    arc_surface = pygame.Surface((radius * 2 + width, radius * 2 + width), pygame.SRCALPHA)
    
    # Calcular ángulo final basado en el progreso (0-1)
    end_angle = -math.pi / 2 + (2 * math.pi * progress)
    
    # Dibujar arco usando múltiples líneas
    num_segments = int(360 * progress)
    for i in range(num_segments):
        angle1 = -math.pi / 2 + (2 * math.pi * i / 360)
        angle2 = -math.pi / 2 + (2 * math.pi * (i + 1) / 360)
        
        x1 = radius + width // 2 + radius * math.cos(angle1)
        y1 = radius + width // 2 + radius * math.sin(angle1)
        x2 = radius + width // 2 + radius * math.cos(angle2)
        y2 = radius + width // 2 + radius * math.sin(angle2)
        
        # Gradiente de color basado en el progreso
        segment_progress = i / max(num_segments, 1)
        alpha = int(255 * (0.5 + 0.5 * segment_progress))
        
        pygame.draw.line(arc_surface, (*color, alpha), (x1, y1), (x2, y2), width)
    
    # Blit en la superficie principal
    surface.blit(arc_surface, (center[0] - radius - width // 2, center[1] - radius - width // 2))


def create_pulse_effect(time_ms, speed=0.002, min_scale=0.9, max_scale=1.1):
    """Calcula un factor de escala para efecto de pulso"""
    pulse = math.sin(time_ms * speed)
    scale = min_scale + (max_scale - min_scale) * (pulse + 1) / 2
    return scale
