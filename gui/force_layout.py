from math import sqrt, log
import threading
from kivy.animation import Animation
from kivy.clock import Clock

from gui import globals
from time import sleep

c1 = 2
c2 = 150
c3 = 250
c4 = 1
M = 500

def dist(u, v):
    return sqrt((v.pos[0] - u.pos[0]) ** 2 + (v.pos[1] - u.pos[1]) ** 2)

def __calculateForces():
    # for v in graphManager.nodeWidgets:
    nodeWidgets = globals.graphManager.getNodeWidgetList()
    for v in nodeWidgets:
        v.force = [0, 0]

    for v in nodeWidgets:
        # for u in graphManager.nodeWidgets:
        for u in nodeWidgets:
            if v != u:
                d = dist(u, v)
                sinus = (v.pos[1] - u.pos[1]) / d
                cosinus = (v.pos[0] - u.pos[0]) / d

                if globals.graphManager.edgeAlreadyExists(u.nr, v.nr):
                    F = c1 * log(d / c2) # F is positive towards v

                else:
                    F = -c3 / (d ** 2)

                if globals.graphManager.isDirected:
                    F *= 2

                u.force[0] += F * cosinus
                u.force[1] += F * sinus

                v.force[0] -= F * cosinus
                v.force[1] -= F * sinus


def __moveNodes():
    # for v in graphManager.nodeWidgets:
    nodeWidgets = globals.graphManager.getNodeWidgetList()

    for v in nodeWidgets:
        nx = v.pos[0] + c4 * v.force[0]
        ny = v.pos[1] + c4 * v.force[1]

        if nx < 0:
            nx = 20

        if nx > globals.graphManager.mainViewWidget.ids.graph_canvas.size[0]:
            nx = globals.graphManager.mainViewWidget.ids.graph_canvas.size[0] - 60

        if ny < 0:
            ny = 20

        if ny > globals.graphManager.mainViewWidget.ids.graph_canvas.size[1]:
            ny = globals.graphManager.mainViewWidget.ids.graph_canvas.size[1] - 60

        v.pos[0] = nx
        v.pos[1] = ny

    edgeWidgets = globals.graphManager.getEdgeWidgetList()
    for e in edgeWidgets:
        e.updateCoords()


number = 0

def update(arg=0):
    __calculateForces()
    __moveNodes()
    globals.graphManager.update_canvas()
    global number
    number += 1
    if number >= M:
        Clock.unschedule(update)
        number = 0


def recalculatePositions():
    #globals.graphManager.randomizePositions()
    Clock.schedule_interval(update, 0.001)



