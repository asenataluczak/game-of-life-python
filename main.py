import numpy
from view.view import View
from model.model import Model

cells_amount_x = 70
cells_amount_y = 70

view = View(cells_amount_x, cells_amount_y)
model = Model(cells_amount_x, cells_amount_y)

view.draw_cells(model.grid, numpy.ndindex(model.grid.shape))

updating = False
running = True
while running:
    view.update_screen()
    mouse = view.get_mouse_position()

    for event in view.get_event():
        if event.type == view.get_event_type('QUIT'):
            running = False
        if event.type == view.get_event_type('MOUSEBUTTONDOWN'):
            if view.buttonPlayPause.collide(mouse):
                updating = not updating
                view.buttonPlayPause.switch(view.get_surface(), updating)
                view.buttonRefresh.disableEnable(view.get_surface(), updating)
                view.buttonNext.disableEnable(view.get_surface(), updating)
            if view.buttonRefresh.collide(mouse) and not updating:
                model.set_initial_position()
                view.draw_cells(model.grid, numpy.ndindex(model.grid.shape))
            if view.buttonNext.collide(mouse) and not updating:
                model.update()
                view.draw_cells(model.grid, numpy.ndindex(model.grid.shape))

    if updating:
        model.update()
        view.draw_cells(model.grid, numpy.ndindex(model.grid.shape))
        
quit()


