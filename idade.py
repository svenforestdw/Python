from datetime import date 


def calcular_idade(nascimento: date) -> int:
	"""Calcula a idade a partir da data de nascimento, date(year, month, day).
	
	Args:
		nascimento (date): data de nascimento.
	
	Returns:
		int: idade.
	"""

	hoje = date.today() 
	idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day)) 

	return idade


def maior_de_idade(nascimento: date) -> bool:
	"""Retorna se uma pessoa é maior de idade a partir da data de nascimento, date(year, month, day).

	Args:
		nascimento (date): data de Nascimento.

	Returns:
		bool: True se for maior de idade e False caso contrário.
	"""

	hoje = date.today()

	return (hoje.month, hoje.day) > (nascimento.month, nascimento.day)
