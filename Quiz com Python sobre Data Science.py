# Quiz: Fundamentos de BI, Data Science e Inteligência Artificial
# Baseado em conceitos de governança de dados, análise preditiva e agentes autônomos.

questoes = [
    {
        "enunciado": "1. Tanto BI, quanto Data Science e Inteligência Artificial prescindem (não precisam) de dados para funcionar adequadamente.",
        "resposta": "F",
        "justificativa": "Nenhum dos três campos existe sem dados. O tratamento e a limpeza são obrigatórios."
    },
    {
        "enunciado": "2. O princípio 'Garbage in, Garbage out' significa que a qualidade das respostas do sistema depende diretamente da qualidade dos dados inseridos.",
        "resposta": "V",
        "justificativa": "Se entra lixo, sai lixo. A governança da informação é essencial."
    },
    {
        "enunciado": "3. O Business Intelligence (BI) é focado na análise preditiva e prescritiva, respondendo a perguntas como 'O que vai acontecer amanhã?'.",
        "resposta": "F",
        "justificativa": "O BI foca no Passado e Presente (análise descritiva/diagnóstica). Quem responde sobre o amanhã é Data Science."
    },
    {
        "enunciado": "4. Ferramentas computacionais como Python, R e SQL são a base para laboratórios de pesquisa em qualquer uma dessas três áreas de dados.",
        "resposta": "V",
        "justificativa": "O uso de linguagens orientadas a dados é o ponto de partida exigido."
    },
    {
        "enunciado": "5. O produto final do BI costuma ser Dashboards e relatórios para monitoramento, onde a máquina decide sozinha o que fazer.",
        "resposta": "F",
        "justificativa": "No BI, o sistema relata e o humano toma a decisão."
    },
    {
        "enunciado": "6. A Ciência de Dados (Data Science) consegue lidar muito bem com dados não estruturados, como textos, imagens e áudios armazenados em Data Lakes.",
        "resposta": "V",
        "justificativa": "A tipologia de dados de Data Science foca exatamente nesse ambiente não estruturado."
    },
    {
        "enunciado": "7. Testes A/B, algoritmos de clusterização e modelos preditivos são saídas (produtos) típicas do campo de Inteligência Artificial, e não de Data Science.",
        "resposta": "F",
        "justificativa": "Esses são produtos centrais da Ciência de Dados."
    },
    {
        "enunciado": "8. A Inteligência Artificial busca criar agentes capazes de mimetizar capacidades cognitivas humanas, atuando de forma autônoma ou semi-autônoma.",
        "resposta": "V",
        "justificativa": "A IA foca na ação contínua, onde o sistema toma decisões independentes."
    },
    {
        "enunciado": "9. Chatbots, carros autônomos e motores de recomendação são exemplos práticos de sistemas de Inteligência Artificial em produção.",
        "resposta": "V",
        "justificativa": "Esses sistemas utilizam subcampos como Machine Learning, Visão Computacional e Processamento de Linguagem Natural."
    },
    {
        "enunciado": "10. Os currículos dessas áreas exigem bases matemáticas profundas, como Cálculo e Álgebra Linear, mas a IA dispensa a ética em favor do aprendizado rápido.",
        "resposta": "F",
        "justificativa": "A abordagem pedagógica na IA aborda fortemente a ética na governança e o desenvolvimento transparente e sem vieses dos modelos."
    }
]


def executar_quiz():
    print("=" * 60)
    print("QUIZ: BI vs DATA SCIENCE vs INTELIGÊNCIA ARTIFICIAL")
    print("=" * 60)
    print("Responda com 'V' para Verdadeiro ou 'F' para Falso.\n")

    pontuacao = 0
    respostas_usuario = []

    # Loop para fazer as perguntas
    for q in questoes:
        print(q["enunciado"])

        resp = input("Sua resposta (V/F): ").strip().upper()

        # Validação da entrada
        while resp not in ["V", "F"]:
            resp = input(
                "Entrada inválida. Digite apenas 'V' ou 'F': "
            ).strip().upper()

        respostas_usuario.append(resp)

        if resp == q["resposta"]:
            pontuacao += 1

        print("-" * 60)

    # Exibição do resultado final
    print("\n" + "=" * 60)
    print(
        f"RESULTADO FINAL: Você acertou {pontuacao} de {len(questoes)} questões!"
    )
    print("=" * 60)

    percentual = (pontuacao / len(questoes)) * 100
    print(f"Aproveitamento: {percentual:.1f}%")

    print("\n--- GABARITO E JUSTIFICATIVAS ---")

    for i, q in enumerate(questoes):
        correta = q["resposta"]
        dada = respostas_usuario[i]

        status = "✅ ACERTOU" if correta == dada else "❌ ERROU"

        print(f"\nQuestão {i + 1} - {status}")
        print(f"Sua resposta: {dada} | Resposta correta: {correta}")
        print(f"Justificativa: {q['justificativa']}")

    # Feedback final
    print("\n" + "=" * 60)

    if percentual >= 90:
        print("🏆 Excelente! Você domina os conceitos de BI, Data Science e IA.")
    elif percentual >= 70:
        print("👍 Muito bom! Você possui um bom entendimento dos temas.")
    elif percentual >= 50:
        print("📚 Bom começo! Vale revisar alguns conceitos.")
    else:
        print("🚀 Continue estudando. A prática leva ao domínio do conhecimento.")

    print("=" * 60)


# Executa o programa
if __name__ == "__main__":
    executar_quiz()
