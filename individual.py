class Candidato:
    def __init__(self, nome, entrevista, teste_teórico, teste_prático, soft_skills):
        self.nome = nome
        self.entrevista = entrevista
        self.teste_teórico = teste_teórico
        self.teste_prático = teste_prático
        self.soft_skills = soft_skills

    def __repr__(self):
        return f"{self.nome}: e{self.entrevista}_t{self.teste_teórico}_p{self.teste_prático}_s{self.soft_skills}"

# Exemplo de lista de candidatos
lista_candidatos = [
    Candidato("João", 8, 7, 9, 6),
    Candidato("Maria", 9, 8, 7, 8),
    Candidato("Pedro", 7, 6, 8, 7),
    Candidato("Ana", 8, 9, 8, 9)
]

def buscar_candidatos(candidatos, criterios):
    resultados = []
    for candidato in candidatos:
        if all(getattr(candidato, criterio[0]) >= criterio[1] for criterio in criterios):
            resultados.append(candidato)
    return resultados

# Exemplo de utilização da função
crit = [('entrevista', 8), ('teste_teórico', 7), ('teste_prático', 8)]
resultados = buscar_candidatos(lista_candidatos, crit)
print("Candidatos encontrados:")
for candidato in resultados:
    print(candidato.nome)
