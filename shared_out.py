# payoffs1 = [[[[c(5),c(20)],[c(20),c(5)]],[[c(5),c(20)],[c(20),c(5)]]],[[[c(20),c(5)],[c(5),c(20)]],[[c(20),c(5)],[c(5),c(20)]]]]
# payoffs2 = [[[[c(20),c(5)],[c(5),c(20)]],[[c(20),c(5)],[c(5),c(20)]]],[[[c(20),c(5)],[c(5),c(20)]],[[c(20),c(5)],[c(5),c(20)]]]]
payoffs1 = [
    [[[5,20],[20,5]],[[5,20],[20,5]]],
    [[[20,5],[5,20]],[[20,5],[5,20]]],
    [[[20,5],[5,5]],[[5,5],[5,20]]]
]
payoffs2 = [
    [[[20,5],[5,20]],[[20,5],[5,20]]],
    [[[20,5],[5,20]],[[20,5],[5,20]]],
    [[[20,5],[5,5]],[[5,5],[5,20]]]
]
description = tuple([
    "P1 earns $20 if P1 and P2 choose different colours, and earns $5 if P1 and P2 choose the same colour.",
    "P2 earns $20 if P1 and P2 choose the same colour, and earns $5 if P1 and P2 choose different colours.",
    "P1 earns $20 if P1 and P2 choose the same colour, and earns $5 if P1 and P2 choose different colours.",
    "P2 earns $20 if P1 and P2 choose the same colour, and earns $5 if P1 and P2 choose different colours.",
    "P1 earns $20 if P1, P2 and the computer all choose the same colour. Otherwise, P1 earns $5.",
    "P2 earns $20 if P1, P2 and the computer all choose the same colour. Otherwise, P2 earns $5."])
game_type = tuple([
    "P1 and P2 Task",
    "P1 and P2 Task",
    "P1, P2 and Computer Task",
    "P1, P2 and Computer Task"]) 