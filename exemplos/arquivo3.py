# Trabalhando com uma lista e a estrutura for
frutas = ["maçã", "banana", "Uva"]
cv=0
for fruta in frutas:
    for i in fruta:
        if i.lower in ('aeiou'):
            cv+=1
print(cv)
