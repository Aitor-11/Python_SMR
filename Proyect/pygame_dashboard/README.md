# Game Dashboard - Pygame

Un dashboard interactivo tipo videojuego creado con Pygame, con efectos visuales impresionantes, sistema de partículas y widgets animados.

## Características

- 🎨 **Efectos visuales tipo cyberpunk** con colores neón y glow
- ✨ **Sistema de partículas animadas** con líneas de conexión
- 📊 **Widgets interactivos**: tarjetas de estadísticas, barras de progreso, medidores circulares, gráficos
- 🎮 **Animaciones fluidas** y efectos hover
- 🖱️ **Interactividad completa** con mouse y teclado

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

## Controles

- **SPACE** - Randomizar valores
- **R** - Resetear valores
- **ESC** - Salir
- **Mouse** - Interactuar con widgets (hover sobre elementos)
- **Click** - Presionar botones

## Estructura del Proyecto

```
pygame_dashboard/
├── main.py                 # Archivo principal
├── requirements.txt        # Dependencias
└── components/            # Componentes reutilizables
    ├── __init__.py
    ├── colors.py          # Paleta de colores
    ├── particle_system.py # Sistema de partículas
    ├── effects.py         # Efectos visuales
    └── widgets.py         # Widgets del dashboard
```

## Widgets Disponibles

- **StatCard**: Tarjetas de estadísticas con valores animados
- **ProgressBar**: Barras de progreso con gradientes
- **CircularMeter**: Medidores circulares tipo RPG
- **LineGraph**: Gráficos de líneas animados
- **Button**: Botones interactivos con efectos

## Personalización

Puedes personalizar los colores editando `components/colors.py` o añadir nuevos widgets en `components/widgets.py`.
