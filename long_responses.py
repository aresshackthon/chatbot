# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:34:18 2022

@author: user
"""

import random

R_EATING = "Which product do you have a question about? 1)VermiGold Tonic 2)Compost Worms 3)Fishing Worms 4)VermiGold Pellets"
R_ADVICE = "Can I keep fishing worms alive for my next fishing trip"


def unknown():
    response = ["Say Hi",
                "Say Hello",
                "Say Hey",
                "What does that mean?Say Hello"][
        random.randrange(4)]
    return response
        
        
        
        
        