#!/usr/bin/python3
""" method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """""funcion to return boolean whether box is opened or not"""
    unlocked = [0]
    for key in unlocked:
        for box in boxes[key]:
            if box not in unlocked and box < len(boxes):
                unlocked.append(box)
    return len(unlocked) == len(boxes)
