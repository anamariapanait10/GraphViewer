from math import sqrt, log

from kivy.animation import Animation

from gui import globals
from time import sleep

c1 = 1
c2 = 50
c3 = 50
c4 = 0.4
M = 100


def __calculateForces():
    # for v in graphManager.nodeWidgets:
    nodeWidgets = globals.graphManager.getNodeWidgetList()
    for v in nodeWidgets:
        fx = 0
        fy = 0
        # for u in graphManager.nodeWidgets:
        for u in nodeWidgets:
            if v != u:
                if v.pos[0] == u.pos[0]:
                    u.pos[0] += 10
                fx += c3 / ((v.pos[0] - u.pos[0]) ** 2)
                fx += c1 * log(abs((v.pos[0] - u.pos[0]) / c2))

                if v.pos[1] == u.pos[1]:
                    u.pos[1] += 10
                fy += c3 / ((v.pos[1] - u.pos[1]) ** 2)
                fy += c1 * log(abs((v.pos[1] - u.pos[1]) / c2))

        v.force = (fx, fy)


def __moveNodes():
    # for v in graphManager.nodeWidgets:
    nodeWidgets = globals.graphManager.getNodeWidgetList()

    for v in nodeWidgets:
        nx = v.pos[0] + c4 * v.force[0]
        ny = v.pos[1] + c4 * v.force[1]

        if nx > globals.graphManager.mainViewWidget.ids.graph_canvas.size[0]:
            nx = globals.graphManager.mainViewWidget.ids.graph_canvas.size[0] - 60

        if ny > globals.graphManager.mainViewWidget.ids.graph_canvas.size[1]:
            ny = globals.graphManager.mainViewWidget.ids.graph_canvas.size[1] - 60

        v.pos[0] = nx
        v.pos[1] = ny

    edgeWidgets = globals.graphManager.getEdgeWidgetList()
    for e in edgeWidgets:
        e.updateCoords()


def __update():
    __calculateForces()
    __moveNodes()


def recalculatePositions():
    for t in range(M):
        __update()


