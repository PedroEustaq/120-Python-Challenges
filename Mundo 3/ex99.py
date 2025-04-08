print("FUNÇÃO MAIOR")
def maior(*num):
    qtn = 0
    maiorn = 0
    for v in num:
        qtn += 1
        if v > maiorn:
            maiorn = v
    print(f"O maior valor é {maiorn} foram passados {qtn} valores")
maior(2,9,4,5,1)