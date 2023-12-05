#!/usr/bin/python3
""" method that determines if all the boxes can be opened"""
def canUnlockAll(boxes):
    """""funcion to return boolean whether box is opened or not"""
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys:
                keys.append(box)
    return len(keys) == len(boxes)
