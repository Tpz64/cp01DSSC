import streamlit as st
import time
import pandas as pd 
import numpy as np
import scipy.stats as stats
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *
from scipy.stats import norm


#titulo da página
st.markdown("<h1 style='color: #F38C79;'>Análise de dados</h1>", unsafe_allow_html=True)
#st.header("Análise de dados")

st.logo("imgs/logo-cea-1.png")#Logo C&A

#paginas para mudar
pages = st.sidebar.selectbox("Análise", [
    "Apresentação dos dados",
    "Análise Inicial",
    "Distribuição",
    "Conclusão"
])

#info lateral minha
st.sidebar.markdown("""
    <div style="
        background-color: #F38C79; 
        color:white;
        padding: 9px; 
        border-radius: 10px;
        text-align: center;
    ">
        Desenvolvido por  <a href="https://www.linkedin.com/in/thaisgleoncio/" target="_blank" style="color: white; text-decoration: none; font-weight: bold;"> Thaís Leoncio</a>
    </div>
""", unsafe_allow_html=True)

#Leitura CSV
csv_path = "dados/Womens Clothing E-Commerce Reviews.csv"
df = pd.read_csv(csv_path) 

# Função para exibir gráfico Plotly
def plot_distribution(x, y, title, xlabel, ylabel):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
    st.plotly_chart(fig)

#Barra de carregamento
my_bar = st.progress(0)
for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

#st.balloons()

if pages == "Apresentação dos dados":
    #st.subheader("Apresentação dos dados")
    st.markdown("<h3 style='color: #F38C79;'>Apresentação dos dados</h3>", unsafe_allow_html=True)
    st.write("Tendo em foco o **Programa de estágio 2025 da C&A Elas em tech**, decidi ir atrás de um dataset relacionado ao mundo da moda. Entre tantos, acabei encotrando uma base de dados sobre **Avaliações de roupas femininas no E-commerce**, tema altamente relacionado com as vagas disponíveis na C&A, que são relacionadas principalmente a seu aplicativo. Se trata de uma base real, porém com diversas informações sensíveis sendo colocadas em anonimato.")
    st.write("Aqui deixo o link para base de dados, caso queira verificar: [Kaggle](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews?resource=download)")

    st.write("Sobre o dataset, ele possuiu 10 colunas principais, que são:")
    st.markdown("""
    - *Clothing ID*: uma variável quantitativa discreta, que se refere a uma peça de roupa especifica que foi avaliada;
    - *Age*: variável quantitativa discreta, que mostra a idade das mulheres que avaliaram;
    - *Title*: variável qualitativa nominal, um título para as reviews;
    - *Review Text*: variável qualitativa nominal, que possui o texto das avaliações;
    - *Rating*: variável quantitativa discreta, a nota que as mulheres deram para os produtos, vão de 1 a 5, sendo 1 horrível e 5 o melhor;
    - *Recommended IND*: variável quantitativa discreta, onde mostra se o cliente recomenda o produto, sendo 1 recomendado, e 0 não recomendado;
    - *Positive Feedback Count*: váriável quantitativa discreta, que documenta o número que outros clientes que acharam a avaliação positiva;
    - *Division Name*: variável qualitativa nominal, nome da divisão de onde veio o produto;
    - *Department Name*: variável qualitativa nominal, categoriza o departamento de onde veio o produto;
    - *Class Name*: variável qualitativa nominal, nome da classe do produto.
    """)

    #st.write("**Principais perguntas da análise**")
    st.markdown("<h5 style='color: #F38C79;'>Principais perguntas da análise</h5>", unsafe_allow_html=True)
    st.markdown("""
    - Quais são as faixas etárias que mais avaliam as roupas?
    - Qual existem mais avaliações positivas ou negativas sobre as roupas?
    - Avaliações boas influenciam na recomendação das peças de roupa?
    - As avaliações para uma mesma peça de roupa são consistentes ou variam muito?
    - Qual a distribuição etária das consumidoras que deixam avaliações?
    - Quais são as roupas mais bem avaliadas, e as piores avaliadas? 
    - As roupas mais recomendadas são as que realmente possuem as melhores notas?
    - Comentarios com mais feedback positivo indicam peças de melhor qualidade ou simplismente maior volume de vendas?
    - Quais são as divisões, departamentos e produtos que mais possuem avaliações? 
    - Existe relação entre idade e tipo de roupa avaliada?
    - Há variação na satisfação do cliente dependendo da divisão/ departamento da peça de roupa?
    """)

    # Leitura CSV
    csv_path = "dados/Womens Clothing E-Commerce Reviews.csv"
    df = pd.read_csv(csv_path)
    st.markdown("<h3 style='color: #F38C79;'>Visualização dos dados sem tratamento:</h3>", unsafe_allow_html=True)
    #st.subheader("Visualização dos dados sem tratamento:")
    st.dataframe(df) 
    #st.write(df.head()) 

