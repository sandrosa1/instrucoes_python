seg = input (" Por favor, entre com o número de segundos que deseja converter: ")
seg = (int(seg))
dia = seg // 86400
restodia = seg % 86400
hora = restodia // 3600
restohora = restodia % 3600
minutos = restohora // 60
restominutos = restohora %60
segundos = restominutos

print (dia,"dias",hora,"horas",minutos,"minutos e",segundos,"segundos.")
