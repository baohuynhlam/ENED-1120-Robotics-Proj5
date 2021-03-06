"""
Main program 1 to run ENED simulation
Robot traverse entire area without picking up box
while also avoid obstacles and update IPS info
"""

from myconstants import BARCODE, HOME
from mysimulator import Simulator

if __name__ == "__main__":
    target_barode = [1, 1, 1, 1]  # Invalid barcode
    start_pos = HOME[0]

    game = Simulator(start_pos, target_barode)

    game.frontend.render_background(game.backend.box_list, game.backend.rock_list)
    game.frontend.render_surface(game.backend.robot)

    game.search_entire_area()
    