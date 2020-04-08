def fibGen():
    trailing,lead=0,1
    while True:
        yield lead
        trailing,lead=lead,trailing+lead