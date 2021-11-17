while True:
    answer = input("Enter something, q to quit outer: ")
    if answer == "q":
        break

    while True:
        next_answer = input("Enter something else, q to quit inner: ")
        if next_answer == "q":
            break
        else:
            # rest of loop...
            continue
    break  # if i want to break out of both; otherwise delete line
