import streamlit as st
import itertools
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a distância euclidiana
def distancia(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Função para calcular o caminho mínimo
def calcular_melhor_caminho(A, B, paredes):
    combinacoes_paredes = list(itertools.product(*paredes))  # Número total de combinações possíveis

    melhor_caminho = None
    menor_distancia = float('inf')  # Inicializa com a menor distância no infinito

    for combinacao in combinacoes_paredes:
        for ordem in itertools.permutations(combinacao):
            caminho = [A] + list(ordem) + [B]
            distancia_total = sum(distancia(caminho[i], caminho[i+1]) for i in range(len(caminho)-1))

            if distancia_total < menor_distancia:
                menor_distancia = distancia_total
                melhor_caminho = caminho

    return melhor_caminho, menor_distancia

# Função para plotar o gráfico do caminho
def plotar_caminho(A, B, melhor_caminho):
    fig, ax = plt.subplots()
    ax.plot(*zip(*[A] + melhor_caminho + [B]), marker='o', label="Caminho Mínimo")
    
    ax.set_title("Caminho Mínimo")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Título do aplicativo
st.title("Caminho mínimo")

# Inputs para as coordenadas dos pontos A e B (como caixas de texto menores e lado a lado)
st.sidebar.subheader("Coordenadas de A e B")
col1, col2 = st.sidebar.columns(2)
A_x = col1.text_input("X de A", "0", max_chars=5)
A_y = col2.text_input("Y de A", "0", max_chars=5)
B_x = col1.text_input("X de B", "10", max_chars=5)
B_y = col2.text_input("Y de B", "10", max_chars=5)

# Convertendo as entradas para float
A = (float(A_x), float(A_y))
B = (float(B_x), float(B_y))

# Número de paredes
num_paredes = st.sidebar.number_input("Número de paredes", min_value=1, max_value=10, value=3)

# Definir as paredes
paredes = []
for i in range(num_paredes):
    st.sidebar.subheader(f"Parede {i+1}")
    col1, col2 = st.sidebar.columns(2)
    x1 = col1.text_input(f"X1 P{i+1}", "0", max_chars=5)
    y1 = col2.text_input(f"Y1 P{i+1}", "0", max_chars=5)
    x2 = col1.text_input(f"X2 P{i+1}", "1", max_chars=5)
    y2 = col2.text_input(f"Y2 P{i+1}", "1", max_chars=5)

    # Convertendo as entradas para float e adicionando à lista de paredes
    paredes.append([(float(x1), float(y1)), (float(x2), float(y2))])

# Calcular o melhor caminho
melhor_caminho, menor_distancia = calcular_melhor_caminho(A, B, paredes)

# Exibir os resultados
st.write(f"Menor Distância: {menor_distancia}")
st.write("Melhor Caminho (Menor Distância):")
for ponto in melhor_caminho:
    st.write(ponto)

# Plotar o gráfico do melhor caminho
plotar_caminho(A, B, melhor_caminho)
