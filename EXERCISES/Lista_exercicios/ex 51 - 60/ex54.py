dias_da_semana = ["Domingo","Segunda","Terça","Quarta","Quinta", "Sexta", "Sabado"]

def dias_com_S (dias_que_comecam_com_S):
    ajuda = []
    for data in dias_que_comecam_com_S:
        if "S" in data:
            ajuda.append(data)
    return ajuda

dias_tem_a_inicial_s = dias_com_S(dias_da_semana)
print(dias_tem_a_inicial_s)