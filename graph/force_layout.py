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
c2 = 200
c3 = 250
c4 = 1
M = 500

grabbed_node = 0

def dist(u, v):
    return sqrt((v.pos[0] - u.pos[0]) ** 2 + (v.pos[1] - u.pos[1]) ** 2)

def __calculateForces():

    node_widgets = globals.graph_manager.getNodeWidgetList()
    for v in node_widgets:
        v.force = [0, 0]

    for v in node_widgets:

        for u in node_widgets:
            if v != u:
                d = dist(u, v)
                sine = (v.pos[1] - u.pos[1]) / d
                cosine = (v.pos[0] - u.pos[0]) / d

                if globals.graph_manager.edgeAlreadyExists(int(u.Id), int(v.Id)):
                    F = c1 * log(d / c2) # F is positive towards v

                else:
                    F = -c3 / (d ** 2)

                if globals.graph_manager.is_directed or u.Id == grabbed_node or v.Id == grabbed_node: # ?
                    F *= 2

                if u.Id != grabbed_node:
                    u.force[0] += F * cosine
                    u.force[1] += F * sine

                if v.Id != grabbed_node:
                    v.force[0] -= F * cosine
                    v.force[1] -= F * sine


def __moveNodes():

    node_widgets = globals.graph_manager.getNodeWidgetList()

    for v in node_widgets:
        nx = v.pos[0] + c4 * v.force[0]
        ny = v.pos[1] + c4 * v.force[1]

        if nx < 5:
            nx = 5

        if nx > globals.main_view_widget.ids.graph_canvas.size[0] - globals.node_radius * 2 - 5:
            nx = globals.main_view_widget.ids.graph_canvas.size[0] - globals.node_radius * 2 - 5

        if ny < 5:
            ny = 5

        if ny > globals.main_view_widget.ids.graph_canvas.size[1] - globals.node_radius * 2 - 5:
            ny = globals.main_view_widget.ids.graph_canvas.size[1] - globals.node_radius * 2 - 5

        v.pos[0] = nx
        v.pos[1] = ny

    edge_widgets = globals.graph_manager.getEdgeWidgetList()
    for e in edge_widgets:
        e.updateCoords()


number = 0

def update(arg=0):
    __calculateForces()
    __moveNodes()

    global number
    number += 1
    if number >= M:
        Clock.unschedule(update)
        number = 0
        global grabbed_node
        grabbed_node = 0


def recalculatePositions(gn=0):
    global grabbed_node
    grabbed_node = gn
    Clock.schedule_interval(update, 0.0005)



