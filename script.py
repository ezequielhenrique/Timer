# Teste
import time


def timer(t):
    while True:
        if t == 0:
            break
        time.sleep(1)
        t -= 1
        print(t)
