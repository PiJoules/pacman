#! /usr/bin/env python
# -*- coding: utf-8 -*-

from level import Level

class Level001(Level):
    """Level 1 of the PyMan Game"""

    def getLayout(self):
        return [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1 ,0, 1, 1, 1, 0, 1, 1, 0, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1 ,1, 1, 0, 1, 0, 1, 1, 0, 1, 9],\
                [9, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 ,0, 0, 0, 1, 0, 0, 0, 0, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 0, 0, 7, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 3, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 1, 4, 5, 6, 1, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 9],\
                [9, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1, 9],\
                [9, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 9],\
                [9, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 9],\
                [9, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]]

