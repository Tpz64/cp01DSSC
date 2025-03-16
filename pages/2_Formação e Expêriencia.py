import streamlit as st

st.markdown("<h2 style='color: #F38C79;'>Formação e Experiência</h2>", unsafe_allow_html=True)
#st.header("Formação e Expêriencia")
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

#Cursos
st.markdown("<h3 style='color: #F38C79;'><em>Formação Acadêmica:<em></h3>", unsafe_allow_html=True)
#st.subheader("*Formação Acadêmica:*")
st.write('- Engenharia de Software - Fiap - Previsão de conculsão para junho de 2027')

st.markdown("<h3 style='color: #F38C79;'><em>Certificações:<em></h3>", unsafe_allow_html=True)
#st.subheader("*Certificações:*")
st.write("- Nano Course: Design Thinking - Process - OUT/2023")
st.write("- Nano Course: Formação Social e Sustentabilidade - MAI/2024")
st.write("- Nano Course: Gestão Financeira de Empresa - MAI/2024")

st.markdown("<h3 style='color: #F38C79;'><em>Projetos Acadêmicos:<em></h3>", unsafe_allow_html=True)
#st.subheader("Projetos Acadêmicos")
with st.expander("Health Tech Experience - FIAP – agosto de 2023 a junho de 2024"):
  st.write("Junto a uma equipe, criamos um projeto de humanização para o Instituto da Criança e do Adolescente do hospital das Clínicas de São Paulo utilizando HTML, CSS e Javascript. Desenvolvemos uma biblioteca virtual com histórias interativas para explicar sobre os exames, chamada MedEduca. Fomos um dos finalistas do NEXT 2024.")
with st.expander("Global Solution Green Energy - FIAP – novembro de 2024"):
  st.write("Com foco na energia verde, e aliada a um amigo, desenvolvemos o EcoChain. Um projeto para melhorar o monitoramento e gestão de poda de árvores. A solução fortalece a comunicação entre concessionárias de energia e prefeituras, garantindo eficiência desde a solicitação inicial até o descarte sustentável dos resíduos, que são reaproveitados na produção de biomassa para a geração de energia verde. Foi um dos projetos vencedores da Global Solution.")

st.markdown("<h3 style='color: #F38C79;'><em>Experiências Relevantes:<em></h3>", unsafe_allow_html=True)
#st.subheader("*Experiências Relevantes:*")
with st.expander("República Dominicana"):
  st.write("Durante o anos de 2018-2023, vivi na República Dominicana, um país que fica no caribe, e faz fronteira terrestre com o Haiti. Foi uma experiência que me fez desenvolver em várias áreas da minha vida e vivi coisas que nunca imaginei. Além de aprender o idioma, que é o espanhol, acabei participando de diversas atividades no país, como voluntariado voltado para politicas verdes.")
with st.expander("JVA"):
  st.write("Durante o período de 2019-2023 fiz parte da JVA - Jovenes Verdes de las Américas. Apesar de ser brasileira, por estar residindo naquele momento na República Dominicana, era representante deste país. Foi super importante na minha vida, pois além de me desenvolver pessoalmente, praticando os idiomas que hoje falo, pude participar de diversos projetos internacionais, entre eles o Programa de Liderança Verde, na qual criamos um projeto chamado 'La Luz Verde'. Além disso, participei de varios congressos, sendo a maioria realizados na República Dominicana, onde trabalhei na organização e planejamento.")
with st.expander("Global Young Green"):
  st.write("Durante o ano de 2020, fiz parte do Global Young Green, fazendo parte da comissão que revisava os estatutos da organização. Foi um dos maiores desafios que enfrentei naquele momento, porque era a representante das américas, e me comunicava semanalmente com representantes de diversos países, representantes de todos os continentes. ")
