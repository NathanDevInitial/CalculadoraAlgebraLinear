import numpy as np
import sympy as sp

def calcular_produto_escalar(u, v):
    try:
        u = np.array(eval(u))
        v = np.array(eval(v))
        produto_escalar_resultado = np.dot(u, v)
        return f"O produto escalar dos vetores é: {produto_escalar_resultado}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

# Restante das funções...

def calcular_valor_k(u, v, w):
    try:
        # Obter os valores inseridos pelo usuário para os vetores
        u_input = u
        v_input = v
        w_input = w

        u = sp.symbols(u_input)
        v = sp.symbols(v_input)
        w = sp.symbols(w_input)

        a, b = sp.symbols('a b')

        eq = sp.Eq(a * u[0] + b * u[1], w[0])

        solucao = sp.solve(eq, (a, b))

        a_valor, b_valor = solucao[a], solucao[b]

        return f"O valor de a é: {a_valor}\nO valor de b é: {b_valor}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"
