def transition_function(current_state, curTapeSym):
    if current_state == "q1" and curTapeSym == "a":
        return ("q2", curTapeSym, "R")
    elif current_state == "q2":
        if curTapeSym == "b":
            return ("q2", curTapeSym, "R")
        elif curTapeSym == "c":
            return ("q3", curTapeSym, "L")
    elif current_state == "q3":
        if curTapeSym in ["a", "b", "c"]:
            return ("q3", curTapeSym, "L")
        else:
            return ("q4", "_", "R")
    return None

def run_tm(input_string):
    tape = list(input_string + "_")
    head = 0
    state = "q1"
    while state != "q4":
        result = transition_function(state, tape[head])
        if result is None:
            return False
        state, tape[head], direction = result
        head += 1 if direction == "R" else -1
    return True

input_string = "an bn cn"
if run_tm(input_string):
    print(f"{input_string} is accepted")
else:
    print(f"{input_string} is rejected")
