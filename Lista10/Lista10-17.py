d = input().split("/")
m = {1: "janeiro", 2: "fevereiro", 3: "mar�o", 4: "abril", 5: "maio", 6: "junho", 
     7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"}
print(f"Voc� nasceu em {d[0]} de {m[int(d[1])]} de {d[2]}")