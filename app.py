import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# --- FUNÇÃO PARA BLINDAR O ÁUDIO CONTRA O BLOQUEIO DO STREAMLIT ---
def renderizar_audio_seguro(caminho, cor_borda, cor_fundo_hover, cor_texto_hover, fonte, texto):
    if os.path.exists(caminho):
        with open(caminho, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        
        html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=Lora:ital,wght@0,400;0,600&display=swap');
                body {{
                    margin: 0; display: flex; justify-content: center; align-items: center; background-color: transparent;
                }}
                .btn-audio {{
                    background: transparent; border: 1px solid {cor_borda}; color: {cor_borda};
                    padding: 8px 20px; border-radius: 20px; cursor: pointer;
                    font-family: {fonte}; font-size: 1rem; transition: background-color 0.3s, color 0.3s;
                    text-transform: uppercase; letter-spacing: 1px; outline: none;
                }}
                .btn-audio:hover {{
                    background-color: {cor_fundo_hover}; color: {cor_texto_hover};
                }}
            </style>
        </head>
        <body>
            <audio id="player" loop>
              <source src="data:audio/mp3;base64,{b64}" type="audio/mpeg">
            </audio>
            <button class="btn-audio" onclick="var a=document.getElementById('player'); if(a.paused){{a.play(); this.innerText='PAUSAR TRILHA';}} else {{a.pause(); this.innerText='{texto.upper()}';}}">▶ {texto.upper()}</button>
        </body>
        </html>
        """
        components.html(html_code, height=60)

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Caderno Didático: GPT",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INICIALIZAÇÃO DE VARIÁVEIS DE ESTADO ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'mundo_invertido' not in st.session_state:
    st.session_state.mundo_invertido = False
if 'reset_scroll' not in st.session_state:
    st.session_state.reset_scroll = False

# --- CONTROLE DE MODO NOTURNO (PADRÃO ATIVADO) ---
col_vazia, col_toggle = st.columns([8, 2])
with col_toggle:
    modo_noturno = st.toggle("Modo Noturno", value=True)

# --- CONTROLE DE NAVEGAÇÃO E SCROLL ---
def alternar_dimensao():
    st.session_state.mundo_invertido = not st.session_state.mundo_invertido
    st.session_state.reset_scroll = True

# Script para rolar ao topo com atraso controlado
if st.session_state.reset_scroll:
    components.html("""
    <script>
        setTimeout(function() {
            var mainNode = window.parent.document.querySelector('.main');
            var stMain = window.parent.document.querySelector('[data-testid="stMain"]');
            var appContainer = window.parent.document.querySelector('[data-testid="stAppViewContainer"]');
            if (mainNode) mainNode.scrollTo({top: 0, behavior: 'instant'});
            if (stMain) stMain.scrollTo({top: 0, behavior: 'instant'});
            if (appContainer) appContainer.scrollTo({top: 0, behavior: 'instant'});
            window.parent.scrollTo({top: 0, behavior: 'instant'});
        }, 150);
    </script>
    """, height=0)
    st.session_state.reset_scroll = False

# --- VARIÁVEIS DE TEMA ---
if modo_noturno:
    bg_app = "#121212"
    bg_paper = "#1a1a1a"
    color_text = "#d4d4d4"
    color_title = "#ffffff"
    color_accent = "#d47272"
    color_border = "#333333"
    bg_img_box = "#222222"
    bg_dossie = "#141414"
    color_dossie_text = "#b0b0b0"
else:
    bg_app = "#f4f1ea"          
    bg_paper = "#fcfbf8"        
    color_text = "#333333"
    color_title = "#1c1c1c"
    color_accent = "#823636"    
    color_border = "#d1cabc"
    bg_img_box = "#f5f3ec"
    bg_dossie = "#e8e3d3"
    color_dossie_text = "#2b2b2b"

# ==============================================================================
# 🔒 TELA DE LOGIN (BARREIRA DE ACESSO ULTRA MINIMALISTA)
# ==============================================================================
if not st.session_state.autenticado:
    
    img_login_b64_html = ""
    if os.path.exists("login.jpg"):
        with open("login.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        img_login_b64_html = f'<img src="data:image/jpeg;base64,{encoded_string}" class="id-photo">'
    
    st.markdown(f"""
    <style>
        .stApp {{ background-color: {bg_app} !important; transition: background-color 0.3s; }}
        header {{ visibility: hidden !important; }}
        h1 {{ color: {color_title} !important; font-family: 'Playfair Display', serif !important; text-align: center; }}
        
        .login-box {{ max-width: 400px; margin: 5rem auto; padding: 2.5rem 2rem; background-color: {bg_paper}; border: 1px solid {color_border}; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border-radius: 8px; text-align: center; }}
        
        .id-photo {{
            width: 120px !important;
            aspect-ratio: 3 / 4 !important;
            object-fit: cover !important;
            display: block !important;
            margin: 0 auto 1.5rem auto !important;
            border: 1px solid {color_border} !important;
            border-radius: 4px !important;
        }}
        
        .stButton > button {{ background-color: transparent !important; border: 1px solid {color_accent} !important; color: {color_accent} !important; width: 100% !important; padding: 10px !important; text-transform: uppercase !important; letter-spacing: 2px !important; transition: 0.3s; margin-top: 1.5rem; font-family: 'Lora', serif !important;}}
        .stButton > button:hover {{ background-color: {color_accent} !important; color: {bg_paper} !important; }}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    
    if img_login_b64_html:
        st.markdown(img_login_b64_html, unsafe_allow_html=True)
        
    st.markdown("<h1 style='font-size: 2.2rem; margin-bottom: 2rem; margin-top:0;'>Acesso Restrito</h1>", unsafe_allow_html=True)
    
    senha_digitada = st.text_input("Senha", type="password", label_visibility="collapsed", placeholder="digite a senha (bomdia)")
    
    if st.button("Entrar"):
        if senha_digitada == "bomdia":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Senha incorreta. Acesso negado.")
            
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ==============================================================================
# 📁 LADO B: O GUIA DO PROFESSOR (Dossiê Confidencial)
# ==============================================================================
if st.session_state.mundo_invertido:
    st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    .stApp {{ background-color: {bg_app} !important; transition: background-color 0.3s; }}
    .block-container {{ max-width: 900px !important; padding: 4rem 5rem !important; background-color: {bg_dossie} !important; border: 3px solid {color_border} !important; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4) !important; }}
    h1, h2, h3, p, span, div, li {{ color: {color_dossie_text} !important; font-family: 'Special Elite', monospace !important; background: transparent !important; }}
    .dossie-texto {{ font-size: 1.25rem !important; line-height: 1.8 !important; text-align: justify !important; margin-bottom: 1.5rem !important; text-indent: 0 !important; }}
    .carimbo {{ color: #b32424 !important; border: 4px solid #b32424 !important; padding: 10px 20px !important; font-size: 3rem !important; text-transform: uppercase !important; transform: rotate(-3deg); display: inline-block !important; margin-bottom: 2rem !important; opacity: 0.8 !important;}}
    .marca-texto {{ background-color: #e6d97e !important; color: #111 !important; padding: 0 5px !important; }}
    .censura {{ background-color: #1a1a1a !important; color: #1a1a1a !important; padding: 0 5px !important; border-radius: 2px; transition: 0.3s; }}
    .censura:hover {{ color: #fff !important; cursor: help; }}
    header, footer {{ visibility: hidden !important; }}
    .stButton > button {{ background-color: transparent !important; color: #b32424 !important; border: 2px dashed #b32424 !important; width: 100% !important; font-family: 'Special Elite', monospace !important; font-size: 1.2rem !important; padding: 1rem !important; transition: 0.3s; margin-top: 2rem;}}
    .stButton > button:hover {{ background-color: #b32424 !important; color: {bg_dossie} !important; }}
    
    /* Estilo do Botão de Download PDF */
    .btn-pdf-b {{ background-color: transparent !important; color: {color_dossie_text} !important; border: 1px solid {color_border} !important; padding: 10px 20px !important; font-family: 'Special Elite', monospace !important; font-size: 1rem !important; cursor: pointer; transition: 0.3s; width: auto; display: block; margin: 0 auto; border-radius: 4px; }}
    .btn-pdf-b:hover {{ background-color: {color_border} !important; color: {bg_dossie} !important; }}

    /* Ocultar elementos desnecessários na hora de imprimir */
    @media print {{
        .stButton, .btn-pdf-b, iframe, div[data-testid="stToolbar"] {{ display: none !important; }}
        .block-container {{ border: none !important; box-shadow: none !important; max-width: 100% !important; padding: 0 !important; }}
        body, .stApp {{ background-color: transparent !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }}
    }}
    
    @media (max-width: 768px) {{ .block-container {{ padding: 2rem 1.5rem !important; border: 2px solid {color_border} !important;}} .carimbo {{ font-size: 2rem !important; }} .dossie-texto {{ font-size: 1.1rem !important; }} }}
</style>
""", unsafe_allow_html=True)

    st.markdown('<div style="text-align:center;"><div class="carimbo">Arquivo Confidencial</div></div>', unsafe_allow_html=True)
    
    renderizar_audio_seguro("audio_lado_b.mp3", "#b32424", "#b32424", bg_dossie, "'Special Elite', monospace", "Ouvir Trilha")

    st.markdown('<h2 style="border-bottom: 2px solid #b32424; padding-bottom:10px; margin-bottom: 2rem;">Capítulo 1: O Portão</h2>', unsafe_allow_html=True)
    
    st.markdown('''
<p class="dossie-texto">A maioria das pessoas vive sem saber de um segredo essencial: o peso das coisas não é o mesmo em todos os lugares.</p>
<p class="dossie-texto">Quem trabalha em Escola sabe disso. E eu, Professor de Educação Física, deveria até saber mais que todo mundo. Eu estava prestes a testemunhar, mais uma vez, as consequências desse fenômeno.</p>
<p class="dossie-texto">Mas antes de contar o que aconteceu, preciso explicar uma coisa.</p>
<p class="dossie-texto">O "Ranca" não é uma simples brincadeira. Não é uma pelada desorganizada. O Ranca é uma força da natureza. <span class="marca-texto">O Ranca não tem MÃE!</span> É Um evento espontâneo com poderes magnéticos, capaz de atrair corpos desavisados e os envolver num ritual de suor, gritos e dedões do pé dilacerados. <span class="censura">“Toca essa bola, C@#$%%0!!!”</span></p>
<p class="dossie-texto">Sabendo disso ou não, lá fui eu.</p>
<p class="dossie-texto">Era o primeiro dia de tentativa de apresentar o projeto de Ginástica Para Todos para os alunos do Integral. Fui de sala em sala no horário do almoço, quando os alunos ainda não tinham terminado de comer, além dos que encontrava pelos corredores. O plano era simples: convidar todo mundo para ir até o auditório, fazer uma demonstração, explicar o que é a Ginástica Para Todos e tentar conquistar aquele povo para a nova prática. Porque nada conquista mais um adolescente do ensino integRal do que interromper a única pausa que ele tem no dia para falar sobre atividade física.</p>
<p class="dossie-texto">Fui. Salas visitadas, alunos abordados, convites feitos. Tudo dentro do planejado. Dialógico.</p>
<p class="dossie-texto" style="text-align: center; font-size: 1.5rem; margin: 3rem 0; font-weight:bold;">Às onze e meia da manhã do dia dez de março, testemunhei o inevitável.</p>
<p class="dossie-texto" style="text-align: center; font-size: 2rem; color: #b32424 !important; font-weight:bold; transform: rotate(1deg);">Alguém abriu o portão da quadra.</p>
<p class="dossie-texto">Não foi um evento grandioso. Não teve anúncio, não teve alarde. Foi só um portão se abrindo. Mas, para quem tem intimidade com escola, sabe que aquilo é equivalente ao sinal do recreio em dia que a merenda é cachorro-quente. Mais que depressa, a maioria dos alunos bateu em retirada. Não foi desinteresse, não foi maldade. Foi pura e simplesmente a força da gravidade local agindo. Eles correram para a quadra em busca de outra dose para saciar a coceira das pernas. O Ranca.</p>
<p class="dossie-texto">Lá no auditório, esperei. E esperei. E continuei esperando.</p>
<p class="dossie-texto">No final, alguns poucos alunos restaram. Não eram necessariamente os mais interessados em ginástica. Eram, muito provavelmente, os que sentiram vergonha de me deixar falando sozinho. Eles ficaram até o fim, ouviram a explicação inteira, nunca tinha testemunhado tamanha delicadeza, alguns até acenaram com a cabeça em momentos estratégicos.</p>
<p class="dossie-texto">Lá fora, no chão quente da quadra, o Ranca rugia.</p>
<p class="dossie-texto">E eu entendi, naquele dia, que o universo tem suas próprias leis. Você pode planejar, convidar, explicar, demonstrar. Pode ir de sala em sala no horário do almoço, abordar aluno por aluno nos corredores. Pode ser o sujeito mais otimista e sonhador da face da Terra.</p>
<p class="dossie-texto">Mas se alguém abrir o portão da quadra, não adianta.</p>
<p class="dossie-texto" style="font-size:2.5rem; text-align: center; margin-top: 3rem; color: #b32424 !important; font-weight:bold;">O Ranca é inevitável!</p>
''', unsafe_allow_html=True)

    st.markdown('<div style="text-align:center; margin-top: 4rem; margin-bottom: 1rem;"><button onclick="window.print()" class="btn-pdf-b">Baixar Dossiê (PDF)</button></div>', unsafe_allow_html=True)

    st.button("FECHAR DOSSIÊ E VOLTAR AO RELATÓRIO", on_click=alternar_dimensao)

# ==============================================================================
# LADO A: O CADERNO DIDÁTICO (A Poesia do Movimento)
# ==============================================================================
else:
    st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=Lora:ital,wght@0,400;0,600;1,400;1,600&display=swap');
    .stApp {{ background-color: {bg_app} !important; transition: background-color 0.3s; }}
    .block-container {{ max-width: 1150px !important; padding: 6rem 5rem !important; background-color: {bg_paper} !important; box-shadow: 0 25px 70px rgba(0,0,0,0.08) !important; border: 3px solid {color_border} !important; transition: background-color 0.3s; }}
    h1, h2, h3, h4 {{ color: {color_title} !important; font-family: 'Playfair Display', serif !important; background: transparent !important; }}
    p, span, div, li {{ color: {color_text} !important; font-family: 'Lora', serif !important; background: transparent !important; }}
    .quebra-pagina {{ margin: 6rem 0; border: none; border-top: 1px solid {color_border}; opacity: 0.7; }}
    .ornamento {{ text-align: center; color: {color_border}; font-size: 2.5rem; margin: 2rem 0; line-height: 0; }}
    .titulo-capa {{ font-size: 3.5rem !important; font-weight: 700 !important; text-align: center !important; line-height: 1.2 !important; margin-bottom: 1rem !important; }}
    .subtitulo-capitulo {{ font-size: 2.2rem !important; color: {color_accent} !important; border-bottom: 1px solid {color_border} !important; padding-bottom: 0.8rem !important; margin-top: 1rem !important; margin-bottom: 2.5rem !important; font-style: italic !important;}}
    .dropcap::first-letter {{ float: left !important; font-size: 5rem !important; line-height: 0.8 !important; padding-top: 8px !important; padding-right: 12px !important; color: {color_accent} !important; font-weight: 700 !important; }}
    .texto {{ text-align: justify !important; font-size: 1.2rem !important; line-height: 1.8 !important; margin-bottom: 1.5rem !important; text-indent: 0 !important; }}
    .box-imagem-paisagem {{ aspect-ratio: 16 / 9; background-color: {bg_img_box} !important; border: 1px dashed #bbb !important; border-radius: 4px !important; display: flex !important; flex-direction: column !important; justify-content: center !important; align-items: center !important; width: 100% !important; margin: 1rem 0 0.5rem 0 !important; padding: 10px !important; }}
    .box-imagem-retrato {{ aspect-ratio: 9 / 16; background-color: {bg_img_box} !important; border: 1px dashed #bbb !important; border-radius: 4px !important; display: flex !important; flex-direction: column !important; justify-content: center !important; align-items: center !important; width: 100% !important; margin: 1rem 0 0.5rem 0 !important; padding: 10px !important; }}
    .legenda-img {{ font-size: 0.95rem !important; color: #777 !important; text-align: center !important; font-style: italic !important; margin-bottom: 2rem !important; font-family: 'Lora', serif !important; }}
    .ficha-catalografica-container {{ font-family: 'Times New Roman', Times, serif !important; color: {color_text} !important; max-width: 650px; margin: 4rem auto; font-size: 1rem; text-indent: 0 !important;}}
    .ficha-box {{ border: 1px solid {color_text} !important; padding: 1.5rem; display: flex; margin-top: 1.5rem; margin-bottom: 1.5rem; }}
    .ficha-texto {{ font-family: 'Times New Roman', Times, serif !important; color: {color_text} !important; }}
    .epigrafe-container {{ text-align: center; margin-bottom: 2rem; }}
    .epigrafe-texto {{ font-family: 'Playfair Display', serif !important; font-size: 1.1rem !important; font-style: italic !important; color: {color_accent} !important; line-height: 1.4 !important; margin-bottom: 0.5rem !important; text-indent: 0 !important;}}
    .epigrafe-autor {{ font-family: 'Lora', serif !important; font-size: 0.85rem !important; color: #777 !important; text-transform: uppercase; letter-spacing: 1px; text-indent: 0 !important;}}
    header, footer {{ visibility: hidden !important; }}
    .stButton > button {{ background-color: transparent !important; border: 1px solid {color_border} !important; color: {color_accent} !important; width: 100% !important; padding: 20px !important; text-transform: uppercase !important; letter-spacing: 2px !important; transition: 0.3s; margin-top: 2rem;}}
    .stButton > button:hover {{ background-color: {color_accent} !important; color: {bg_paper} !important; }}
    
    /* Estilo do Botão de Download PDF */
    .btn-pdf-a {{ background-color: transparent !important; color: {color_text} !important; border: 1px solid {color_border} !important; padding: 10px 20px !important; font-family: 'Lora', serif !important; font-size: 1rem !important; cursor: pointer; transition: 0.3s; width: auto; display: block; margin: 0 auto; border-radius: 4px; text-transform: uppercase; letter-spacing: 1px;}}
    .btn-pdf-a:hover {{ background-color: {color_border} !important; color: {bg_paper} !important; }}

    /* Ocultar elementos desnecessários na hora de imprimir */
    @media print {{
        .stButton, .btn-pdf-a, iframe, div[data-testid="stToolbar"] {{ display: none !important; }}
        .block-container {{ border: none !important; box-shadow: none !important; max-width: 100% !important; padding: 0 !important; }}
        body, .stApp {{ background-color: transparent !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }}
    }}

    @media (max-width: 768px) {{ .block-container {{ padding: 2rem 1rem !important; border: 1px solid {color_border} !important; }} .titulo-capa {{ font-size: 2.2rem !important; }} .subtitulo-capitulo {{ font-size: 1.8rem !important; }} .texto {{ font-size: 1.1rem !important; text-indent: 0 !important; }} .dropcap::first-letter {{ font-size: 4rem !important; }} div[data-testid="column"] {{ width: 100% !important; flex: unset !important; }} .ficha-box {{ flex-direction: column; }} }}
</style>
""", unsafe_allow_html=True)

    renderizar_audio_seguro("audio_lado_a.mp3", color_accent, color_accent, bg_paper, "'Lora', serif", "Ouvir Trilha")

    st.markdown('<h1 class="titulo-capa" style="margin-top: 2rem;">RELATÓRIO DA AÇÃO EXTENSIONISTA:<br>ENTRE O PLANEJAR, O FAZER E O SONHAR</h1>', unsafe_allow_html=True)
    
    if os.path.exists("foto_capa.jpg"):
        st.image("foto_capa.jpg", use_container_width=True)
    st.markdown('<div class="legenda-img">Fotografia de Capa: Registro oficial da ação extensionista.</div>', unsafe_allow_html=True)

    st.markdown('<div class="ornamento">❧</div>', unsafe_allow_html=True)
    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown("""
<div class="ficha-catalografica-container">
<div style="text-align: center; margin-bottom: 2rem;">
<strong class="ficha-texto">Organizadores</strong><br>
<span class="ficha-texto">Nome Sobrenome</span><br>
<span class="ficha-texto">Nome Sobrenome</span><br>
<span class="ficha-texto">Nome Sobrenome</span><br><br>
<strong class="ficha-texto">Fotografia</strong><br>
<span class="ficha-texto">Nome Sobrenome</span><br>
<span class="ficha-texto">Nome Sobrenome</span><br><br>
<strong class="ficha-texto">Diagramação</strong><br>
<span class="ficha-texto">Nome Sobrenome</span>
</div>
<div style="text-align: center; font-size: 0.95rem;" class="ficha-texto">Elaborado com os dados fornecidos pelo(a) autor(a).</div>
<div class="ficha-box">
<div style="width: 50px; font-size: 0.9rem;">P745</div>
<div style="flex: 1; font-size: 0.95rem; text-align: justify; line-height: 1.4;">
<span class="ficha-texto">RELATÓRIO DA AÇÃO EXTENSIONISTA: ENTRE O PLANEJAR, O FAZER E O SONHAR / organizadores Nome Sobrenome, Nome Sobrenome, Nome Sobrenome; fotografia Nome Sobrenome, Nome Sobrenome; diagramação Nome Sobrenome. - Diamantina: UFVJM, 2024.</span><br><br>
<span class="ficha-texto">Inclui bibliografia</span><br><br>
<span class="ficha-texto">ISBN: 978-65-00-00000-0</span><br><br>
<span class="ficha-texto">1. Ginástica para todos. 2. Educação Física Escolar. 3. Extensão Universitária. I. Sobrenome, Nome. II. Sobrenome, Nome. III. Sobrenome, Nome. IV. Sobrenome, Nome. V. Sobrenome, Nome. VI. Título. VII. Universidade Federal dos Vales do Jequitinhonha e Mucuri.</span><br><br>
<div style="text-align: right; font-weight: bold;" class="ficha-texto">CDD 372.86</div>
</div>
</div>
<div style="text-align: center; margin-top: 1rem; font-size: 0.95rem; line-height: 1.4;">
<span class="ficha-texto">Ficha Catalográfica – Serviço de Bibliotecas/UFVJM</span><br>
<span class="ficha-texto">Bibliotecária Nome Sobrenome – CRB-6/1234</span>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown('<div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">', unsafe_allow_html=True)
    if os.path.exists("foto_epigrafe.jpg"):
        st.image("foto_epigrafe.jpg", use_container_width=True)
    st.markdown('''
<div class="legenda-img" style="margin-bottom: 3rem;">Figura 1: A leveza e o preparo do movimento.</div>
<div class="epigrafe-container">
<p class="epigrafe-texto">"Enquanto o tempo acelera e pede pressa<br>Eu me recuso, faço hora, vou na valsa<br>A vida é tão rara"</p>
<p class="epigrafe-autor">— Paciência, Lenine</p>
</div>
</div>
''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown('<h2 class="subtitulo-capitulo">Apresentação</h2>', unsafe_allow_html=True)
    st.markdown('''
<p class="texto dropcap">Neste caderno, datas e ponteiros do relógio importam menos do que as transformações que ocorreram nos espaços da Escola Estadual Professora Ayna Torres. A Ginástica para Todos (GPT) não foi apenas uma sequência de aulas práticas; foi um desafio, foi mudança, foi conflito e foi divertido demais!</p>
<p class="texto">Deixamos os relatos cronológicos de lado para organizar nossas memórias através dos sentimentos, das barreiras quebradas e das conquistas coletivas.</p>
''', unsafe_allow_html=True)

    st.markdown('<div class="ornamento">❧</div>', unsafe_allow_html=True)
    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown('<h2 class="subtitulo-capitulo">O Tempo e o Corpo</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.markdown('''
<p class="texto">O tempo no Ensino Médio em Tempo Integral (EMTI) pode ser um rio longo, denso e exaustivo. Permanecer quase dez horas no ambiente escolar exige muito dos estudantes, um esforço que, nas palavras deles, "acaba com qualquer um" e exige muita coluna.</p>
<p class="texto">O longo intervalo do almoço era vencido por corpos sentados, intermináveis partidas de Truco e prática deliberada de Futsal. Não que ficar sentado após o almoço seja algo negativo, na verdade é o fisiologicamente recomendado. Mas intervalo de almoço é verdadeiramente longo e visto como tedioso pelos alunos.</p>
<p class="texto">O convite para o movemento encontrou, de início, a resistência natural de quem teme o novo. No primeiro dia de projeto, quando o portão se abriu, muitos alunos bateram em retirada para a quadra, buscando o conforto das práticas habituais. Mas com insistência, apoio dos bolsistas do PIBID e alguns vídeos legais, a semente da curiosidade foi plantada. Aos poucos, a rotina foi quebrada, e o auditório virou um refúgio de leveza onde o tempo, antes arrastado, passou a voar.</p>
''', unsafe_allow_html=True)
    with col2:
        if os.path.exists("foto_contraste.jpg"):
            st.image("foto_contraste.jpg", use_container_width=True)
        st.markdown('<div class="legenda-img">Figura 2: Alunos entrando no auditório e descobrindo os colchonetes.</div>', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown(f'<h3 style="text-align: center; color: {color_accent} !important; font-style: italic; margin-bottom: 2rem;">Galeria: A Descoberta</h3>', unsafe_allow_html=True)
    
    if os.path.exists("video_descoberta.mp4"):
        with open("video_descoberta.mp4", "rb") as f:
            b64_video = base64.b64encode(f.read()).decode()
        st.markdown(f'''
        <div class="box-imagem-paisagem">
            <video autoplay loop muted playsinline style="width: 100%; border-radius: 4px; pointer-events: none;">
                <source src="data:video/mp4;base64,{b64_video}" type="video/mp4">
            </video>
        </div>
        ''', unsafe_allow_html=True)
        
    st.markdown('<div class="legenda-img">Registro 1: O auditório ganhando vida em movimento.</div>', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown('<h2 class="subtitulo-capitulo">Vencendo o Medo do Desconhecido e o Preconceito</h2>', unsafe_allow_html=True)
    st.markdown('''
<p class="texto">Talvez a maior acrobacia realizada neste projeto não tenha sido física. O colchonete revelou que muitos de nós somos prisioneiros dos nossos próprios medos. Os alunos descobriram que o bloqueio mental é o verdadeiro causador de lesões: quando a gente evita o movimento por medo de se machucar, acaba se machucando.</p>
<p class="texto">Havia preconceito a ser quebrados. O julgamento da sociedade pesava, rotulando quem praticava a ginástica com termos pejorativos. As meninas e os meninos enfrentavam o medo da sexualização e do olhar malicioso diante do básico: posições de quatro apoios e espacates, consideradas equivocadamente “vulgares”.</p>
<p class="texto">O projeto foi o martelo que estilhaçou todo reflexo do olhar maldoso lá de fora. O ambiente seguro mostrou que a malícia habita a mente de quem assiste, e não a pureza do movimento. Eles aprenderam que a escola é exatamente o lugar para se abrir a cabeça e derrubar essas barreiras.</p>
''', unsafe_allow_html=True)
    
    if os.path.exists("foto_superacao.jpg"):
        st.image("foto_superacao.jpg", use_container_width=True)
    st.markdown('<div class="legenda-img">Figura 3: O sorriso após superar o medo da primeira acrobacia.</div>', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown('<h2 class="subtitulo-capitulo">Construindo o Coletivo: Paciência</h2>', unsafe_allow_html=True)
    st.markdown('''
<p class="texto">Diferente da frieza das competições tradicionais, a GPT não carrega a balança dos jurados, as notas ou a rivalidade que cria inimizades. Sem a pressão de ser o melhor, o que floresceu foi a empatia.</p>
<p class="texto">O corpo aprendeu novas rimas: pontes, velas, rolamentos à frente, saltos grupados, afastados e a execução precisa da estrelinha. Mas a alma aprendeu a virtude da paciência. A orientação calma ensinou os alunos a terem cautela com a dificuldade do outro. Rapidamente, eles mesmos começaram a se ajudar e a compreender que ninguém é igual a ninguém.</p>
<p class="texto">As coreografias geométricas não foram apenas demonstrações físicas, mas a prova de que cada corpo, com seu próprio ritmo, é essencial para manter a figura acrobática em pé. A ginástica uniu diferenças em um só movimento, respeitando o espaço e o limite de cada um.</p>
''', unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="large")
    with col3:
        if os.path.exists("foto_apoio.jpg"):
            st.image("foto_apoio.jpg", use_container_width=True)
        st.markdown('<div class="legenda-img">Figura 4: Alunos se divertindo.</div>', unsafe_allow_html=True)
    with col4:
        if os.path.exists("foto_roda.jpg"):
            st.image("foto_roda.jpg", use_container_width=True)
        st.markdown('<div class="legenda-img">Figura 5: Preenchimento dos TCLEs em roda.</div>', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown(f'<h3 style="text-align: center; color: {color_accent} !important; font-style: italic; margin-bottom: 2rem;">Galeria: O Movimento Coletivo</h3>', unsafe_allow_html=True)
    
    g_col1, g_col2 = st.columns(2, gap="large")
    with g_col1:
        if os.path.exists("foto_movimento_1.jpg"):
            st.image("foto_movimento_1.jpg", use_container_width=True)
        st.markdown('<div class="legenda-img">Figura 6: Formação geométrica em grupo.</div>', unsafe_allow_html=True)
    with g_col2:
        if os.path.exists("foto_movimento_2.jpg"):
            st.image("foto_movimento_2.jpg", use_container_width=True)
        st.markdown('<div class="legenda-img">Figura 7: Sincronia e movimento coletivo.</div>', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown('<h2 class="subtitulo-capitulo">A Semente: O Futuro da GPT na Escola</h2>', unsafe_allow_html=True)
    st.markdown('''
<p class="texto">O fim do projeto é, na verdade, um começo. Transformados pela flexibilidade que ganharam no corpo e na mente, os alunos sonham mais alto.</p>
<p class="texto">Há um desejo de plantar essa semente, levando a GPT para as crianças do 6º ano do ensino fundamental. Eles sabem que corpos mais jovens absorvem o movimento mais rápido e que mentes mais novas podem crescer blindadas contra os preconceitos que eles próprios tiveram que desconstruir.</p>
<p class="texto">E o auditório da escola já ficou pequeno. O novo sonho pulsa nas ruas da cidade: há o desejo de levar as coreografias para além dos muros da escola, nas aglomerações da cidade aos finais de semana. Apresentar a poesia da GPT para a comunidade é a forma definitiva de mostrar que a ginástica é verdadeiramente PARA TODOS.</p>
''', unsafe_allow_html=True)

    if os.path.exists("foto_final.jpg"):
        st.image("foto_final.jpg", use_container_width=True)
    st.markdown('<div class="legenda-img">Figura 8: Encerramento do projeto. Ginástica para Todos!</div>', unsafe_allow_html=True)

    st.markdown('<div style="text-align:center; margin-top: 4rem; margin-bottom: 1rem;"><button onclick="window.print()" class="btn-pdf-a">Baixar Caderno (PDF)</button></div>', unsafe_allow_html=True)

    st.markdown(f'<div style="margin-top: 2rem; text-align: center; border-top: 1px dashed {color_border}; padding-top:4rem;">', unsafe_allow_html=True)
    st.button("ACESSAR ANEXO CONFIDENCIAL", on_click=alternar_dimensao)
    st.markdown('</div>', unsafe_allow_html=True)
