def minToHours(minutes,seconds):
    hours=minutes/60
    seconds=seconds/3600
    convert=hours,seconds
    return convert
print(minToHours(80,56))