elif pages == "Análise Inicial":
    #st.subheader("Análise incial dos dados")
    st.markdown("<h3 style='color: #F38C79;'>Análise incial dos dados</h3>", unsafe_allow_html=True)
    st.write("O primeiro passo dessa análise é tirar as colunas que não iremos utilizar, que nesse caso são *Title* e *Review Text*, colunas altamente qualitativas e que não influenciaram a nossa análise, e com isso, foi gerado um dataframe filtrado, conforme mostrado abaixo.")
    df = df.drop(columns=["Unnamed: 0","Title","Review Text"])
    st.dataframe(df)

    st.write("Com o dataframe filtrado, usaremos a função describe() do pandas para ter os principais valores estatísticos das colunas quantitativas, como média, mediana e desvio padrão.")
    st.write(df.describe())
    st.write("Para iniciar as análises, verificaremos duas colunas iniciais, a coluna Idade (Age) e a Coluna Rating.")
    st.write("Na coluna *Age*, percebemos que a média de mulheres que realizam compras e as avaliam é de 43 anos, valor bem próximo da mediana, que é 41 anos. O desvio padrão (std) é de 12 anos sugere uma variação considerável nas idades dos comentários, o que significa que a distribuição de idades não é homogenia. A menor idade das mulheres que comentaram foi de 18 anos, o que revela que para realizar compras neste site é necessário ser maior de idade, enquanto a maior idade foi de 99 anos. Analisando os quartils, percebemos que a maioria das clientes que comentam estão na fase adulta, sendo poucas pertecentes a faixa etária de jovem adultas ou da terceira idade.")
    st.write("Analisando a coluna *Rating*, percebemos que a média foi de 4.1, bastante alta se levarmos em consideração que o intervalo de notas vai de 1 a 5. Análisando os quartils, percebemos que a maior concetração de dados esta entre 4 e 5 estrelas, o que podemos concluir que na grande maioria dos casos as compras são positivas, sendo pouquissimas que possuem uma avaliação abaixo de 4 estrelas. ")
    st.write("Continuando a análise, faremos a contagem de frequência dos valores repetidos desse dataset, para verificarmos se encontramos algo interessante. Abaixo, pode-se selecionar as colunas que deseja vizualizar.")
   
    # Frequencia
    st.markdown("<h6 style='color: #F38C79;'>Contagem de valores repetidos</h6>", unsafe_allow_html=True)
    #st.write("**Contagem de valores repetidos**")
    id_column = st.selectbox("Selecione a coluna:", df.columns)
    if id_column:
        id_counts = df[id_column].value_counts().reset_index()
        id_counts.columns = [id_column, "Quantidade"]
        st.dataframe(id_counts)
        st.markdown("<h6 style='color: #F38C79;'>Estatísticas das quantidades</h6>", unsafe_allow_html=True)
        st.write(id_counts["Quantidade"].describe())

    st.write("Filtrando os valores da coluna *'Clothing ID'*, percebemos que a roupa que mais possui avaliação passou das mil postagens. Porém ao analisarmos a estatistíca da quantidade de dados, percebemos que essa não é a realidade, já que a maioria das roupas possui em média 19 avaliações, sendo a mediana 2 avaliações, os quartis revelam que a maioria dos dados estão entre 1 a 6 comentários por roupa, além de possuir um desvio padrão alto de 69. Verificando esses valores, percebemos que esse valor máximo é um grande outlier, pois o normal é as roupas terem poucas avaliações."
    " A quantidade de comentários não reflete necessáriamente a quantidade de roupas vendidas, porém a quantidade de avaliações é um certo indicativo de sucesso de certas roupas. Poderiamos no futuro analisar a partir de quantos comentários, uma roupa pode ser considerada sucesso na plataforma, e separar por departamento.")

    st.markdown("<h4 style='color: #F38C79;'>Correlação</h4>", unsafe_allow_html=True)

    st.write("Ao observar o dados, imaginamos que exista uma correlação entre a coluna *Rating* e *Recommended IND*. Para entender se a nota do produto está relacionada com a recomendação, calcularemos o valor da correlação, usando o coeficiente de Point-Biserial, pois a coluna de recomendação é binomial.")

    corr_pointbiserial, _ = stats.pointbiserialr(df['Rating'], df['Recommended IND'])

    # Exibir o coeficiente de correlação no Streamlit
    st.write(f'O coeficiente de correlação de Point-Biserial entre "Rating" e "Recommended IND" é: `{corr_pointbiserial:.4f}`')

    st.write("O valor obtido indica uma forte correlação positiva. Isso significa que, à medida que a nota do produto aumenta, a probabilidade de recomendação também tende a aumentar. Embora essa correlação seja alta, ela não é perfeita, sugerindo que outros fatores também influenciam a recomendação do produto.")


