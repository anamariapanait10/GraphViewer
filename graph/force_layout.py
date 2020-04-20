"""
    In the following code implements the algorithm of Eades, which targets graphs with up to 30 vertices and uses a
mechanical model to produce “aesthetically pleasing” 2D layouts for plotters and CRT screens. The algorithm is 
succinctly summarized as follows:
    To embed a graph we replace the vertices by steel rings and replace each edge with a spring to form a mechanical 
system. The vertices are placed in some initial layout and let go so that the spring forces on the rings move the system
to a minimal energy state. Two practical adjustments are made to this idea: firstly, logarithmic strength springs are 
used; that is, the force exerted by a spring is:
                                             c1 ∗ log(d/c2),
where d is the length of the spring, and c1 and c2 are constants. Experience shows that Hookes Law (linear) springs are 
too strong when the vertices are far apart; the logarithmic force solves this problem. Note that the springs exert no
force when d = c2. Secondly, we make nonadjacent vertices repel each other. An inverse square law force,
                                             c3/d2,
where c3 is constant and d is the distance between the vertices, is suitable. The mechanical system is simulated by the 
following algorithm:
                                    algorithm SPRING(G:graph);
                                    place vertices of G in random locations;
                                    repeat M times
                                        calculate the force on each vertex;
                                        move the vertex c4 ∗ (force on vertex)
                                    draw graph on CRT or plotter.
    The values c1 = 2, c2 = 1, c3 = 1, c4 = 0.1, are appropriate for most graphs. Almost all graphs achieve a minimal 
energy state after the simulation step is run 100 times, that is, M = 100.

"""

from math import sqrt, log
from kivy.clock import Clock
from globals import globals


c1 = 2
c2 = 150
c3 = 250
c4 = 1
M = 500

def dist(u, v):
    return sqrt((v.pos[0] - u.pos[0]) ** 2 + (v.pos[1] - u.pos[1]) ** 2)

def __calculateForces():

    nodeWidgets = globals.graphManager.getNodeWidgetList()
    for v in nodeWidgets:
        v.force = [0, 0]

    for v in nodeWidgets:

        for u in nodeWidgets:
            if v != u:
                d = dist(u, v)
                sinus = (v.pos[1] - u.pos[1]) / d
                cosinus = (v.pos[0] - u.pos[0]) / d

                if globals.graphManager.edgeAlreadyExists(int(u.Id), int(v.Id)):
                    F = c1 * log(d / c2) # F is positive towards v

                else:
                    F = -c3 / (d ** 2)

                if globals.graphManager.isDirected: # ?
                    F *= 2

                u.force[0] += F * cosinus
                u.force[1] += F * sinus

                v.force[0] -= F * cosinus
                v.force[1] -= F * sinus


def __moveNodes():

    nodeWidgets = globals.graphManager.getNodeWidgetList()

    for v in nodeWidgets:
        nx = v.pos[0] + c4 * v.force[0]
        ny = v.pos[1] + c4 * v.force[1]

        if nx < 0:
            nx = 20

        if nx > globals.mainViewWidget.ids.graph_canvas.size[0]:
            nx = globals.mainViewWidget.ids.graph_canvas.size[0] - 60

        if ny < 0:
            ny = 20

        if ny > globals.mainViewWidget.ids.graph_canvas.size[1]:
            ny = globals.mainViewWidget.ids.graph_canvas.size[1] - 60

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



