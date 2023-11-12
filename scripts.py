from flask import Flask, render_template, request, jsonify
import numpy as np
import sympy as sp

app = Flask(__name__)

# Função para calcular o produto escalar
def calcular_produto_escalar(u, v):
    try:
        u = np.array(eval(u))
        v = np.array(eval(v))
        produto_escalar_resultado = np.dot(u, v)
        return f"O produto escalar dos vetores é: {produto_escalar_resultado}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def calcular_produto_vetorial(u, v):
    try:
        u = np.array(eval(u))
        v = np.array(eval(v))
        produto_vetorial_resultado = np.cross(u, v)
        return f"O produto vetorial dos vetores é: {produto_vetorial_resultado}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def calcular_interseccao(u, v, w):
    try:
        u = set(eval(u))
        v = set(eval(v))
        w = set(eval(w))
        interseccao_resultado = list(u.intersection(v, w))
        return f"A interseção dos vetores é: {interseccao_resultado}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def calcular_combinacao_linear(u, v, w):
    try:
        u = np.array(eval(u))
        v = np.array(eval(v))
        w = np.array(eval(w))

        if np.linalg.matrix_rank(np.vstack([u, v])) < 2:
            return "Os vetores u e v devem ser linearmente independentes."

        solucao, _, _, _ = np.linalg.lstsq(np.vstack([u, v]).T, w, rcond=None)

        a, b = solucao
        return f"O valor de a é: {a:.6f}\nO valor de b é: {b:.6f}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def calcular_soma(u, v, w=None):
    try:
        u = np.array([float(x) for x in u.split(',')])
        v = np.array([float(x) for x in v.split(',')])

        if w:
            w = np.array([float(x) for x in w.split(',')])
            soma_resultado = u + v + w
        else:
            soma_resultado = u + v

        return f"A soma dos vetores é: {soma_resultado}"

    except Exception as e:
        return f"Ocorreu um erro: {e}"

def calcular_valor_k(u, v, w):
    try:
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    print(data)  # Adicione esta linha para imprimir os dados no console do Flask
    resultado_produto_escalar = calcular_produto_escalar(data['u'], data['v'])
    data = request.get_json()

    # Chame as funções com os dados recebidos
    resultado_produto_escalar = calcular_produto_escalar(data['u'], data['v'])
    resultado_produto_vetorial = calcular_produto_vetorial(data['u'], data['v'])
    resultado_interseccao = calcular_interseccao(data['u'], data['v'], data['w'])
    resultado_combinacao_linear = calcular_combinacao_linear(data['u'], data['v'], data['w'])
    resultado_soma = calcular_soma(data['u'], data['v'], data['w'])
    resultado_valor_k = calcular_valor_k(data['u'], data['v'], data['w'])

     
    # Retorne os resultados em formato JSON
    return jsonify({
        'produto_escalar': resultado_produto_escalar,
        'produto_vetorial': resultado_produto_vetorial,
        'interseccao': resultado_interseccao,
        'combinacao_linear': resultado_combinacao_linear,
        'soma': resultado_soma,
        'valor_k': resultado_valor_k
    })

if __name__ == '__main__':
    app.run(debug=True)
