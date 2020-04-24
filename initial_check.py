import sys
import random
import numpy as np

allowed_commands = ["F", "B", "R", "U", "L", "D", "F'", "B'", "R'", "U'", "L'", "D'", "F2", "B2", "R2", "U2", "L2",
                        "D2"];

def randomize_mix(s) :
    s = s.strip();
    if len(s) < 1 or s.isdigit() == False :
        print("Error: amount of moves is not a valid argument");
        exit();
    moves_amount = int(s);
    if moves_amount > 20 or moves_amount < 1:
        print("Error: amount of moves must be 0 < x < 21");
        exit();

    i = 0;
    commands = np.array([]);
    while i < moves_amount :
        commands = np.append(commands, random.choice(allowed_commands));
        i += 1;

    print("Random mix:\t\t", commands);
    print("Estimated time: ", (15 ** moves_amount) / 10000.0, "s");
    return (commands);

def initial_check() :
    if (len(sys.argv) != 2) :
        print("Error: provide exactly one parameter");
        exit();

    if (len(sys.argv[1]) < 1) :
        print("Error: argument is too short");
        exit();

    if (sys.argv[1][0:6].lower() == "random") :
        if len(sys.argv[1]) < 8 :
            print("Error: can't randomize without number of moves");
        return (randomize_mix(sys.argv[1][6:]));

    for i in sys.argv[1] :
        allowed = False;
        for j in "FBRLUD' 2":
            if (i == j) :
                allowed = True;
                break;
        if (allowed == False) :
            print("Error: character '" + i + "' from argument is not allowed");
            exit();

    commands = np.array(sys.argv[1].split());

    for i in commands :
        if (len(i) > 2) :
            print("Error: operation '" + i + "' is not allowed");
            exit();
        allowed = False;
        for j in allowed_commands :
            if (i == j) :
                allowed = True;
                break;
        if (allowed == False) :
            print("Error: operation '" + i + "' is not allowed");
            exit();
    return (commands);