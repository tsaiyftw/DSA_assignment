# reference
# https://python-course.eu/applications-python/towers-of-hanoi.php
def move(n, source, temp, target):
    global stepCount
    print("move ( ", n, source, temp, target, " called")
    if n >= 1:
        # move tower of size -1 to temp
        print("move#1")
        move(n - 1, source, target, temp)
        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            stepCount += 1
            print("StepCount:{}".format(stepCount))
            print("Move disk {}: {} --> {}".format(disk, source[1], target[1]))
            target[0].append(disk)
        # move tower of size n-1 size from temp to target
        print("move#2")
        move(n - 1, temp, source, target)


source = ([7, 6, 5, 4, 3, 2, 1], "source")
target = ([], "target")
temp = ([], "temp")
stepCount = 0
move(len(source[0]), source, temp, target)
