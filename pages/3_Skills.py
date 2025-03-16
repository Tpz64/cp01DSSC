import streamlit as st

st.markdown("<h2 style='color: #F38C79;'>Skills</h2>", unsafe_allow_html=True)
#st.header("Skills")

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

col1,col3 = st.columns([0.5,0.5])

col1.markdown("<h3 style='color: #F38C79;'><em>Idiomas<em></h3>", unsafe_allow_html=True)
#col1.subheader("*Idiomas*")
col1.markdown("""
- Português nativo
- Espanhol Avançado
- Inglês Intermediario
""")

col3.markdown("<h3 style='color: #F38C79;'><em>Tecnologias e Ferramentas<em></h3>", unsafe_allow_html=True)
#col3.subheader("*Tecnologias e Ferramentas*")
col3.markdown("""
- Python
- Java
- HTML, CSS e JavaScript
- React
              
""")

col1.markdown("<h3 style='color: #F38C79;'><em>Soft Skills<em></h3>", unsafe_allow_html=True)
#col1.subheader("*Soft Skills*")
col1.markdown("""
- Consistente
- Colaborativo
- Engajado
- Resiliente
- Original
- Pragmático
""")

col3.markdown("<h3 style='color: #F38C79;'><em>Outras Competências<em></h3>", unsafe_allow_html=True)
#col3.subheader("*Outras Competências*")
col3.markdown("""
- Pacote Office
- Kanban
- Scrum
- Design Thinking
""")

