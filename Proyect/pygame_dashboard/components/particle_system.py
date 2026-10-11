"""
Sistema de partículas para efectos de fondo animados
"""
import pygame
import random
import math
from components.colors import *


class Particle:
    """Partícula individual con movimiento y efectos visuales"""
    
    def __init__(self, x, y, color=None, size=None, speed=None):
        self.x = x
        self.y = y
        self.color = color or random.choice(GRAPH_COLORS)
        self.size = size or random.uniform(1, 4)
        self.speed = speed or random.uniform(0.2, 1.5)
        self.angle = random.uniform(0, 2 * math.pi)
        self.alpha = random.randint(50, 200)
        self.life = random.uniform(0.5, 1.0)
        self.max_life = self.life
        self.pulse_speed = random.uniform(0.02, 0.05)
        self.pulse_offset = random.uniform(0, 2 * math.pi)
        
    def update(self, dt, width, height):
        """Actualiza la posición y estado de la partícula"""
        # Movimiento flotante
        self.x += math.cos(self.angle) * self.speed * dt
        self.y += math.sin(self.angle) * self.speed * dt
        
        # Efecto de pulso
        pulse = math.sin(pygame.time.get_ticks() * self.pulse_speed + self.pulse_offset)
        self.current_size = self.size * (0.8 + 0.2 * pulse)
        
        # Wrap around screen
        if self.x < 0:
            self.x = width
        elif self.x > width:
            self.x = 0
        if self.y < 0:
            self.y = height
        elif self.y > height:
            self.y = 0
            
        # Actualizar vida
        self.life -= 0.001 * dt
        if self.life <= 0:
            self.life = self.max_life
            
    def draw(self, surface):
        """Dibuja la partícula con efecto de glow"""
        # Calcular alpha basado en la vida
        current_alpha = int(self.alpha * (self.life / self.max_life))
        
        # Crear superficie con transparencia
        particle_surface = pygame.Surface((int(self.current_size * 4), int(self.current_size * 4)), pygame.SRCALPHA)
        
        # Dibujar glow (círculos concéntricos)
        for i in range(3):
            alpha = current_alpha // (i + 1)
            size = self.current_size * (3 - i)
            color = (*self.color, alpha)
            center = (int(self.current_size * 2), int(self.current_size * 2))
            pygame.draw.circle(particle_surface, color, center, int(size))
        
        # Blit en la superficie principal
        surface.blit(particle_surface, (int(self.x - self.current_size * 2), int(self.y - self.current_size * 2)))


class ParticleSystem:
    """Sistema que gestiona múltiples partículas"""
    
    def __init__(self, width, height, num_particles=100):
        self.width = width
        self.height = height
        self.particles = []
        
        # Crear partículas iniciales
        for _ in range(num_particles):
            x = random.uniform(0, width)
            y = random.uniform(0, height)
            self.particles.append(Particle(x, y))
    
    def update(self, dt):
        """Actualiza todas las partículas"""
        for particle in self.particles:
            particle.update(dt, self.width, self.height)
    
    def draw(self, surface):
        """Dibuja todas las partículas"""
        for particle in self.particles:
            particle.draw(surface)
    
    def add_burst(self, x, y, count=20, color=None):
        """Añade una explosión de partículas en una posición"""
        for _ in range(count):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 5)
            particle = Particle(x, y, color=color, size=random.uniform(2, 5), speed=speed)
            particle.angle = angle
            self.particles.append(particle)
        
        # Limitar número de partículas
        if len(self.particles) > 300:
            self.particles = self.particles[-300:]


class ConnectionLines:
    """Dibuja líneas conectando partículas cercanas"""
    
    def __init__(self, particle_system, max_distance=150):
        self.particle_system = particle_system
        self.max_distance = max_distance
    
    def draw(self, surface):
        """Dibuja líneas entre partículas cercanas"""
        particles = self.particle_system.particles
        
        for i, p1 in enumerate(particles):
            for p2 in particles[i+1:]:
                dx = p1.x - p2.x
                dy = p1.y - p2.y
                distance = math.sqrt(dx*dx + dy*dy)
                
                if distance < self.max_distance:
                    # Calcular alpha basado en la distancia
                    alpha = int(100 * (1 - distance / self.max_distance))
                    
                    # Crear superficie para la línea
                    line_surface = pygame.Surface((abs(int(dx)) + 2, abs(int(dy)) + 2), pygame.SRCALPHA)
                    
                    # Color de la línea (mezcla de los colores de las partículas)
                    color = tuple((c1 + c2) // 2 for c1, c2 in zip(p1.color, p2.color))
                    
                    start_pos = (0 if dx > 0 else abs(int(dx)), 0 if dy > 0 else abs(int(dy)))
                    end_pos = (abs(int(dx)) if dx > 0 else 0, abs(int(dy)) if dy > 0 else 0)
                    
                    pygame.draw.line(line_surface, (*color, alpha), start_pos, end_pos, 1)
                    
                    blit_x = min(p1.x, p2.x)
                    blit_y = min(p1.y, p2.y)
                    surface.blit(line_surface, (int(blit_x), int(blit_y)))
