def calcular_novo_preco(preco):
    if preco <= 50:
        return preco * 1.05
    else:
        return preco * 1.10


# Lista de produtos com preços reais (exemplo)
produtos = [
    ("Caderno", 25.00),
    ("Caneta", 3.50),
    ("Fone de ouvido", 45.00),
    ("Mouse", 60.00),
    ("Teclado", 120.00)
]


print("=== REAJUSTE DE PREÇOS ===\n")

for nome, preco in produtos:
    novo_preco = calcular_novo_preco(preco)

    print(f"Produto: {nome}")
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Novo preço: R$ {novo_preco:.2f}")
    print("-" * 30)