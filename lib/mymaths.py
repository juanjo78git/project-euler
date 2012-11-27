# mymaths algunas funciones que uso mucho

def ispalindrome(n):
    s = str(n)
    for i in range(0, len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
