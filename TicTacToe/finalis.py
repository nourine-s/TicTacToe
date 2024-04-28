import math
import time
from finalplayer import HumanPlayer,SmartPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod #bt belong lel class badal ma teb2a instance meno la2enaha msh bt-depend 3alla el state bta3t ay instance 3shan te3mel el board mn el init() w msh btakhod self 
    def make_board():
        return [' ' for i in range(9)]#returns a list of 9 empty spaces

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:#bt3ml matrix 3x3
            print('| ' + ' | '.join(row) + ' |') #bt print shakl el board 

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |') #bt print el matrix bel index

    def make_move(self, square, letter): #square:index
        if self.board[square] == ' ':
            self.board[square] = letter #bey check law el square el ana dkhlto fady fa bihot el letter fel mkan dah
            if self.winner(square, letter): #ba3d ma bn3ml move bey-check law hoa winner walla la
                self.current_winner = letter
            return True
        return False #law dah invalid move aslun

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]#bt extracts el values el goa el index el bigebo mn el row_ind
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3 #check columns
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0: #check diagonlas
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self): #returns true law fih 3al a2al 1 square fady
        return ' ' in self.board

    def num_empty_squares(self):#returns 3adad el empty squares
        return self.board.count(' ')

    def available_moves(self):#returns a list of indeces benesba lel positions el fadya 
        return [i for i, x in enumerate(self.board) if x == " "]#el enumerate bt-iterate 3alla el elements el fel self.board bel index bta3hom btraga3(index,element)


def play(game, x_player, o_player, print_game=True):

    if print_game:#law b true hatedkhol fel condition
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():#el game tkamel law lesa fih empty squares
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()

            if game.current_winner:#bey-check law had kasab
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)#ba3mel delay ben kol move 3shan matb2ash sari3a awy aw bate2a awy

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':  #creates instances mn el smartplayer, humanplayer and t w call
    x_player =SmartPlayer('X')
    o_player =HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)