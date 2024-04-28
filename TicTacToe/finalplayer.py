import math
import random


class Player(): #base class 
    def __init__(self, letter): #initiate: constructor
        self.letter = letter #instance variable

    def get_move(self, game):  #get move :placeholder hayt3amalaha implement taht fel subclasses
        pass #law fi ay error bey3melo avoid


class HumanPlayer(Player): #subclass 1
    def __init__(self, letter):
        super().__init__(letter)#calls parent class

    def get_move(self, game):  #over-rides el function el fel parent class
        valid_square = False #flag that indicates whether el move valid or not
        val = None #will store the valid move made by the player
        while not valid_square: #loop btfdal shghala le had ma el player ydakhal valid move
            square = input(self.letter + '\'s turn. Input move (0-9): ') 
            try:
                val = int(square) #law el user b3t non-integer value el try bt7awel te converto le int law m3rfsh haytala3 error
                if val not in game.available_moves():
                    raise ValueError #el except btmsk el error dah w bttsrf fih
                valid_square = True #ttla3 bara el loop
            except ValueError:
                print('Invalid square. Try again.')
        return val #hatraga3 el valid move


class SmartPlayer(Player): #subclass 2
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game): 
        if len(game.available_moves()) == 9: #el board fadya mahadsh bada2 le3b
            square = random.choice(game.available_moves()) #random move
        else:
            square = self.minimax(game, self.letter)['position']#el position hoa key f dictionary el birg3o el minimax, btraga3 el optimal position el gebnah mn el minimax
        return square

    def minimax(self, state, player): #state heya el state of the game
        max_player = self.letter  # el ai w hayeb2a X
        other_player = 'O' if player == 'X' else 'X' #if(player==X)=> other_player=O else => other_player=X  ai=X fa e7na el O

        #bn explore all possible moves and their outcomes
        # check if the previous move is a winner lel human player
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares()) if other_player == max_player else -1 * (state.num_empty_squares())} #for max player: +1 ya3ny biksab , -1 bikhsar , 0 draw
        elif not state.empty_squares(): # check for draw
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  #should maximize
        else:
            best = {'position': None, 'score': math.inf}  #should minimize
        for possible_move in state.available_moves(): #haymshy 3alla kol el possible moves el mwgoda fel board
            state.make_move(possible_move, player) #hena hano3od ngrb el move bta3t el Smartplayer TEMPORARILY  
            sim_score = self.minimax(state, other_player)  # han-explore el tree lel possible choices lama negarab law el smartplayer 3ml el move dih fa el human player momkn y3ml eh w nehseb el score le had ma negib el optimal move lel SmartPlayer

            # baraga3 kol haga zai el awal 3shan el next move
            state.board[possible_move] = ' ' #braga3 el temporary move ely el smartplayer 3amalha
            state.current_winner = None #bnrg3 lel original state 
            sim_score['position'] = possible_move  

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:  #lel max player biakhod a3la score
                    best = sim_score
            else:
                if sim_score['score'] < best['score']: #lel min biakhod a2al score
                    best = sim_score
        return best