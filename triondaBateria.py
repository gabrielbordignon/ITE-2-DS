# Inicialização das variáveis para o teste do sistema
bateria_atual = 14  # Exemplo de carga da bateria (inteiro de 0 a 100)
bola_em_jogo = False  # Exemplo do estado da partida (booleano)

# Estrutura de lógica condicional ordenável (If / Elif / Else)
if bateria_atual < 15 and bola_em_jogo == True:
    print("ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação.")

elif bateria_atual < 15 and bola_em_jogo == False:
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")

else:
    print("Sistema Trionda operando normalmente. Bateria ok.")
