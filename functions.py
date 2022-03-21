import pygame as pg
from pygame import quit as pg_quit
from pygame.mixer import music
from pygame.locals import *

from classes import LimitedArea, Ball, Player, Score
from constants import *

pg.init()

FONT = pg.font.Font(STANDARD_FONT, FONT_SIZE)
FONT2 = pg.font.Font(STANDARD_FONT, FONT_SIZE2)


area = LimitedArea()
ball = Ball()
player1 = Player(1)
player2 = Player(2)
score1 = Score()
score2 = Score()


def exit_game() -> None:
    pg_quit()
    quit()

def restart():
    ball.regenerate()
    player1.regenerate()
    player2.regenerate()
    score1.reset()
    score2.reset()

    run()

def run(win: object):
    player1_moving_up = False
    player1_moving_down = False
    player2_moving_up = False
    player2_moving_down = False

    while score1.value < 10 and score2.value < 10:
        # loop constants
        pg.time.Clock().tick(300)
        win.fill(BACKGROUND_COLOR)


        # event detection
        for event in pg.event.get():
            if event.type == QUIT: exit_game()

            if event.type == KEYDOWN:
                if event.key == K_q or event.key == K_ESCAPE: exit_game()

                if event.key == K_w: player1_moving_up = True
                if event.key == K_s: player1_moving_down = True

                if event.key == K_UP: player2_moving_up = True
                if event.key == K_DOWN: player2_moving_down = True

            if event.type == KEYUP:
                if event.key == K_w: player1_moving_up = False
                if event.key == K_s: player1_moving_down = False

                if event.key == K_UP: player2_moving_up = False
                if event.key == K_DOWN: player2_moving_down = False


        # collisions detection
        if player1.player_top <= area.top + PX_SIZE:
            player1_moving_up = False
        elif player1.player_bottom >= area.bottom - PX_SIZE:
            player1_moving_down = False

        if player2.player_top <= area.top + PX_SIZE:
            player2_moving_up = False
        elif player2.player_bottom >= area.bottom - PX_SIZE:
            player2_moving_down = False

        if area.wall_collision(ball.pos[1]):
            ball.y_direction = 'down'
            music.load(r'.\sounds\wall.wav')
            music.play(0)
        elif area.wall_collision(ball.pos[1] + ball.diameter):
            ball.y_direction = 'up'
            music.load(r'.\sounds\wall.wav')
            music.play(0)
        elif area.goal(ball.pos[0]):
            score2.add()
            music.load(r'.\sounds\goal.wav')
            music.play(0)
            pg.display.update()
            ball.regenerate(2)
            continue
        elif area.goal(ball.pos[0] + ball.diameter):
            score1.add()
            music.load(r'.\sounds\goal.wav')
            music.play(0)
            pg.display.update()
            ball.regenerate(1)
            continue

        if player1.defend(ball.pos):
            ball.y_direction = player1.defend_direction(ball.pos)
            ball.x_direction = 'right'
            music.load(r'.\sounds\defend.wav')
            music.play(0)
        elif player2.defend(ball.pos):
            ball.y_direction = player2.defend_direction(ball.pos)
            ball.x_direction = 'left'
            music.load(r'.\sounds\defend.wav')
            music.play(0)


        # moving stuff
        if player1_moving_up: player1.go_up()
        if player1_moving_down: player1.go_down()
        if player2_moving_up: player2.go_up()
        if player2_moving_down: player2.go_down()

        ball.move()


        # draw objects
        pg.draw.rect(
            win,
            area.color,
            pg.Rect(
                area.left,
                area.top,
                area.width,
                area.height
            ),
            area.border,
            PX_SIZE
        )

        pg.draw.aaline(win, MARKS, (WIN_SIZE[0] / 2, area.top), (WIN_SIZE[0] / 2, area.bottom))

        win.blit(ball.surface, ball.pos)

        win.blit(player1.surface, player1.pos)
        win.blit(player2.surface, player2.pos)


        # text render
        player1_score_text = FONT.render(
            f'{score1.value}',
            True,
            OBJ_COLOR
        )
        player1_text_rect = player1_score_text.get_rect()
        player1_text_rect.left = area.right * 1/4 + area.left
        player1_text_rect.top = area.left
        win.blit(player1_score_text, player1_text_rect)

        player2_score_text = FONT.render(
            f'{score2.value}',
            True,
            OBJ_COLOR
        )
        player2_text_rect = player2_score_text.get_rect()
        player2_text_rect.right = area.right * 3/4
        player2_text_rect.top = area.left
        win.blit(player2_score_text, player2_text_rect)

        pg.display.update()

    while 1:
        for event in pg.event.get():
            if event.type == QUIT: exit_game()

            if event.type == KEYDOWN:
                if event.key == K_q or event.key == K_ESCAPE: exit_game()
                if event.key == K_r: restart()

        end1_text = FONT.render(
            f'Game Over! The score is:',
            True,
            OBJ_COLOR
        )
        end1_text_rect = end1_text.get_rect()
        end1_text_rect.center = (WIN_SIZE[0] / 2, WIN_SIZE[1] / 2 - FONT_SIZE)
        win.blit(end1_text, end1_text_rect)

        end2_text = FONT.render(
            f'{score1.value} x {score2.value}',
            True,
            OBJ_COLOR
        )
        end2_text_rect = end2_text.get_rect()
        end2_text_rect.center = (WIN_SIZE[0] / 2, WIN_SIZE[1] / 2)
        win.blit(end2_text, end2_text_rect)

        end3_text = FONT2.render(
            f'press "r" to restart or "q" to quit',
            True,
            OBJ_COLOR
        )
        end3_text_rect = end3_text.get_rect()
        end3_text_rect.center = (WIN_SIZE[0] / 2, WIN_SIZE[1] / 2 + FONT_SIZE * 2)
        win.blit(end3_text, end3_text_rect)

        pg.display.update()