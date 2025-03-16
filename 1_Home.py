import streamlit as st
#from streamlit_extra.app_logo import add_logo

#configuração da página
st.set_page_config(page_title="Thaís Leoncio", layout="wide")

#sidebar
#criando sub-abas(pages)
pages = st.sidebar.selectbox("Escolha o Idioma:", [
    "Português",
    "Español",
    "English"
])
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

#teste de algo
st.markdown(
    """
    <style>
    .header-container {
        background-color: #FAD0C4;
        padding: 32px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .info-container {
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .info-container img {
        width: 20px;
        height: 20px;
    }
    .name-bar {
        background-color: #F38C79;
        color: white;
        padding: 15px;
        font-size: 25px;
        font-weight: bold;
        border-radius: 10px;
        text-align: center;
        margin-top: 0px;
        margin-bottom: 10px;
    }
    .profile-pic {
        width: 80px;
        height: 80px;
        border-radius: 25px;
        object-fit: cover;
        border: 3px solid white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 3])  # Criando colunas para imagem e informações

with col1:
    st.image("imgs/foto_tgl.jpg", width=400)

with col2:
    st.markdown('<div class="name-bar">Thaís Gonçalves Leoncio</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-container header-container">
            <span>📧  thaisgleoncio@gmail.com</span>
            <span>📞  +55 (11) 99999 1111</span>
            <span>📍  Guarulhos - SP</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)


#body 

if pages == "Português":
    st.markdown("<h3 style='color: #F38C79;'>Informações Pessoais</h3>", unsafe_allow_html=True)
    #st.subheader("Informações Pessoais")
    st.write("Olá a todos! Meu nome é Thaís, tenho 25 anos e atualmente estudo Engenharia de Software na FIAP. Viajar pelo mundo é um dos meus grandes sonhos, e passar o máximo de tempo possível com minha família é o que mais gosto de fazer.")
    st.write("Minha personalidade é a de uma idealista que luta pelo que acredita. Sou observadora, calma e agradável. À primeira vista, posso parecer tímida e reservada, mas, por dentro, sou repleta de emoções. Tenho um olhar atento para identificar o que precisa ser corrigido e sou muito boa em reconhecer talentos e ajudar as pessoas a alcançarem o sucesso. Conectar indivíduos em torno de uma mesma ideia é algo que faço com entusiasmo. Adoro mudanças e estou sempre em busca de novidades. No entanto, preciso ter cuidado para não me perder em meus pensamentos enquanto a vida acontece ao meu redor.")

    #st.subheader("Objetivo Profissional")
    st.markdown("<h3 style='color: #F38C79;'>Objetivo Profissional</h3>", unsafe_allow_html=True)
    st.write("Conquistar um estágio na área de tecnologia e aprender algo novo a cada dia.")

elif pages == "Español": 
    st.markdown("<h3 style='color: #F38C79;'>Información Personal</h3>", unsafe_allow_html=True)
    #st.subheader("Información Personal")
    st.write("¡Hola a todos! Me llamo Thaís, tengo 25 años y actualmente estudio Ingeniería de Software en FIAP. Viajar por el mundo es uno de mis mayores sueños, y pasar el mayor tiempo posible con mi familia es lo que más disfruto.")
    st.write("Mi personalidad es la de una idealista que lucha por lo que cree. Soy observadora, tranquila y agradable. A primera vista, puedo parecer tímida y reservada, pero por dentro, tengo muchas emociones. Tengo un ojo atento para identificar lo que necesita mejorarse y soy muy buena en reconocer los talentos de las personas y ayudarlas a alcanzar el éxito. Unir a las personas en torno a una misma idea es algo que realmente disfruto. Me encantan los cambios y siempre busco nuevas experiencias. Sin embargo, debo tener cuidado de no perderme en mis pensamientos mientras la vida transcurre a mi alrededor.")
    #st.subheader("Objetivos Profissional")
    st.markdown("<h3 style='color: #F38C79;'>Objetivo Profissional</h3>", unsafe_allow_html=True)
    st.write("Conseguir una pasantía en el área de tecnología y aprender algo nuevo cada día.")

elif pages == "English":
    #st.subheader("Personal Information")
    st.markdown("<h3 style='color: #F38C79;'>Personal Information</h3>", unsafe_allow_html=True)
    st.write("Hello everyone! My name is Thaís, I am 25 years old, and I am currently studying Software Engineering at FIAP. Traveling the world is one of my biggest dreams, and spending as much time as possible with my family is what I enjoy the most.")
    st.write("My personality is that of an idealist who fights for what they believe in. I am observant, calm, and pleasant. At first glance, I may seem shy and reserved, but inside, I am full of emotions. I have a keen eye for identifying what needs to be improved, and I am very good at recognizing people’s talents and helping them succeed. Bringing people together around a common idea is something I truly enjoy. I love change and am always looking for new experiences. However, I must be careful not to get lost in my thoughts while life unfolds around me.")
    #st.subheader("Professional Goal")
    st.markdown("<h3 style='color: #F38C79;'>Professional Goal</h3>", unsafe_allow_html=True)
    st.write("To secure an internship in the technology field and learn something new every day.")