from ast import Not
import os
from time import sleep
import sys

class Board:
    def __init__(self):
        self.cells = [["", "", ""],["", "", ""],["", "", ""]]
    def fill_board(self):
        for i in range(3):
            for j in range(3):
                print(f"  {self.cells[i][j]} ", end = "")
                if j != 2:
                    print("|" ,end = "")
            if i != 2:
                print("\n--------------")

class Player:
    def __init__(self):
        self.win = False
        self.move = [0, 0]
        self.row_container = [0, 0, 0]
        self.column_container = [0, 0, 0]
        self.diagonal_container = 0
        self.opposite_diagonal_container = 0
        self.win = False
    def check_win_case(self):
        for i in self.row_container:
            if i == 3:
                self.win = True
        for i in self.column_container:
            if i == 3:
                self.win = True
        if self.diagonal_container == 3:
                self.win = True
            
        if self.opposite_diagonal_container == 3:
                self.win = True
    def make_a_move(self, step):
        if step == 1:
            real_step = [0, 0]
            self.row_container[0] += 1
            self.column_container[0] += 1
            self.diagonal_container += 1
        if step == 2:
            real_step = [0, 1]
            self.row_container[0] += 1
            self.column_container[1] += 1
        if step == 3:
            real_step = [0, 2]
            self.row_container[0] += 1
            self.column_container[2] += 1
            self.opposite_diagonal_container += 1
        if step == 4:
            real_step = [1, 0]
            self.row_container[1] += 1
            self.column_container[0] += 1
        if step == 5:
            real_step = [1, 1]
            self.row_container[1] += 1
            self.column_container[1] += 1
            self.opposite_diagonal_container += 1
            self.diagonal_container += 1
        if step == 6:
            real_step = [1, 2]
            self.row_container[1] += 1
            self.column_container[2] += 1
        if step == 7:
            real_step = [2, 0]
            self.row_container[2] += 1
            self.column_container[0] += 1
            self.opposite_diagonal_container += 1
        if step == 8:
            real_step = [2, 1]
            self.row_container[2] += 1
            self.column_container[1] += 1
        if step == 9:
            real_step = [2, 2]
            self.row_container[2] += 1
            self.column_container[2] += 1
            self.diagonal_container += 1
        self.move = real_step

class Main:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.board = Board()
    def get_x_input(self):
        step = int(input("\nX, Your turn: "))
        main.player1.make_a_move(step)
        self.board.cells[self.player1.move[0]] [self.player1.move[1]] = "X"
    def get_o_input(self):
        step = int(input("\nO, Your turn: "))
        main.player2.make_a_move(step)
        self.board.cells[self.player2.move[0]] [self.player2.move[1]] = "O"
        
   
    def show_step(self):
        self.board.fill_board()

    def check_draw_case(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board.cells[i][j] == "X" or self.board.cells[i][j] == "O":
                    count += 1
        if count == 9:
            print("\nGame Over. Tie!")
            sys.exit()
        
        
main = Main()

while True: 
    main.show_step()
    main.player1.check_win_case()
    main.player2.check_win_case()
    if main.player1.win == True:
            print("\nPlayer 1 won!")
            sys.exit()
    if main.player2.win == True:
            print("\nPlayer 2 won!")
            sys.exit()
    main.check_draw_case()
    main.get_x_input()
    sleep(0.05)
    os.system('cls')
    main.show_step()
    main.player1.check_win_case()
    main.player2.check_win_case()
    if main.player1.win == True:
            print("\nPlayer 1 won!")
            sys.exit()
    if main.player2.win == True:
            print("\nPlayer 2 won!")
            sys.exit()
    main.check_draw_case()
    main.get_o_input()
    sleep(0.05)
    os.system('cls')