def transition_function(current_state,curTapeSym):
    if current_state == "q1":
        if curTapeSym == "a":
            return ("q2", curTapeSym, "R")
    elif current_state == "q2":
        if curTapeSym == "b":
            return ("q3", curTapeSym, "R")
    elif current_state == "q3":
        if curTapeSym == "c":
            return ("q4", curTapeSym, "R")
    elif current_state == "q4":
        if curTapeSym == "b":
            return ("q5", curTapeSym, "L")
    elif current_state == "q5":
        if curTapeSym in ["a","b","c"]:
            return (current_state, curTapeSym, "L")
        else:
            return (current_state, "_", "L")
    return None

def run_tm(input_string):
    tape = list(input_string+"_")
    head = 0
    state = "q1"
    while state!="q5":
        result = transition_function(state,tape[head])
        if result is None:
            return False
        state, tape[head], direction = result
        if direction == "R":
            head +=1
        elif direction == "L":
            head -=1
    return True

input_string = "aabbcc"
if run_tm(input_string):
    print(f"{input_string} is accepted")
else:
    print(f"{input_string} is rejected")