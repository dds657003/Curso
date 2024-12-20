# funcao  que converte fahrenheit para celsius
def farh_para_celcius (temp):
    resultado_celsius = ((temp - 32) * (5/9))
    return resultado_celsius

temp_fahr = float(input("Digite a temperatura em fahrenheit: "))
print(f"A temperatura farhenheit {temp_fahr}")
temp_celsius = farh_para_celcius(temp_fahr)
print(f"A temperatura em celsius: {temp_celsius}")
