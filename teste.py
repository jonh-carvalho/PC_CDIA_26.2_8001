def fibonacci(n):
	"""Retorna os primeiros n números da sequência de Fibonacci."""
	if n < 0:
		raise ValueError("n deve ser não negativo")

	numeros = []
	a, b = 0, 1
	for _ in range(n):
		numeros.append(a)
		a, b = b, a + b
	return numeros


if __name__ == "__main__":
	quantidade = int(input("Quantos números de Fibonacci? "))
	print(fibonacci(quantidade))
