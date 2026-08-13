from pathlib import Path

from PIL import Image, ImageDraw

WIDTH, HEIGHT = 800, 240
FRAME_DURATION_MS = 120
NODES = [(120, 120), (280, 64), (400, 172), (540, 78), (680, 130)]
EDGES = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]

frames = []
for index in range(24):
    active = index % len(NODES)
    image = Image.new('RGB', (WIDTH, HEIGHT), '#0d1117')
    draw = ImageDraw.Draw(image)
    for left, right in EDGES:
        color = '#3fb950' if active in (left, right) else '#58a6ff'
        draw.line((NODES[left], NODES[right]), fill=color, width=3)
    for node_index, point in enumerate(NODES):
        color = '#3fb950' if node_index == active else '#58a6ff'
        draw.ellipse((point[0] - 12, point[1] - 12, point[0] + 12, point[1] + 12), fill=color)
    frames.append(image)

output = Path('assets/collaboration-network.gif')
output.parent.mkdir(exist_ok=True)
frames[0].save(output, save_all=True, append_images=frames[1:], loop=0, duration=FRAME_DURATION_MS, disposal=2, optimize=True)
