# -*- coding: utf-8 -*-

#If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

#Not all numbers produce palindromes so quickly. For example,

#349 + 943 = 1292,
#1292 + 2921 = 4213
#4213 + 3124 = 7337

#That is, 349 took three iterations to arrive at a palindrome.

#Although no one has proved it yet, it is thought that some numbers, like 196,
#never produce a palindrome. A number that never forms a palindrome through the
#reverse and add process is called a Lychrel number. Due to the theoretical
#nature of these numbers, and for the purpose of this problem, we shall assume
#that a number is Lychrel until proven otherwise.In addition you are given that
#for every number below ten-thousand, it will either (i) become a palindrome in
#less than fifty iterations, or, (ii) no one, with all the computing power that
#exists, has managed so far to map it to a palindrome. In fact, 10677 is the
#first number to be shown to require over fifty iterations before producing a
#palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

#Surprisingly, there are palindromic numbers that are themselves Lychrel
#numbers; the first example is 4994.

#How many Lychrel numbers are there below ten-thousand?

#NOTE: Wording was modified slightly on 24 April 2007 to emphasise the
#theoretical nature of Lychrel numbers.


def ispalindrome(n):
    s = str(n)
    for i in range(0, len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


def numreverse(n):
    s1 = str(n)
    s2 = ''
    for i in range(len(s1) - 1, -1, -1):
        s2 = s2 + s1[i]
    return int(s2)


def result():
    num_max = 10000
    max_iter = 50
    lychrel = 0
    for n in range(1, 10000):
        ispal = False
        na = n
        nr = numreverse(n)
        for i in range(0, max_iter):
            if ispalindrome(na + nr):
                ispal = True
                break
            na = na + nr
            nr = numreverse(na)

        if not ispal:
            lychrel = lychrel + 1

    return lychrel
