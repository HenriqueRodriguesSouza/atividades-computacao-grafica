import glfw
from OpenGL.GL import *
import numpy as np

def create_scale_matrix(sx, sy):
    return np.array([
        [sx, 0,  0, 0],
        [0,  sy, 0, 0],
        [0,  0,  1, 0],
        [0,  0,  0, 1]
    ], dtype=np.float32)

glfw.init()
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
window = glfw.create_window(800, 600, "Escala com matriz", None, None)
glfw.make_context_current(window)

x_scale, y_scale = 1.0, 1.0
scale_step = 0.01

while not glfw.window_should_close(window):
    glfw.poll_events()

    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        x_scale += scale_step
    if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
        x_scale = max(0.01, x_scale - scale_step)
    if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
        y_scale += scale_step
    if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
        y_scale = max(0.01, y_scale - scale_step)
    
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    scale_matrix = create_scale_matrix(x_scale, y_scale)
    glLoadMatrixf(scale_matrix.T)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.5)
    glEnd()

    glfw.swap_buffers(window)

glfw.terminate()