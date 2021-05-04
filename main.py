# KBC PROGRAM

print("\t\t\t*********************WELCOME*********************")
print("\t\t\t*****************TO VIRTUAL KBC******************")
print("\t\t\t*************KAUN BANEGA CROREPATI***************")
print("\t\t\t*************I AM YOUR HOST AND DOST*************")
print("\t\t\t**************VIRTUAL ANSHU GUPTA****************")

name = input("\t\t\tENTER YOUR NAME-->")
import DETAILS as d
d
while True:
    START = input("\t\t\tTO START THE GAME PRESS CAPITAL\'S\'")
    if START == "S":
        print("\t\t\t*************************************************")
        break
    else:
        print("\t\t\t*************************************************")
        print("\t\t\tTRY AGAIN")
        print("\t\t\tTO START")
        print("\t\t\t*************************************************")
        continue

print("\t\t\t***************LET START THE GAME****************")
print("\t\t\t|-----------------------------------------------|")
print("\t\t\tSO", name.upper(), "THIS IS YOUR FIRST QUESTION")

from text import A, a, B, b, C, c, D, d, E, e, F, f, G, g, H, h, I, i, J, j
score=0

print(A, a)
n = int(input("\t\t\tENTER CORRECT OPTION\n\t\t\t"))
CORRECT_ANSWER = a[n]
if n == 4:
    print("\t\t\t", CORRECT_ANSWER, " is CORRECT ANSWER")
    score += 100
    print("\t\t\tYOUR TOTAL SCORE IS",score)
    print("\t\t\t|-----------------------------------------------|")
    print("\t\t\tSO", name.upper(), "THIS IS YOUR SECOND QUESTION")
    print(B, b)
    n = int(input("\t\t\tENTER CORRECT OPTION\n\t\t\t"))
    CORRECT_ANSWER = b[n]
    if n == 2:
        print("\t\t\t", CORRECT_ANSWER, " is CORRECT ANSWER")
        score += 150
        print("\t\t\tYOUR TOTAL SCORE IS", score)
        print("\t\t\t|-----------------------------------------------|")
        print("\t\t\tSO", name.upper(), "THIS IS YOUR THIRD QUESTION")
        print(C, c)
        n = int(input("\t\t\tENTER CORRECT OPTION\n\t\t\t"))
        CORRECT_ANSWER = c[n]
        if n == 3:
            print("\t\t\t", CORRECT_ANSWER, " is CORRECT ANSWER")
            score += 200
            print("\t\t\tYOUR TOTAL SCORE IS", score)
            print("\t\t\t|-----------------------------------------------|")
            print("\t\t\tSO", name.upper(), "THIS IS YOUR FOURTH QUESTION")
            print(D, d)
            n = int(input("\t\t\tENTER CORRECT OPTION\n\t\t\t"))
            CORRECT_ANSWER = d[n]
            if n == 1:
                print("\t\t\t", CORRECT_ANSWER, " is CORRECT ANSWER")
                score += 250
                print("\t\t\tYOUR TOTAL SCORE IS", score)
                print("\t\t\t|-----------------------------------------------|")
                print("\t\t\tSO", name.upper(), "THIS IS YOUR FIFTH QUESTION")
                print(E, e)
                n = int(input("\t\t\tENTER CORRECT OPTION\n\t\t\t"))
                CORRECT_ANSWER = d[n]
                if n == 3:
                    print("\t\t\t", CORRECT_ANSWER, " is CORRECT ANSWER")
                    score += 500
                    print("\t\t\tYOUR TOTAL SCORE IS", score)
                    print("\t\t\t|-----------------------------------------------|")
                    print("\t\t\tSO", name.upper(), "THIS IS YOUR SIXTH QUESTION")
                    print(F, f)
                    n = int(input("\t\t\tENTER CORRECT OPTION\n\t\t\t"))
                    CORRECT_ANSWER = f[n]
                    if n == 2:
                        print("\t\t\t", CORRECT_ANSWER, " is CORRECT ANSWER")
                        score += 600
                        print("\t\t\tYOUR TOTAL SCORE IS", score)
                        print("\t\t\t|-----------------------------------------------|")
                        print("\t\t\tSO", name.upper(), "THIS IS YOUR SEVENTH QUESTION")
                        print(G, g)
                        n = int(input("\t\t\tENTER CORRECT OPTION\n\t\t\t"))
                        CORRECT_ANSWER = g[4]
                        if n == 4:
                            print("\t\t\t", CORRECT_ANSWER, " is CORRECT ANSWER")
                            score += 650
                            print("\t\t\tYOUR TOTAL SCORE IS", score)
                            print("\t\t\t|-----------------------------------------------|")
                            print("\t\t\tSO", name.upper(), "THIS IS YOUR EIGHTH QUESTION")
                            print(H, h)
                            n = int(input("\t\t\tENTER CORRECT OPTION\n\t\t\t"))
                            CORRECT_ANSWER = f[n]
                            if n == 2:
                                print("\t\t\t", CORRECT_ANSWER, " is CORRECT ANSWER")
                                score += 750
                                print("\t\t\tYOUR TOTAL SCORE IS", score)
                                print("\t\t\t|-----------------------------------------------|")
                                print("\t\t\tSO", name.upper(), "THIS IS YOUR NINTH QUESTION")
                                print(I, i)
                                n = int(input("\t\t\tENTER CORRECT OPTION\n\t\t\t"))
                                CORRECT_ANSWER = f[n]
                                if n == 1:
                                    print("\t\t\t", CORRECT_ANSWER, " is CORRECT ANSWER")
                                    score += 800
                                    print("\t\t\tYOUR TOTAL SCORE IS", score)
                                    print("\t\t\t|-----------------------------------------------|")
                                    print("\t\t\tSO", name.upper(), "THIS IS YOUR TENTH QUESTION")
                                    print(J, j)
                                    n = int(input("\t\t\tENTER CORRECT OPTION\n\t\t\t"))
                                    CORRECT_ANSWER = f[n]
                                    if n == 3:
                                        print("\t\t\t", CORRECT_ANSWER, " is CORRECT ANSWER")
                                        score += 1000
                                        print("\t\t\tYOUR TOTAL SCORE IS", score)
                                        print("\t\t\t|-----------------------------------------------|")
                                        print("\t\t\tTOTLA SCORE =", score)
                                        print("\t\t\t*****************CONGRATULATIONS*****************")
                                        print("\t\t\t*************YOU WON THE WHOLE GAME**************")
                                else:
                                    print("\t\t\tTOTLA SCORE =", score)
                                    print("\t\t\tYOU LOSS THE GAME")
                            else:
                                print("\t\t\tTOTLA SCORE =", score)
                                print("\t\t\tYOU LOSS THE GAME")
                        else:
                            print("\t\t\tTOTLA SCORE =", score)
                            print("\t\t\tYOU LOSS THE GAME")
                    else:
                        print("\t\t\tTOTLA SCORE =", score)
                        print("\t\t\tYOU LOSS THE GAME")
                else:
                    print("\t\t\tTOTLA SCORE =", score)
                    print("\t\t\tYOU LOSS THE GAME")
            else:
                print("\t\t\tTOTLA SCORE =", score)
                print("\t\t\tYOU LOSS THE GAME")
        else:
            print("\t\t\tTOTLA SCORE =", score)
            print("\t\t\tYOU LOSS THE GAME")
    else:
        print("\t\t\tTOTLA SCORE =", score)
        print("\t\t\tYOU LOSS THE GAME")

else:
    print("\t\t\tTOTLA SCORE =", score)
    print("\t\t\tYOU LOSS THE GAME")