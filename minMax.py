# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:42:25 2018

@author: Team Alpha0
"""

from numpy import inf
import chess


def tourMax(board,profondeur,boolean):
    if (profondeur==0):
        b=board.fen()
        return [utility(b,boolean),0]
    profondeur = profondeur-1
    u=-inf
    coup=None
    listeCoupsPossible=board.legal_moves
    for l in listeCoupsPossible:
        copyOfBoard=board.copy()
        copyOfBoard.push(l)
        utiliteTour=tourMin(copyOfBoard,profondeur,boolean)[0]
        if utiliteTour>u :
            coup=l
            u=utiliteTour
    return [u,coup]


#==========================================================================================================


def tourMin(board,profondeur,boolean):
    if (profondeur==0):
        b=board.fen()
        return [utility(b,boolean),0]
    profondeur=profondeur-1
    coup=None
    u=inf
    listeCoupsPossible=board.legal_moves
    for l in listeCoupsPossible:
        copyOfBoard=board.copy()
        copyOfBoard.push(l)
        utiliteTour=tourMax(copyOfBoard,profondeur,boolean)[0]
        if utiliteTour<u :
            coup=l
            u=utiliteTour
    return [u,coup]

#==========================================================================================================

def MinMax(board,profondeur,boolean):
    return tourMax(board, profondeur,boolean)


#===========================================================================================================

def utility(liste,boolean):
    sumNoir=0
    sumBlanc=0
    i=0
    while liste[i]!=' ':
        if liste [i]=='p':
            sumNoir+=1
            i+=1
        elif liste[i]=='n' or liste[i]=='b' or liste[i]=='r' :
            sumNoir+=3
            i+=1
        elif liste [i]=='q':
            sumNoir+=9
            i+=1
        elif liste [i]=='P':
            sumBlanc+=1
            i+=1
        elif liste[i]=='N' or liste[i]=='B' or liste[i]=='R' :
            sumBlanc+=3
            i+=1
        elif liste [i]=='Q':
            sumBlanc+=9
            i+=1
        else:
            i+=1
    if boolean == True :
        return sumBlanc-sumNoir
    return sumNoir-sumBlanc
