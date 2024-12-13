'''
This file defines a Turing Machine, then a set of states and transitions to simulate the language.
The language is represented by initial_state, final_states, accepting_states, and transition_function.
It is then simulated by putting this tuple into the Turing Machine. 
If the final state is reached, the output is printed and the grade can be found in the tape.
If the final state is not reached, the machine will hang and run forever.
This program also runs three test cases to show some of the possible outputs, and
to run more test cases the user can change the value of the input_string.
'''


class Tape(object):
    blank = "[]" ## Blank character
    def __init__(self, string=""): ## Break string into a list of the characters in alphabet
        self.tape = dict(enumerate(string.split('_')))
    
    def __str__(self): ## Return the string of the tape
        s = ""
        for char in self.tape.values():
            s += char
            s += " "
        return s
    
    def __getitem__(self, index): ## Get the character at the index
        if index in self.tape:
            return self.tape[index]
        return Tape.blank
    
    def __setitem__(self, index, value): ## Set the character at the index
        self.tape[index] = value
    
class Turing(object):
    def __init__(self, tape="", blank=" ", initial_state="", final_states=None, transition_function=None):
        self.tape = Tape(tape)
        self.head_position = 0
        self.blank = blank
        self.current_state = initial_state
        if transition_function == None:
            self.transition_function = {}
        else:
            self.transition_function = transition_function
        if final_states == None:
            self.final_states = set()
        else:
            self.final_states = set(final_states)
    
    def get_tape(self):
        return str(self.tape)
    
    def step(self):
        head_symbol = self.tape[self.head_position]
        x = (self.current_state, head_symbol)
        if x in self.transition_function:
            y = self.transition_function[x]
            self.tape[self.head_position] = y[1]
            if y[2] == "R":
                self.head_position += 1
            elif y[2] == "L":
                self.head_position -= 1
            self.current_state = y[0]
        
    def final(self):
        if self.current_state in self.final_states:
            return True
        return False