#PAGINA DISTRIBUIÇÃO
elif pages == "Distribuição":
    #st.subheader("Distribuição")
    st.markdown("<h3 style='color: #F38C79;'>Distribuição</h3>", unsafe_allow_html=True)

    st.write("Conhecido também com distribuição de probabilidade, ela descreve como os valores são distribuídos, se são comuns ou incomuns. Usamos para determinar qual a probabilidade de algo ou um valor específico acontecer. ")
    st.write("Tendo o conhecimento do que são distribuições, e visando a base nos dados que temos, escolhemos calular a probabilidade de dois eventos:")

    st.markdown(""" 
    **1.** *Qual a probabilidade de alguém recomendar a compra em 10 tentativas?*
    - Para isso, vamos usar como base a coluna 'Recommended IND', uma coluna binomial, e para isso usaremos a **distribuição binomial**.
                
    **2.** *Qual a probabilidade de a próxima cliente a comentar ter a idade próxima da média?*
    -  Para isso usaremos a coluna *Age* como base, e usaremos a **distribuição normal**. 
    """)

    st.markdown("<h4 style='color: #F38C79;'>Distribuição Binomial</h4>", unsafe_allow_html=True)
    st.write("A distribuição binomial é usada quando temos eventos independentes e idênticos que resultam em *sucesso* ou *fracasso*. Esse tipo de distribuição é apropriada para modelar a probabilidade de recomendações, pois a coluna *Recommended IND* assume apenas dois valores possíveis: recomendar (1) ou não recomandar (0). ")
    st.write("A probabilidade de obter um número específico de sucessos em um conjunto fixo de tentativas segue a seguinte formúla matemática:")
    st.latex(r"P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}")

    st.write("Para melhor visualização e entendimento, delimitamos o número de tentativas para 10, e deixamos o usuário escolher o número de sucessos desejado, e abaixo será mostrado a propabilidade de esse número ocorrer. Junto a essa informação, será mostrado o resultado do número de sucessos esperado e a probabilidade estimada com base nos dados da coluna de recomendação.")
    st.write("Além disso, colocamos abaixo a tabela de probabildade, que mostra a probabilidade, junto à probabilidade acumulada.")

    #distribuicao binomial 

    if "Recommended IND" in df.columns:
        # Calculando n (total de avaliações) e p (probabilidade de sucesso)
        n = 10  # Total de tentativas (avaliações)
        p = df["Recommended IND"].mean()  # Probabilidade de sucesso (média dos valores)

        # Entrada do usuário para definir k
        k = st.slider("Número de sucessos desejados (k)", min_value=0, max_value=n, value=n//2, step=1)

        # Cálculo da distribuição binomial
        x = np.arange(0, n + 1)  # Possíveis números de sucessos
        y = stats.binom.pmf(x, n, p)  # Probabilidades para cada número de sucessos
        prob_k = stats.binom.pmf(k, n, p)  # Probabilidade específica de k sucessos
        expected_successes = n * p  # Número esperado de sucessos

        # Exibir resultados
        st.markdown(f"###### Probabilidade de obter **{k}** sucessos: `{prob_k:.6f}`")
        st.markdown(f"###### Número esperado de sucessos: `{expected_successes:.2f}`")
        st.markdown(f"###### Probabilidade de sucesso (p) estimada: `{p:.4f}`")

        # Criar tabela de probabilidades
        df_binomial = pd.DataFrame({"Número de Sucessos": x, "P(X)": y, "P(X ≤ k) (Acumulado)": np.cumsum(y)}).set_index("Número de Sucessos")
        st.markdown("<h5 style='color: #F38C79;'>Tabela de Probabilidade</h5>", unsafe_allow_html=True)

        st.dataframe(df_binomial)

        st.write("Para melhor visualização, colocamos as informações acima em um gráfico interativo da distribuição binomial.")
        # Criar gráfico interativo
        fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color="#f38c79")])
        fig.update_layout(title="Distribuição Binomial", xaxis_title="Número de Sucessos", yaxis_title="Probabilidade", template="plotly_white")

        st.plotly_chart(fig)
    
    st.write("Ao analisar as informações, observamos que a probabilidade de as próximas compras receberem recomendações positivas é bastante alta. Em cada 10 avaliações feitas no site, a maior parte das mulheres (entre 8 e 9) tende a recomendar a peça que compraram. A probabilidade de que poucas mulheres recomendem a compra é muito baixa. Isso sugere que, em sua maioria, as roupas compradas neste site são de boa qualidade e proporcionaram uma excelente experiência de entrega. Para uma análise mais aprofundada no futuro, seria interessante estudar os comentários das mulheres que não recomendaram a compra de determinadas peças, a fim de identificar áreas em que o site possa melhorar")
    st.write("De forma geral, podemos conluir que a grande maioria das mulheres tende a recomendar as peças adquiridas neste e-commerce.")

    #############
    st.markdown("<h4 style='color: #F38C79;'>Distribuição Normal</h4>", unsafe_allow_html=True)
    st.write("Também conhecida como *distribuição de Gauss*, é usada quando temos uma váriavel contínua que segue um padrão simétrico em torno da média, formando ao final um gráfico com a forma de um sino. ")
    st.write("A fórmula da densidade de probabilidade normal é: ")
    st.latex(r"f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}")
    st.write("Dentro dos dados que possuimos, a idade das clientes é uma variável contínua e tende a seguir um padrão aproximadamente simétrico ao redor da média.")
    st.write("Para essa análise, usaremos o conceito de normal *empírica* e *teórica*, onde a primeira é a distribuição real dos dados observados, equanto que a segunda é uma idealização matemática baseada na média, que neste caso é 43, e o desvio padrão, que é de 12. ")
    
    # Calcular média e desvio padrão para a normal teórica
    media = df["Age"].mean()
    desvio = df["Age"].std()

    # Criar histograma e distribuição empírica
    fig = ff.create_distplot(
        [df["Age"]], 
        group_labels=["Distribuição Normal Empírica"], 
        show_hist=True,  
        show_rug=False,  
        bin_size=2, 
        colors = ['#f38c79']
    )

    # Gerar curva da normal teórica
    x = np.linspace(min(df["Age"]), max(df["Age"]), 100)
    y = norm.pdf(x, media, desvio)

    # Adicionar linha da normal teórica ao gráfico
    fig.add_trace(go.Scatter(
        x=x, 
        y=y, 
        mode='lines',
        name='Distribuição Normal Teórica',
        line=dict(color='turquoise', dash='dash')
    ))

    # Layout do gráfico
    fig.update_layout(
        title="Gráfico de Distribuição Normal",
        xaxis_title="Idade",
        yaxis_title="Densidade de Probabilidade",
        template="plotly_white"
    )

    # Exibir gráfico no Streamlit
    st.plotly_chart(fig)

    st.write("Percebemos que, embora as distribuições sejam relativamente semelhantes, há uma ligeira assimetria à esquerda, indicando que a maioria das clientes que deixam comentários no e-commerce estão abaixo da média, ou seja, são mulheres consideravelmente mais jovens.")
    st.write("Caso tentássemos prever a idade da próxima mulher que realizará uma compra e deixará um comentário, utilizaríamos a distribuição normal empírica, que indicaria que a idade mais provável seria mais próxima dos 39 anos do que dos 43. Essa diferença sugere que o público-alvo deste e-commerce tende a ser mais jovem, o que pode fornecer 'insights' valiosos para futuras decisões de marketing e estratégias de design, permitindo um direcionamento mais eficaz das campanhas e a criação de uma experiência de compra mais personalizada.")


