from .game import Playterm
def play():
    from curses import wrapper
    speed = 0.1
    points = 1
    player_xy = None
    for level in range(1, 10):
        playterm = Playterm(points=int(round(points)), speed=speed, player_xy=player_xy)
        wrapper(playterm.show)
        player_xy = playterm.player_xy
        speed = speed/7 * 3
        points = points*1.40