initial_state = "Start"
final_states = {"End"}
accepting_states = ["End"]
transition_function = {("Start", "B"): ("H", "B", "R"),
                        ("Start", "T"): ("H", "T", "R"),
                        
                        ("H", "Crimp"): ("H1", "1", "R"),
                        ("H", "Sloper"): ("H1", "1", "R"),
                        ("H", "Under cling"): ("H1", "1", "R"),
                        ("H", "Side cling"): ("M", "1", "R"),
                        ("H", "Pocket"): ("M", "1", "R"),
                        ("H", "Pinch"): ("M", "1", "R"),
                        ("H", "Jug"): ("M", "X", "R"),
                        ("H", "Handle"): ("M", "X", "R"),

                        ("H1", "Crimp"): ("H1", "Crimp", "R"),
                        ("H1", "Sloper"): ("H1", "Sloper", "R"),
                        ("H1", "Under cling"): ("H1", "Under cling", "R"),
                        ("H1", "Side cling"): ("H1", "Side cling", "R"),
                        ("H1", "Pocket"): ("H1", "Pocket", "R"),
                        ("H1", "Pinch"): ("H1", "Pinch", "R"),
                        ("H1", "Jug"): ("H1", "Jug", "R"),
                        ("H1", "Handle"): ("H1", "Handle", "R"),
                        ("H1", "Mantle"): ("H1", "Mantle", "R"),
                        ("H1", "Barn door"): ("H1", "Barn door", "R"),
                        ("H1", "Chimney"): ("H1", "Chimney", "R"),
                        ("H1", "Dyno"): ("H1", "Dyno", "R"),
                        ("H1", "Static"): ("H1", "Static", "R"),
                        ("H1", "Stem"): ("H1", "Stem", "R"),
                        ("H1", "Drop knee"): ("H1", "Drop knee", "R"),
                        ("H1", "Gaston"): ("H1", "Gaston", "R"),
                        ("H1", "Flag"): ("H1", "Flag", "R"),
                        ("H1", "Walk through"): ("H1", "Walk through", "R"),
                        ("H1", "Match"): ("H1", "Match", "R"),
                        ("H1", "Layback"): ("H1", "Layback", "R"),
                        ("H1", "Heel hook"): ("H1", "Heel hook", "R"),
                        ("H1", "Toe hook"): ("H1", "Toe hook", "R"),
                        ("H1", "Bicycle"): ("H1", "Bicycle", "R"),
                        ("H1", "Bump"): ("H1", "Bump", "R"),
                        ("H1", "Deadpoint"): ("H1", "Deadpoint", "R"),
                        ("H1", "Knee bar"): ("H1", "Knee bar", "R"),
                        ("H1", "1"): ("H1", "1", "R"),
                        ("H1", "[]"): ("H2", "1", "L"),

                        ("H2", "1"): ("H2", "1", "L"),
                        ("H2", "X"): ("H2", "X", "L"),
                        ("H2", "Crimp"): ("H3", "Crimp", "L"),
                        ("H2", "Sloper"): ("H3", "Sloper", "L"),
                        ("H2", "Under cling"): ("H3", "Under cling", "L"),
                        ("H2", "Side cling"): ("H3", "Side cling", "L"),
                        ("H2", "Pocket"): ("H3", "Pocket", "L"),
                        ("H2", "Pinch"): ("H3", "Pinch", "L"),
                        ("H2", "Jug"): ("H3", "Jug", "L"),
                        ("H2", "Handle"): ("H3", "Handle", "L"),
                        ("H2", "Mantle"): ("H3", "Mantle", "L"),
                        ("H2", "Barn door"): ("H3", "Barn door", "L"),
                        ("H2", "Chimney"): ("H3", "Chimney", "L"),
                        ("H2", "Dyno"): ("H3", "Dyno", "L"),
                        ("H2", "Static"): ("H3", "Static", "L"),
                        ("H2", "Stem"): ("H3", "Stem", "L"),
                        ("H2", "Drop knee"): ("H3", "Drop knee", "L"),
                        ("H2", "Gaston"): ("H3", "Gaston", "L"),
                        ("H2", "Flag"): ("H3", "Flag", "L"),
                        ("H2", "Walk through"): ("H3", "Walk through", "L"),
                        ("H2", "Match"): ("H3", "Match", "L"),
                        ("H2", "Layback"): ("H3", "Layback", "L"),
                        ("H2", "Heel hook"): ("H3", "Heel hook", "L"),
                        ("H2", "Toe hook"): ("H3", "Toe hook", "L"),
                        ("H2", "Bicycle"): ("H3", "Bicycle", "L"),
                        ("H2", "Bump"): ("H3", "Bump", "L"),
                        ("H2", "Deadpoint"): ("H3", "Deadpoint", "L"),
                        ("H2", "Knee bar"): ("H3", "Knee bar", "L"),
                        ("H2", "B"): ("E0", "B", "R"),
                        ("H2", "T"): ("E0", "T", "R"),

                        ("H3", "Crimp"): ("H3", "Crimp", "L"),
                        ("H3", "Sloper"): ("H3", "Sloper", "L"),
                        ("H3", "Under cling"): ("H3", "Under cling", "L"),
                        ("H3", "Side cling"): ("H3", "Side cling", "L"),
                        ("H3", "Pocket"): ("H3", "Pocket", "L"),
                        ("H3", "Pinch"): ("H3", "Pinch", "L"),
                        ("H3", "Jug"): ("H3", "Jug", "L"),
                        ("H3", "Handle"): ("H3", "Handle", "L"),
                        ("H3", "Mantle"): ("H3", "Mantle", "L"),
                        ("H3", "Barn door"): ("H3", "Barn door", "L"),
                        ("H3", "Chimney"): ("H3", "Chimney", "L"),
                        ("H3", "Dyno"): ("H3", "Dyno", "L"),
                        ("H3", "Static"): ("H3", "Static", "L"),
                        ("H3", "Stem"): ("H3", "Stem", "L"),
                        ("H3", "Drop knee"): ("H3", "Drop knee", "L"),
                        ("H3", "Gaston"): ("H3", "Gaston", "L"),
                        ("H3", "Flag"): ("H3", "Flag", "L"),
                        ("H3", "Walk through"): ("H3", "Walk through", "L"),
                        ("H3", "Bump"): ("H3", "Bump", "L"),
                        ("H3", "Match"): ("H3", "Match", "L"),
                        ("H3", "Layback"): ("H3", "Layback", "L"),
                        ("H3", "Heel hook"): ("H3", "Heel hook", "L"),
                        ("H3", "Toe hook"): ("H3", "Toe hook", "L"),
                        ("H3", "Bicycle"): ("H3", "Bicycle", "L"),
                        ("H3", "Deadpoint"): ("H3", "Deadpoint", "L"),
                        ("H3", "Knee bar"): ("H3", "Knee bar", "L"),
                        ("H3", "1"): ("M", "1", "R"),
                        ("H3", "B"): ("M", "B", "R"),
                        ("H3", "T"): ("M", "T", "R"),

                        ("M", "[]"): ("M", "[]", "L"),
                        ("M", "X"): ("M", "X", "L"),
                        ("M", "1"): ("M", "1", "L"),
                        ("M", "Chimney"): ("H", "1", "R"),
                        ("M", "Stem"): ("H", "1", "R"),
                        ("M", "Drop knee"): ("H", "1", "R"),
                        ("M", "Rock over"): ("H", "1", "R"),
                        ("M", "Toe hook"): ("H", "1", "R"),
                        ("M", "Static"): ("H", "X", "R"),
                        ("M", "Bump"): ("H", "X", "R"),
                        ("M", "Match"): ("H", "X", "R"),
                        ("M", "Flag"): ("H", "X", "R"),
                        ("M", "Walk through"): ("H", "X", "R"),
                        ("M", "Layback"): ("H", "X", "R"),
                        ("M", "Dyno"): ("M4", "1", "R"),
                        ("M", "Bicycle"): ("M4", "1", "R"),
                        ("M", "Mantle"): ("M1", "1", "R"),
                        ("M", "Barn door"): ("M1", "1", "R"),
                        ("M", "Gaston"): ("M1", "1", "R"),
                        ("M", "Deadpoint"): ("M1", "1", "R"),
                        ("M", "Knee bar"): ("M1", "1", "R"),
                        ("M", "Heel hook"): ("M1", "1", "R"),
                        ("M", "B"): ("E0", "B", "R"),
                        ("M", "T"): ("E0", "T", "R"),

                        ("M1", "1"): ("M1", "1", "R"),
                        ("M1", "Crimp"): ("M1", "Crimp", "R"),
                        ("M1", "Sloper"): ("M1", "Sloper", "R"),
                        ("M1", "Under cling"): ("M1", "Under cling", "R"),
                        ("M1", "Side cling"): ("M1", "Side cling", "R"),
                        ("M1", "Pocket"): ("M1", "Pocket", "R"),
                        ("M1", "Pinch"): ("M1", "Pinch", "R"),
                        ("M1", "Jug"): ("M1", "Jug", "R"),
                        ("M1", "Handle"): ("M1", "Handle", "R"),
                        ("M1", "Mantle"): ("M1", "Mantle", "R"),
                        ("M1", "Barn door"): ("M1", "Barn door", "R"),
                        ("M1", "Chimney"): ("M1", "Chimney", "R"),
                        ("M1", "Dyno"): ("M1", "Dyno", "R"),
                        ("M1", "Static"): ("M1", "Static", "R"),
                        ("M1", "Bump"): ("M1", "Bump", "R"),
                        ("M1", "Stem"): ("M1", "Stem", "R"),
                        ("M1", "Drop knee"): ("M1", "Drop knee", "R"),
                        ("M1", "Gaston"): ("M1", "Gaston", "R"),
                        ("M1", "Flag"): ("M1", "Flag", "R"),
                        ("M1", "Walk through"): ("M1", "Walk through", "R"),
                        ("M1", "Match"): ("M1", "Match", "R"),
                        ("M1", "Layback"): ("M1", "Layback", "R"),
                        ("M1", "Heel hook"): ("M1", "Heel hook", "R"),
                        ("M1", "Toe hook"): ("M1", "Toe hook", "R"),
                        ("M1", "Bicycle"): ("M1", "Bicycle", "R"),
                        ("M1", "Deadpoint"): ("M1", "Deadpoint", "R"),
                        ("M1", "Knee bar"): ("M1", "Knee bar", "R"),
                        ("M1", "[]"): ("M2", "1", "L"),

                        ("M2", "1"): ("M2", "1", "L"),
                        ("M2", "Crimp"): ("M3", "Crimp", "L"),
                        ("M2", "Sloper"): ("M3", "Sloper", "L"),
                        ("M2", "Under cling"): ("M3", "Under cling", "L"),
                        ("M2", "Side cling"): ("M3", "Side cling", "L"),
                        ("M2", "Pocket"): ("M3", "Pocket", "L"),
                        ("M2", "Pinch"): ("M3", "Pinch", "L"),
                        ("M2", "Jug"): ("M3", "Jug", "L"),
                        ("M2", "Handle"): ("M3", "Handle", "L"),
                        ("M2", "Mantle"): ("M3", "Mantle", "L"),
                        ("M2", "Barn door"): ("M3", "Barn door", "L"),
                        ("M2", "Chimney"): ("M3", "Chimney", "L"),
                        ("M2", "Dyno"): ("M3", "Dyno", "L"),
                        ("M2", "Static"): ("M3", "Static", "L"),
                        ("M2", "Stem"): ("M3", "Stem", "L"),
                        ("M2", "Drop knee"): ("M3", "Drop knee", "L"),
                        ("M2", "Gaston"): ("M3", "Gaston", "L"),
                        ("M2", "Flag"): ("M3", "Flag", "L"),
                        ("M2", "Bump"): ("M3", "Bump", "L"),
                        ("M2", "Walk through"): ("M3", "Walk through", "L"),
                        ("M2", "Match"): ("M3", "Match", "L"),
                        ("M2", "Layback"): ("M3", "Layback", "L"),
                        ("M2", "Heel hook"): ("M3", "Heel hook", "L"),
                        ("M2", "Toe hook"): ("M3", "Toe hook", "L"),
                        ("M2", "Bicycle"): ("M3", "Bicycle", "L"),
                        ("M2", "Deadpoint"): ("M3", "Deadpoint", "L"),
                        ("M2", "Knee bar"): ("M3", "Knee bar", "L"),
                        
                        ("M3", "Crimp"): ("M3", "Crimp", "L"),
                        ("M3", "Sloper"): ("M3", "Sloper", "L"),
                        ("M3", "Under cling"): ("M3", "Under cling", "L"),
                        ("M3", "Side cling"): ("M3", "Side cling", "L"),
                        ("M3", "Pocket"): ("M3", "Pocket", "L"),
                        ("M3", "Pinch"): ("M3", "Pinch", "L"),
                        ("M3", "Jug"): ("M3", "Jug", "L"),
                        ("M3", "Handle"): ("M3", "Handle", "L"),
                        ("M3", "Mantle"): ("M3", "Mantle", "L"),
                        ("M3", "Barn door"): ("M3", "Barn door", "L"),
                        ("M3", "Chimney"): ("M3", "Chimney", "L"),
                        ("M3", "Dyno"): ("M3", "Dyno", "L"),
                        ("M3", "Static"): ("M3", "Static", "L"),
                        ("M3", "Stem"): ("M3", "Stem", "L"),
                        ("M3", "Drop knee"): ("M3", "Drop knee", "L"),
                        ("M3", "Gaston"): ("M3", "Gaston", "L"),
                        ("M3", "Bump"): ("M3", "Bump", "L"),
                        ("M3", "Flag"): ("M3", "Flag", "L"),
                        ("M3", "Walk through"): ("M3", "Walk through", "L"),
                        ("M3", "Match"): ("M3", "Match", "L"),
                        ("M3", "Layback"): ("M3", "Layback", "L"),
                        ("M3", "Heel hook"): ("M3", "Heel hook", "L"),
                        ("M3", "Toe hook"): ("M3", "Toe hook", "L"),
                        ("M3", "Bicycle"): ("M3", "Bicycle", "L"),
                        ("M3", "Deadpoint"): ("M3", "Deadpoint", "L"),
                        ("M3", "Knee bar"): ("M3", "Knee bar", "L"),
                        ("M3", "1"): ("H", "1", "R"),
                        ("M3", "B"): ("H", "B", "R"),
                        ("M3", "T"): ("H", "T", "R"),

                        ("M4", "Crimp"): ("M4", "Crimp", "R"),
                        ("M4", "Sloper"): ("M4", "Sloper", "R"),
                        ("M4", "Under cling"): ("M4", "Under cling", "R"),
                        ("M4", "Side cling"): ("M4", "Side cling", "R"),
                        ("M4", "Pocket"): ("M4", "Pocket", "R"),
                        ("M4", "Pinch"): ("M4", "Pinch", "R"),
                        ("M4", "Jug"): ("M4", "Jug", "R"),
                        ("M4", "Handle"): ("M4", "Handle", "R"),
                        ("M4", "Mantle"): ("M4", "Mantle", "R"),
                        ("M4", "Barn door"): ("M4", "Barn door", "R"),
                        ("M4", "Chimney"): ("M4", "Chimney", "R"),
                        ("M4", "Dyno"): ("M4", "Dyno", "R"),
                        ("M4", "Static"): ("M4", "Static", "R"),
                        ("M4", "Stem"): ("M4", "Stem", "R"),
                        ("M4", "Drop knee"): ("M4", "Drop knee", "R"),
                        ("M4", "Gaston"): ("M4", "Gaston", "R"),
                        ("M4", "Flag"): ("M4", "Flag", "R"),
                        ("M4", "Walk through"): ("M4", "Walk through", "R"),
                        ("M4", "Match"): ("M4", "Match", "R"),
                        ("M4", "Bump"): ("M4", "Bump", "R"),
                        ("M4", "Layback"): ("M4", "Layback", "R"),
                        ("M4", "Heel hook"): ("M4", "Heel hook", "R"),
                        ("M4", "Toe hook"): ("M4", "Toe hook", "R"),
                        ("M4", "Bicycle"): ("M4", "Bicycle", "R"),
                        ("M4", "Deadpoint"): ("M4", "Deadpoint", "R"),
                        ("M4", "Knee bar"): ("M4", "Knee bar", "R"),
                        ("M4", "1"): ("M4", "1", "R"),
                        ("M4", "[]"): ("M5", "1", "R"),

                        ("M5", "[]"): ("M2", "1", "L"),


                        ("E0", "1"): ("E0", "1", "R"),
                        ("E0", "X"): ("E1", "X", "R"),
                        ("E0", "[]"): ("E4", "[]", "L"),

                        ("E1", "X"): ("E1", "X", "R"),
                        ("E1", "1"): ("E2", "X", "L"),
                        ("E1", "[]"): ("E4", "[]", "L"),

                        ("E2", "X"): ("E2", "X", "L"),
                        ("E2", "1"): ("E3", "1", "R"),
                        ("E2", "B"): ("E3", "B", "R"),
                        ("E2", "T"): ("E3", "T", "R"),

                        ("E3", "X"): ("E0", "1", "R"),

                        ("E4", "X"): ("E4", "[]", "L"),
                        ("E4", "1"): ("E4", "1", "L"),
                        ("E4", "B"): ("q0", "[]", "R"),
                        ("E4", "T"): ("p0", "[]", "R"),

                        ("q0", "1"): ("q1", "[]", "R"),
                        ("q0", "X"): ("q3", "1", "R"),
                        ("q0", "[]"): ("T1", "[]", "L"),

                        ("q1", "1"): ("q1", "1", "R"),
                        ("q1", "X"): ("q2", "X", "L"),
                        ("q1", "[]"): ("q2", "[]", "L"),

                        ("q2", "[]"): ("q3", "[]", "R"),
                        ("q2", "1"): ("q4", "X", "L"),

                        ("q3", "X"): ("q3", "1", "R"),
                        ("q3", "[]"): ("T1", "[]", "L"),

                        ("q4", "1"): ("q4", "1", "L"),
                        ("q4", "[]"): ("q0", "[]", "R"),

                        ("T1", "1"): ("T1", "1", "L"),
                        ("T1", "[]"): ("V0", "[]", "R"),


                        ("p0", "1"): ("p1", "[]", "R"),
                        ("p0", "X"): ("p5", "1", "R"),
                        ("p0", "[]"): ("T2", "[]", "L"),

                        ("p1", "1"): ("p2", "[]", "R"),
                        ("p1", "X"): ("p4", "X", "L"),
                        ("p1", "[]"): ("p4", "[]", "L"),

                        ("p2", "1"): ("p3", "[]", "R"),
                        ("p2", "X"): ("p4", "X", "L"),
                        ("p2", "[]"): ("p4", "[]", "L"),

                        ("p3", "1"): ("p3", "1", "R"),
                        ("p3", "X"): ("p4", "X", "L"),
                        ("p3", "[]"): ("p4", "[]", "L"),

                        ("p4", "[]"): ("p5", "[]", "R"),
                        ("p4", "1"): ("p6", "X", "L"),

                        ("p5", "X"): ("p5", "1", "R"),
                        ("p5", "[]"): ("T2", "[]", "L"),

                        ("p6", "1"): ("p6", "1", "L"),
                        ("p6", "[]"): ("p0", "[]", "R"),

                        ("T2", "1"): ("T2", "1", "L"),
                        ("T2", "[]"): ("5.6", "[]", "R"),


                        ("V0", "1"): ("V1", "[]", "R"),
                        ("V1", "1"): ("V2", "[]", "R"),
                        ("V2", "1"): ("V3", "[]", "R"),
                        ("V3", "1"): ("V4", "[]", "R"),
                        ("V4", "1"): ("V5", "[]", "R"),
                        ("V5", "1"): ("V6", "[]", "R"),
                        ("V6", "1"): ("V7", "[]", "R"),
                        ("V7", "1"): ("V8", "[]", "R"),
                        ("V8", "1"): ("V9", "[]", "R"),
                        ("V9", "1"): ("V10", "[]", "R"),
                        ("V10", "1"): ("V10", "[]", "R"),
                        ("V0", "[]"): ("End", "V0", "R"),
                        ("V1", "[]"): ("End", "V1", "R"),
                        ("V2", "[]"): ("End", "V2", "R"),
                        ("V3", "[]"): ("End", "V3", "R"),
                        ("V4", "[]"): ("End", "V4", "R"),
                        ("V5", "[]"): ("End", "V5", "R"),
                        ("V6", "[]"): ("End", "V6", "R"),
                        ("V7", "[]"): ("End", "V7", "R"),
                        ("V8", "[]"): ("End", "V8", "R"),
                        ("V9", "[]"): ("End", "V9", "R"),
                        ("V10", "[]"): ("End", "V10+", "R"),

                        ("5.6", "1"): ("5.7", "[]", "R"),
                        ("5.7", "1"): ("5.8", "[]", "R"),
                        ("5.8", "1"): ("5.9", "[]", "R"),
                        ("5.9", "1"): ("5.10", "[]", "R"),
                        ("5.10", "1"): ("5.11", "[]", "R"),
                        ("5.11", "1"): ("5.12", "[]", "R"),
                        ("5.12", "1"): ("5.13", "[]", "R"),
                        ("5.13", "1"): ("5.14", "[]", "R"),
                        ("5.14", "1"): ("5.14", "[]", "R"),
                        ("5.6", "[]"): ("End", "5.6", "R"),
                        ("5.7", "[]"): ("End", "5.7", "R"),
                        ("5.8", "[]"): ("End", "5.8", "R"),
                        ("5.9", "[]"): ("End", "5.9", "R"),
                        ("5.10", "[]"): ("End", "5.10", "R"),
                        ("5.11", "[]"): ("End", "5.11", "R"),
                        ("5.12", "[]"): ("End", "5.12", "R"),
                        ("5.13", "[]"): ("End", "5.13", "R"),
                        ("5.14", "[]"): ("End", "5.14+", "R")

}