elif pages =="Conclusão":
    st.markdown("<h3 style='color: #F38C79;'>Conclusão</h3>", unsafe_allow_html=True)
    st.write("A base de dados apesar de não ser gigante, é grande o suficiente para realizar análises e conclusões interessantes. Apesar de não ter sido possivel responder a todas as perguntas nestá análise, porém pudemos responder algumas.")
    st.write("Uma das colunas mais avaliadas foi sobre a idade, com ela percebemos a maior parte do público feminino que avalia está na idade adulta, além de percebemos na prática que as clientes que mais avaliam estão na faixa etaria de 30-39 anos. Ficamos supresos com a presença de comentáricos de contas de mulheres com mais de 70 anos, são poucos, porém existem. Com essas informações em mãos, podemos melhorar o marketing da plataforma, ou melhorar a experiência das pessoas de 70+ com a plataforma.")
    st.write("Além disso, descobrimos que a probabilidade de quem comenta recomendar a roupa é alta, e há uma correlação entre a nota e a recomendação.")
    st.write("No futuro, espero poder realizar análises mais detalhadas relacionadas aos departamentos, identificando quais têm as melhores avaliações e recomendações, além de explorar diferentes tipos de roupas. Também espero poder responder às demais perguntas levantadas no início dessa análise.")
    st.write("Thaís L. - RM553892")
