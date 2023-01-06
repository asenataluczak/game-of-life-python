from view.view import View
from model.model import Model
from controller.controller import Controller

cells_amount_x = 70
cells_amount_y = 70

view = View(cells_amount_x, cells_amount_y)
model = Model(cells_amount_x, cells_amount_y)
controller = Controller(view, model)


while controller.running:
    controller.update_cells()
    controller.update_screen()
    controller.get_user_input()   


