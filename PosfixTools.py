# -*- coding: utf-8 -*-
"""

Autores: Martínez Márquez Héctor
         Rosasles Valdez Edna
         Bustamante Cruz Horacio

Analisis de Algoritmos 3CV4

https://en.wikipedia.org/wiki/Shunting-yard_algorithm
https://rosettacode.org/wiki/Parsing/Shunting-yard_algorithm#Python
https://www.youtube.com/watch?v=qN8LPIcY6K4
https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/
@author: Lacho
"""
import numpy as np
from collections import namedtuple
from pprint import pprint as pp
 
OpInfo = namedtuple('OpInfo', 'prec assoc')
L, R = 'Left Right'.split()
 
ops = {
    '+': OpInfo(prec=2, assoc=L),
    '-': OpInfo(prec=2, assoc=L),
    '*': OpInfo(prec=3, assoc=L),
    '/': OpInfo(prec=3, assoc=L),
    '^': OpInfo(prec=4, assoc=R),
    'ln': OpInfo(prec=3, assoc=R),
    'log': OpInfo(prec=3, assoc=R),
    'sin': OpInfo(prec=3, assoc=R),
    'cos': OpInfo(prec=3, assoc=R),
    'floor': OpInfo(prec=3, assoc=R),
    'ceil': OpInfo(prec=3, assoc=R),
    '(': OpInfo(prec=9, assoc=L),
    ')': OpInfo(prec=0, assoc=L),
}
 
NUM, LPAREN, RPAREN = 'NUMBER ( )'.split()
SEP = ','
VAR = 'n'
 
 
def get_input(inp = None):
    'Inputs an expression and returns list of (TOKENTYPE, tokenvalue)'
 
    if inp is None:
        inp = input('expression: ')
    tokens = inp.strip().split()
    tokenvals = [] 
    for token in tokens:
        if token in ops:
            tokenvals.append((token, ops[token]))
        #elif token in (LPAREN, RPAREN):
        #    tokenvals.append((token, token))
        elif token is SEP:
            tokenvals.append((SEP, token))
        else:    
            tokenvals.append((NUM, token))
    return tokenvals
 
def shunting(tokenvals):
    outq, stack = [], []
    table = ['TOKEN,ACTION,RPN OUTPUT,OP STACK,NOTES'.split(',')]
    for token, val in tokenvals:
        note = action = ''
        if token is NUM:
            action = 'Add number to output'
            outq.append(val)
            table.append( (val, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
        elif token in ops:
            t1, (p1, a1) = token, val
            v = t1
            note = 'Pop ops from stack to output' 
            while stack:
                t2, (p2, a2) = stack[-1]
                if (a1 == L and p1 <= p2) or (a1 == R and p1 < p2):
                    if t1 != RPAREN:
                        if t2 != LPAREN:
                            stack.pop()
                            action = '(Pop op)'
                            outq.append(t2)
                        else:    
                            break
                    else:        
                        if t2 != LPAREN:
                            stack.pop()
                            action = '(Pop op)'
                            outq.append(t2)
                        else:    
                            stack.pop()
                            action = '(Pop & discard "(")'
                            table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
                            break
                    table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
                    v = note = ''
                else:
                    note = ''
                    break
                note = '' 
            note = '' 
            if t1 != RPAREN:
                stack.append((token, val))
                action = 'Push op token to stack'
            else:
                action = 'Discard ")"'
            table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
        elif token is SEP:
            action = 'Ignore'
            table.append( (val, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
    note = 'Drain stack to output'
    while stack:
        v = ''
        t2, (p2, a2) = stack[-1]
        action = '(Pop op)'
        stack.pop()
        outq.append(t2)
        table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
        v = note = ''
    return table

def printPosfix(psfxStack):
    maxcolwidths = [len(max(x, key=len)) for x in zip(*psfxStack)]
    row = psfxStack[0]
    print( ' '.join('{cell:^{width}}'.format(width=width, cell=cell) for (width, cell) in zip(maxcolwidths, row)))
    for row in psfxStack[1:]:
        print( ' '.join('{cell:<{width}}'.format(width=width, cell=cell) for (width, cell) in zip(maxcolwidths, row)))
    print('\n The final output RPN is: %r' % psfxStack[-1][2])

def getPosfixString(psfxStack):
    return str(psfxStack[-1][2])

class evalpostfix: 
    def __init__(self, min, max, step): 
        self.stack =[] 
        self.top =-1
        self.n = np.arange(min, max, step)
    def pop(self): 
        if self.top ==-1: 
            return
        else: 
            self.top-= 1
            return self.stack.pop() 
    def push(self, i): 
        self.top+= 1
        self.stack.append(i) 
        # print('Push:{}\n'.format(i))
  
    def centralfunc(self, posfix): 
        tokens = posfix.split(' ')
        for token in tokens: 
            # print('Token:{}\n'.format(token))
            if token in ops:
                val1 = self.pop() 
                
                if(token == "+"):
                    val2 = self.pop()
                    valArray = np.add(val2,val1)
                elif(token == "-"):
                    val2 = self.pop()
                    valArray = np.subtract(val2,val1)
                elif(token == "*"):
                    val2 = self.pop()
                    valArray = np.multiply(val2,val1)
                elif(token == "/"):
                    val2 = self.pop()
                    valArray = np.true_divide(val2,val1)
                elif(token == "^"):
                    val2 = self.pop()
                    valArray = np.power(val2,val1)
                elif(token == "ln"):
                    valArray = np.log(val1)
                elif(token == "log"):
                    val2 = self.pop()
                    valArray = np.log(val2) / np.log(val1)
                elif(token == "sin"):
                    valArray = np.sin(val1)
                elif(token == "cos"):
                    valArray = np.sin(val1)
                elif(token == "floor"):
                    valArray = np.floor(val1)
                elif(token == "ceil"):
                    valArray = np.ceil(val1)
                else:
                    print('Invalid Operator: {}\n'.format(token))
                    return
                # print('valArray:{}\n'.format(valArray))
                self.push(valArray) 
            elif token is VAR:
                self.push(self.n) 
            else: 
                if(token == "π" or token == "pi"):
                    val1 = np.pi
                elif(token == "γ" or token == "gamma"):
                    val1 = np.euler_gamma
                elif(token == "e" or token == "euler"):
                    val1 = np.e
                else:
                    val1 = float(token)
                
                valArray = np.full(self.n.size, val1)
                self.push(valArray)
        # return self.pop().astype(int)
        return self.pop()