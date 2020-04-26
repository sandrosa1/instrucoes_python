segundos_str = input ("Por favor, digite o numero em segundos")
total_str =  int(segundos_str)

horas = total_segundos // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs restantes % 60

print (horas, "horas,",minutos, "minutos e ",segs_restantes_final) 