data_structure = ("Some input string", "[]", initial_state, final_states, transition_function)

def main():
    ## Define input string, create turing machine, run the machine.
    
    input = "B_Crimp_Dyno_Handle_Gaston_Pinch"
    turing = Turing(input, "[]", initial_state, final_states, transition_function)

    print("Input: ", turing.get_tape())

    while not turing.final():
        turing.step()
    print("State: ", turing.current_state)
    print("Output: ", turing.get_tape())

    input = "T_Crimp_Dyno_Handle_Gaston_Pinch_Static_Pocket_Gaston_Sloper_Gaston_Sloper_Bump_Crimp_Deadpoint_Handle"
    turing = Turing(input, "[]", initial_state, final_states, transition_function)
    print("Input: ", turing.get_tape())

    while not turing.final():
        turing.step()
    print("State: ", turing.current_state)
    print("Output: ", turing.get_tape())

    input = "B_Crimp_Dyno_Handle_Gaston_Pinch_Static_Handle_Dyno_Sloper" ## Feel free to change to test more cases
    turing = Turing(input, "[]", initial_state, final_states, transition_function)
    print("Input: ", turing.get_tape())

    while not turing.final():
        turing.step()
        ##print("State: ", turing.current_state) ## Uncomment to see the state at each step
        ##print("Output: ", turing.get_tape()) ## Uncomment to see the tape at each step
    print("State: ", turing.current_state)
    print("Output: ", turing.get_tape())

if __name__ == "__main__":
    main()