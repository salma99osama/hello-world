
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,30)
    gluLookAt(8,9,10,
              0,0,0,
              0,1,0)
    glClearColor(1,1,1,1)
    glMatrixMode(GL_MODELVIEW)


x = 0
theta=0
forward= True
def draw():
    global x
    global theta
    global forward
    glClearColor(0,1,0,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(.5,.5,.5)
    glScale(17,2,3)
    glutSolidCube(3)
    glLoadIdentity()

    glColor3f(1,1,1)
    glScale(2.7,0.1,0.45)
    glutSolidCube(2)
    glLoadIdentity()

    glTranslate(10, 0, 0)
    glScale(2.7, 0.1, .45)
    glutSolidCube(2)
    glLoadIdentity()

    glTranslate(-13, 0, 0)
    glScale(2.7, 0.1, .45)
    glutSolidCube(2)
    glLoadIdentity()

    glColor3f(0,0,0)
    glTranslate(0,5.5,0)
    glScale(.2,1.2,.2)
    glutSolidCube(1)
    glLoadIdentity()

    glTranslate(0,6.65,0)
    glScale(.8,1.1,.3)
    glutSolidCube(1)
    glLoadIdentity()

    glEnable(GL_BLEND)

    glColor4f(.5,.5,.5,1)
    glTranslate(0,7,0)
    glutSolidSphere(.1,150,150)
    glLoadIdentity()

    glColor4f(.5,.5,.5,0)
    glTranslate(0, 6.7, 0)
    glutSolidSphere(.1, 200, 200)
    glLoadIdentity()

    glColor4f(0,1,0,.8)
    glTranslate(0, 6.4, 0)
    glutSolidSphere(.1, 200, 200)
    glLoadIdentity()


    glColor3f(.7,0,1)
    glTranslate(x,0,0)
    glScalef(4,1,2)
    glutSolidCube(1)
    glLoadIdentity()

    glTranslate(x, 1, 0)
    glScalef(2, 1, 2)
    glutSolidCube(1)
    glLoadIdentity()

    glColor3f(0,0,0)
    glTranslate(x, 0, 0)
    glScalef(4, 1, 2)
    glutWireCube(1)
    glLoadIdentity()

    glTranslate(x, 1, 0)
    glScalef(2, 1, 2)
    glutWireCube(1)
    glLoadIdentity()




    glColor3f(0,0,0)
    glTranslate(x+2,-0.5,-1)
    glRotate(theta,0,0,-1)
    glutWireTorus(0.15,0.35,10,12)
    glLoadIdentity()


    glTranslate(x-2, -0.5, -1)
    glRotate(theta,0,0,-1)
    glutWireTorus(0.15, 0.35, 10, 12)
    glLoadIdentity()

    glTranslate(x+2, -0.5, 1)
    glRotate(theta,0,0,-1)
    glutWireTorus(0.15, 0.35, 10, 12)
    glLoadIdentity()

    glTranslate(x-2, -0.5, 1)
    glRotate(theta,0,0,-1)
    glutWireTorus(0.15, 0.35, 10, 12)

    glutSwapBuffers()

    if forward:
        x = x + 0.01
        theta = theta + 1
    else:
        x = x - 0.01
        theta = theta - 1
    if x > 6:
        forward = False
    elif x < -14:
        forward = True


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()




