from settings import WINDOW_RESOLUTION
from voxel.engine import Engine


if __name__ == "__main__":
    game = Engine(WINDOW_RESOLUTION.to_tuple())
    game.run()
