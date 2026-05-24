import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#lienpt udpate

# Tạo figure và axes
fig, ax = plt.subplots(figsize=(10, 6))

# Cấu hình biểu đồ
ax.set_xlim(0, 10)
ax.set_ylim(-3, 3)

ax.set_title("DNA Replication Simulation")
ax.set_xlabel("DNA Length")
ax.set_ylabel("Position")

# Trục x
x = np.linspace(0, 10, 500)

# Sóng DNA
phase = np.linspace(0, 6 * np.pi, len(x))

# Các line
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)

line3, = ax.plot([], [], '--', lw=2)
line4, = ax.plot([], [], '--', lw=2)

text = ax.text(0.5, 2.5, '', fontsize=12)

# Khởi tạo
def init():
    line1.set_data([], [])
    line2.set_data([], [])

    line3.set_data([], [])
    line4.set_data([], [])

    return line1, line2, line3, line4, text

# Animation update
def update(frame):

    separation = frame / 25

    y1 = np.sin(phase) + separation
    y2 = -np.sin(phase) - separation

    # DNA gốc
    line1.set_data(x, y1)
    line2.set_data(x, y2)

    # DNA mới
    new_y1 = y1 + 0.3
    new_y2 = y2 - 0.3

    line3.set_data(x, new_y1)
    line4.set_data(x, new_y2)

    text.set_text(f"Replication step: {frame}")

    return line1, line2, line3, line4, text

# Tạo animation
ani = FuncAnimation(
    fig,
    update,
    frames=40,
    init_func=init,
    interval=120,
    blit=True
)

plt.show()