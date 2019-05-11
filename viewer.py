from OpenGL.GLUT import *


class Viewer(object):
    def __init__(self):
        """ Initialize the viewer. """
        self.init_interface()
        # self.init_opengl()
        # self.init_scene()Î
        # self.init_interaction()
        # init_primitives()

    def init_interface(self):
        """ initialize the window and register the render function """
        glutInit()
        glutInitWindowSize(640, 480)
        glutCreateWindow("3D Modeler")
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutDisplayFunc(self.render)

    def render(self):
        pass

    def main_loop(self):
        glutMainLoop()


if __name__ == "__main__":
    viewer = Viewer()
    viewer.main_loop()
