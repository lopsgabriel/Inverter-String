def inverter_string(string):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1): 
        string_invertida += string[i]
    return string_invertida
#função para inverter a string

# Entrada do usuário para inverter a string
entrada = input("Digite uma string para inverter: \t")
string_invertida = inverter_string(entrada)

print("String invertida: ", string_invertida)