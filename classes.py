import pygame as pg

from constants import *


class Area:
    def __init__(self) -> None:
        self.width, self.height = LIMIT_AREA

        self.left = (WIN_SIZE[0] - self.width + PX_SIZE) / 2 // PX_SIZE * PX_SIZE
        self.top = (WIN_SIZE[1] - self.height - self.left) // PX_SIZE * PX_SIZE
        self.right = self.left + self.width
        self.bottom = self.top + self.height


class LimitedArea(Area):
    def __init__(self) -> None:
        Area.__init__(self)

        self.border = 1
        self.color = MARKS

    def wall_collision(self, pos: int) -> bool:
        if self.top + 5 < pos < self.bottom - 5:
            return False
        return True

    def goal(self, pos: int) -> bool:
        if self.left < pos < self.right:
            return False
        return True


class Player(Area):
    def __init__(self, player: int) -> None:
        Area.__init__(self)

        self.player_width = PX_SIZE
        self.player_height = PX_SIZE * 4

        self.player = player

        if self.player == 1:
            self.pos = (
                self.left + PX_SIZE,
                (self.top + self.height / 2) - (self.player_height / 2)
            )
        else:
            self.pos = (
                self.right - (2 * PX_SIZE),
                (self.top + self.height / 2) - (self.player_height / 2)
            )

        self.player_top = self.pos[1]
        self.player_bottom = self.pos[1] + self.player_height
        self.player_left = self.pos[0]
        self.player_right = self.pos[0] + self.player_width

        self.surface = pg.Surface((self.player_width, self.player_height))
        self.surface.fill(OBJ_COLOR)

    def define_hitbox(self) -> None:
        self.player_top = self.pos[1]
        self.player_bottom = self.pos[1] + self.player_height
        self.player_left = self.pos[0]
        self.player_right = self.pos[0] + self.player_width

    def go_up(self) -> None:
        self.pos = (self.pos[0], self.pos[1] - MOVEMENT / 4)

        self.define_hitbox()

    def go_down(self) -> None:
        self.pos = (self.pos[0], self.pos[1] + MOVEMENT / 4)

        self.define_hitbox()

    def defend(self, ball_pos: tuple) -> bool:
        if self.player == 1:
            if self.player_right - 4 < ball_pos[0] < self.player_right + 4 and \
                self.player_bottom > ball_pos[1] and \
                self.player_top < ball_pos[1] + PX_SIZE:
                return True

        elif self.player == 2:
            if self.player_left + 4 > ball_pos[0] + PX_SIZE > self.player_left - 4 and \
                self.player_bottom > ball_pos[1] and \
                self.player_top < ball_pos[1] + PX_SIZE:
                return True

        return False

    def defend_direction(self, ball_pos: tuple) -> str:
        if (self.player_bottom + self.player_top) / 2 < ball_pos[1] + PX_SIZE / 2:
            return 'down'
        return 'up'

    def regenerate(self) -> None:
        if self.player == 1:
            self.pos = (
                self.left + PX_SIZE,
                (self.top + self.height / 2) - (self.player_height / 2)
            )
        else:
            self.pos = (
                self.right - (2 * PX_SIZE),
                (self.top + self.height / 2) - (self.player_height / 2)
            )

        self.define_hitbox()


class Ball(Area):
    def __init__(self) -> None:
        Area.__init__(self)

        self.diameter = PX_SIZE

        self.pos = (
            (WIN_SIZE[0] - self.diameter) / 2,
            (self.top + self.height / 2) - (self.diameter / 2)
        )
        self.surface = pg.Surface((self.diameter, self.diameter))
        self.surface.fill(OBJ_COLOR)

        self.x_speed = self.y_speed = MOVEMENT ** 0.5

        self.x_direction = 'left'
        self.y_direction = ''
    
    def move(self) -> None:
        match f'{self.x_direction}_{self.y_direction}':
            case 'left_up':
                self.pos = (self.pos[0] - self.x_speed, self.pos[1] - self.y_speed)
            case 'left_down':
                self.pos = (self.pos[0] - self.x_speed, self.pos[1] + self.y_speed)
            case 'left_':
                self.pos = (self.pos[0] - self.x_speed, self.pos[1])
            case 'right_up':
                self.pos = (self.pos[0] + self.x_speed, self.pos[1] - self.y_speed)
            case 'right_down':
                self.pos = (self.pos[0] + self.x_speed, self.pos[1] + self.y_speed)
            case 'right_':
                self.pos = (self.pos[0] + self.x_speed, self.pos[1])

    def regenerate(self, serve=1) -> None:
        self.pos = (
            (WIN_SIZE[0] - self.diameter) / 2,
            (self.top + self.height / 2) - (self.diameter / 2)
        )

        if serve == 1:
            self.x_direction = 'right'
            self.y_direction = ''
        else:
            self.x_direction = 'left'
            self.y_direction = ''


class Score:
    def __init__(self) -> None:
        self.value = 0
    
    def add(self) -> None: self.value += 1

    def reset(self) -> None: self.value = 0