print ("SALÁRIO DO MÊS")

valor_hora = float(input("Informe o valor da hora trabalhada:"))

horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês:"))
# calcula o convênio médico do titular
ida = int(input("Qual a sua idade "))
if(ida <= 18):
    conv1 = 149.25
elif (ida >= 19 and ida <= 23):
    conv1 = 191.76
elif (ida >= 24 and ida <= 28):
    conv1 =  219.91
elif (ida >= 29 and ida <= 33):
    conv1 = 241.22
elif (ida >= 34 and ida <= 38):
    conv1 =  247.48
elif (ida >= 39 and ida <= 43):
    conv1 = 278.74
elif (ida >= 44 and ida <= 48):
    conv1 = 334.77
elif (ida >= 49 and ida <= 53):
    conv1 = 457.18
elif (ida >= 54 and ida <= 58):
    conv1 = 488.62
else:
    conv1 = conv + 749.88
    
# calcula o convênio médico dos dependentes    
nd = int( input ("Informe o número de dependentes "))
if(nd == 0):
    conv = 0
else:
    cont = 0
    conv = 0
    i = 1
    while( cont != nd ):
        print ("informe a idade do",i,"º depende")
        ida = int(input(""))
        i = i + 1
        if (ida <= 18):
            conv = conv + 149.25
        elif (ida >= 19 and ida <= 23):
            conv = conv + 191.76
        elif (ida >= 24 and ida <= 28):
            conv = conv + 219.91
        elif (ida >= 29 and ida <= 33):
            conv = conv + 241.22
        elif (ida >= 34 and ida <= 38):
            conv = conv + 247.48
        elif (ida >= 39 and ida <= 43):
            conv = conv + 278.74
        elif (ida >= 44 and ida <= 48):
            conv = conv + 334.77
        elif (ida >= 49 and ida <= 53):
            conv = conv + 457.18
        elif (ida >= 54 and ida <= 58):
            conv = conv + 488.62
        else:
            conv = conv + 749.88
            
        cont = cont + 1
     
# calcula salário bruto
sb = valor_hora * horas_trabalhadas

#calcula dedução po depende
d = 189.59 * nd

# cálculo o inss
if(sb <= 1830.30):
    inss = sb * .08
elif( sb > 1830.30 and sb <= 3050.52):
    inss = sb * .09
elif( sb > 3050.52 and sb <= 6101.06):
    inss = sb * .11
else:
    inss = 671.12 
 
 # calcula o imposto de renda
if (sb <= 1903.98):
    ir = 0
elif (sb > 1903.98 and sb <= 2836.67):
    ir = (( sb - d - inss ) * .075 ) - 142,80
elif ( sb > 2836.66 and sb <= 3751.05):
    ir = (( sb - d - inss ) * .15 ) - 354.80
elif ( sb > 3751.05 and sb <= 4664.68):
    ir = (( sb - d - inss) * .225) - 636.13
else:
    ir = (( sb - d - inss ) * .275) - 869.36

#calcula contribuição sindical
if (sb <= 5799.00):
    sind = sb * .01
else:
    sind = 57.99

t = str(input("Possui convênio médico do titular? [ s/n ] ")) 
if (t == "s"):
    te = 1
else:
    te = 0
de = str(input("Os dependentes possuem convênio médico? [ s/n ]"))
if (de == "s"):
    den = 1
else:
    den = 0
       
# soma e divisão do convênio médico     
con = ((conv * te) + (conv1 * den))/2

print("______________________________________")
print ("")

print ("Salario bruto -> R$",sb )
print ("Imposto de renda -> R$",ir )
print ("Inss -> R$ ",inss )
print ("Convênio médico -> R$",con)
print ("contribuição sindical -> R$",sind)
print ("Refeição ->R$ 34.80")
print ("")
print ("_____________________________________")
print("Valor do adiantamento R$",sb * .40 )
print("Salário líquido é R$", (sb - ir - inss - con - sind - 34.8 ) - ( sb * .40))
