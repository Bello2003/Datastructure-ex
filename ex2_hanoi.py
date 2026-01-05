def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Déplacer disque 1 de {source} vers {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Déplacer disque {n} de {source} vers {target}")
    hanoi(n-1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')
