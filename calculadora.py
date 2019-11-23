# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:40:29 2019

@author: Luan
"""
def operacoes_disponiveis():
    return {'1':'Adicao','2':'Subtracao','3':'Divisao','4':'Multiplicacao'}
    #return {'1': adicao(),'2':subtracao(),'3':'Divisao','4':'Multiplicacao'}

def adicao(numero1,numero2):
    return numero1+numero2

def subtracao(numero1,numero2):
    return numero1-numero2

def divisao(numero1,numero2):
    return numero1/numero2

def multiplicacao(numero1,numero2):
    return numero1*numero2

def opcoes():
    operacoes = operacoes_disponiveis()
    for index,operacao in operacoes.items():
        print("{} - {}".format(index,operacao))
             
def operacoes(numero_operacao,numero1,numero2):
    resultado = 0
    if(int(numero_operacao) == 1):
        resultado = adicao(numero1,numero2)
    elif(int(numero_operacao) == 2): 
        resultado = subtracao(numero1,numero2)
    elif(int(numero_operacao) == 3):     
         resultado = divisao(numero1,numero2)
    elif(int(numero_operacao) == 4):
        resultado = multiplicacao(numero1,numero2)
        
    return resultado 

def verifica_operacao(numero_operacao):
    operacoes = operacoes_disponiveis()
    resposta = False
    for index in operacoes:
        if int(numero_operacao) == int(index) :
            resposta = True
            break
        else:
            resposta = False
    return resposta         

try:
    print('Bem vindo a calculadora em python')
    opcoes()
    op = -1
    while(op!=0):
        op = int(input('Informe o numero da operação que deseja realizar : '))
        if verifica_operacao(op):
            n1 = float(input('numero : '))
            n2 = float(input('numero : '))
            print('resultado da operacao {} '.format(operacoes(op,n1,n2)))
        else:
            print('opcao invalida')
except:
    print('por favor entre apenas com numeros inteiros')
    
