import numpy


class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.updating = False
        self.running = True
        self.mouse = None
        self.view.draw_cells(model.grid, numpy.ndindex(model.grid.shape))

    def update_screen(self):
        self.view.update_screen()
        self.mouse = self.view.get_mouse_position()

    def update_cells(self):
        if self.updating:
            self.model.update()
            self.view.draw_cells(self.model.grid, numpy.ndindex(self.model.grid.shape))

    def get_user_input(self):
        for event in self.view.get_event():
            self.__handle_user_quit(event)
            self.__handle_user_click(event)

    def __handle_user_quit(self, event):
        if event.type == self.view.get_event_type('QUIT'):
            self.__quit()
            self.running = False

    def __handle_user_click(self, event):
        if event.type == self.view.get_event_type('MOUSEBUTTONDOWN'):
            if self.view.buttonPlayPause.collide(self.mouse):
                self.updating = not self.updating
                self.view.buttonPlayPause.switch(self.view.get_surface(), self.updating)
                self.view.buttonRefresh.disable_enable(self.view.get_surface(), self.updating)
                self.view.buttonNext.disable_enable(self.view.get_surface(), self.updating)
            if self.view.buttonRefresh.collide(self.mouse) and not self.updating:
                self.model.set_initial_position()
                self.view.draw_cells(self.model.grid, numpy.ndindex(self.model.grid.shape))
            if self.view.buttonNext.collide(self.mouse) and not self.updating:
                self.model.update()
                self.view.draw_cells(self.model.grid, numpy.ndindex(self.model.grid.shape))

    def __quit(self):
        self.view.quit()
