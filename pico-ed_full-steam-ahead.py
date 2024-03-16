import board
from ringbit import *
from picoed import *

ringbit = Ringbit(board.P1, board.P2)
display.show(Image(
        '00000000000000000:'
        '00000000000000000:'
        '00001100000110000:'
        '00010010001001000:'
        '00100001010000100:'
        '00000000000000000:'
        '00000000000000000:'
    ))

while True:
    if  button_a.is_pressed and button_b.is_pressed():
        ringbit.set_speed(0, 0)
    if button_a.is_pressed():
        ringbit.set_speed(100, 100)
    if button_b.is_pressed():
        ringbit.set_speed(-100, -100)

        