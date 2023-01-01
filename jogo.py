from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=2)


def update():
    player.x += held_keys['d']  * time.dt
    player.x -= held_keys['a']  * time.dt
    player.y += held_keys['w']  * time.dt
    player.y -= held_keys['s']  * time.dt

app.run()
