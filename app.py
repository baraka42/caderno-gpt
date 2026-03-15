import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Caderno Didático: GPT",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CONTROLE DE NAVEGAÇÃO E SCROLL ---
if 'mundo_invertido' not in st.session_state:
    st.session_state.mundo_invertido = False
if 'reset_scroll' not in st.session_state:
    st.session_state.reset_scroll = False

def alternar_dimensao():
    st.session_state.mundo_invertido = not st.session_state.mundo_invertido
    st.session_state.reset_scroll = True

if st.session_state.reset_scroll:
    components.html("<script>window.parent.document.querySelector('.main').scrollTo({top: 0, behavior: 'smooth'});</script>", height=0)
    st.session_state.reset_scroll = False

# ==============================================================================
# 📁 LADO B: O GUIA DO PROFESSOR (Dossiê Confidencial)
# ==============================================================================
if st.session_state.mundo_invertido:
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    .stApp { background-color: #3b3a36 !important; }
    .block-container {
        max-width: 900px !important; padding: 4rem 5rem !important;
        background-color: #f4ecd8 !important;
        border: 1px solid #d1c7b7 !important; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4) !important;
    }
    h1, h2, h3, p, span, div, li { color: #2b2b2b !important; font-family: 'Special Elite', monospace !important; background-color: transparent !important; }
    .carimbo { color: #b32424 !important; border: 4px solid #b32424 !important; padding: 10px 20px !important; font-size: 3rem !important; text-transform: uppercase !important; transform: rotate(-3deg); display: inline-block !important; margin-bottom: 2rem !important; opacity: 0.8 !important;}
    .marca-texto { background-color: #e6d97e !important; color: #111 !important; padding: 0 5px !important; }
    .censura { background-color: #1a1a1a !important; color: #1a1a1a !important; transition: color 0.4s !important; padding: 0 5px !important; }
    .censura:hover { color: #f4ecd8 !important; cursor: help; }
    header, footer { visibility: hidden !important; }
    .stButton > button { background-color: #e3d9c6 !important; color: #b32424 !important; border: 2px dashed #b32424 !important; width: 100% !important; font-family: 'Special Elite', monospace !important; }
</style>
""", unsafe_allow_html=True)

    st.markdown('<div style="text-align:center;"><div class="carimbo">Arquivo Confidencial</div></div>', unsafe_allow_html=True)
    st.markdown('<h2 style="border-bottom: 2px solid #b32424;">O Guia do Professor - Cap. 1: O Portão</h2>', unsafe_allow_html=True)
    
    st.markdown(f'''
<p style="font-size:1.3rem; margin-top:2rem;">A maioria das pessoas vive sem saber de um segredo essencial: o peso das coisas não é o mesmo em todos os lugares.</p>
<p style="font-size:1.3rem;">Quem trabalha em Escola sabe disso. E eu, Professor de Educação Física, deveria até saber mais que todo mundo. Eu estava prestes a testemunhar, mais uma vez, as consequências desse fenômeno.</p>
<p style="font-size:1.3rem;">O "Ranca" não é uma simples brincadeira. Não é uma pelada desorganizada. O Ranca é uma força da natureza. <span class="marca-texto">O Ranca não tem MÃE!</span> É Um evento espontâneo com poderes magnéticos, capaz de atrair corpos desavisados. <span class="censura">“Toca essa bola, C@#$%%0!!!”</span></p>
<p style="font-size:1.3rem;">Sabendo disso ou não, lá fui eu. Salas visitadas, alunos abordados, convites feitos. Tudo dentro do planejado. Dialógico.</p>
<p style="text-align: center; margin: 3rem 0; font-weight:bold; font-size: 1.8rem; color: #b32424 !important;">Às onze e meia da manhã, testemunhei o inevitável.</p>
<p style="text-align: center; font-size: 2.2rem; color: #b32424 !important; border: 2px solid #b32424; padding: 10px; transform: rotate(1deg); display:inline-block;">Alguém abriu o portão da quadra.</p>
<p style="font-size:1.3rem; margin-top: 2rem;">Não foi grandioso. Mas aquilo é equivalente ao sinal do recreio em dia que a merenda é cachorro-quente. Mais que depressa, a maioria dos alunos bateu em retirada. Pura força da gravidade local agindo. O Ranca.</p>
<p style="font-size:1.3rem;">No auditório, esperei. Alguns poucos alunos restaram. Provavelmente os que sentiram vergonha de me deixar falando sozinho. Eles ficaram até o fim, ouviram a explicação inteira. Lá fora, no chão quente da quadra, o Ranca rugia.</p>
<p style="font-size:1.3rem;">Mas se alguém abrir o portão da quadra, não adianta.</p>
<p style="font-size:2.5rem; text-align: center; margin-top: 3rem; color: #b32424 !important; font-weight:bold;">O Ranca é inevitável!</p>
''', unsafe_allow_html=True)

    st.button("FECHAR DOSSIÊ E VOLTAR AO RELATÓRIO", on_click=alternar_dimensao)

# ==============================================================================
# 📖 LADO A: O CADERNO DIDÁTICO (A Poesia do Movimento)
# ==============================================================================
else:
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=Lora:ital,wght@0,400;0,600;1,400;1,600&display=swap');
    
    .stApp { background-color: #e8e6df !important; }
    
    .block-container {
        max-width: 1150px !important; padding: 6rem 5rem !important; background-color: #fffdf8 !important;
        box-shadow: 0 25px 70px rgba(0,0,0,0.1) !important; border-left: 1px solid #eae5d9 !important; border-right: 1px solid #eae5d9 !important;
    }
    
    /* REMOÇÃO DE QUALQUER FUNDO EM TÍTULOS E PARÁGRAFOS */
    h1, h2, h3, h4, p, span, div, li { 
        color: #1a1a1a !important; 
        font-family: 'Playfair Display', serif !important; 
        background-color: transparent !important; 
        background: none !important;
    }
    
    p, li { font-family: 'Lora', serif !important; color: #2c2c2c !important; }

    .titulo-capa { font-size: 4rem !important; font-weight: 700 !important; text-align: center !important; line-height: 1.2 !important; margin-bottom: 1rem !important; }
    .subtitulo-capitulo { font-size: 2.5rem !important; color: #8c3a3a !important; border-bottom: 1px solid #eae5d9 !important; padding-bottom: 0.8rem !important; margin-top: 5rem !important; font-style: italic !important;}
    .dropcap::first-letter { float: left !important; font-size: 5.5rem !important; line-height: 0.8 !important; padding-right: 12px !important; color: #8c3a3a !important; font-weight: 700 !important; }
    
    /* BOX DE IMAGEM LIMPO */
    .box-imagem { background-color: #fcfbf7 !important; border: 1px solid #d4cbb8 !important; padding: 40px !important; text-align: center !important; margin: 2.5rem 0 !important; width: 100% !important; display: block !important;}
    .tag-midia { font-family: sans-serif !important; text-transform: uppercase !important; font-size: 0.9rem !important; font-weight: bold !important; color: #888 !important; display: block !important; margin-bottom: 10px !important;}
    .desc-midia { font-style: italic !important; color: #555 !important; font-size: 1.3rem !important; display: block !important; line-height: 1.5 !important;}
    
    .frase-impacto { font-size: 2.8rem !important; font-style: italic !important; color: #8c3a3a !important; text-align: center !important; margin: 4rem 0 !important; line-height: 1.4 !important; background: transparent !important;}
    
    header, footer { visibility: hidden !important; }
    .stButton > button { background-color: #fffdf8 !important; border: 1px solid #d4cbb8 !important; color: #8c3a3a !important; width: 100% !important; padding: 20px !important; text-transform: uppercase !important; letter-spacing: 2px !important; }
</style>
""", unsafe_allow_html=True)

    # --- PÁGINA 1: CAPA ---
    st.markdown('<p style="text-align:center; letter-spacing: 4px; color: #8c3a3a !important; font-weight:bold;">E. E. PROFESSORA AYNA TORRES | PIBID</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="titulo-capa">RELATÓRIO DA AÇÃO EXTENSIONISTA:<br>ENTRE O PLANEJAR, O FAZER E O SONHAR</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size: 2rem; font-style: italic; color: #555 !important;">A Poesia do Movimento</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="box-imagem" style="min-height:500px;"><span class="tag-midia">Fotografia Principal de Capa</span><span class="desc-midia">Insira aqui a imagem de maior impacto do projeto.</span></div>', unsafe_allow_html=True)
    
    st.markdown('<p style="text-align: center; font-size: 1.3rem; margin-top: 2rem;">Minas Gerais, 2024</p>', unsafe_allow_html=True)

    # --- APRESENTAÇÃO ---
    st.markdown('<h2 class="subtitulo-capitulo">Apresentação</h2>', unsafe_allow_html=True)
    st.markdown('<p class="texto dropcap" style="font-size:1.3rem;">Neste caderno, datas e ponteiros do relógio importam menos do que as transformações que ocorreram nos espaços da Escola Estadual Professora Ayna Torres. A Ginástica para Todos (GPT) não foi apenas uma sequência de aulas práticas; foi um desafio, foi mudança, foi conflito e foi divertido demais!</p>', unsafe_allow_html=True)

    # --- CAPÍTULO 1: O PESO DO TEMPO ---
    st.markdown('<h2 class="subtitulo-capitulo">O Peso do Tempo e o Despertar do Corpo</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.markdown('''
<p style="font-size:1.25rem;">O tempo no Ensino Médio em Tempo Integral (EMTI) pode ser um rio longo, denso e exaustivo. O longo intervalo do almoço era vencido por corpos sentados, intermináveis partidas de Truco e prática deliberada de Futsal.</p>
<p style="font-size:1.25rem;">No primeiro dia de projeto, quando o portão se abriu, muitos alunos bateram em retirada para a quadra. Mas com insistência e apoio dos bolsistas do PIBID, a semente da curiosidade foi plantada. O auditório virou um refúgio de leveza.</p>
''', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="box-imagem"><span class="tag-midia">FOTO 1</span><span class="desc-midia">Contraste entre o pátio vazio e os primeiros alunos entrando.</span></div>', unsafe_allow_html=True)

    # --- GALERIA VISUAL I ---
    st.markdown('<div style="margin: 4rem 0; border-top: 1px solid #eee; padding-top: 2rem;"><h3 style="text-align:center; font-style:italic; color:#8c3a3a !important;">Mosaico Visual I: A Descoberta</h3></div>', unsafe_allow_html=True)
    g1, g2 = st.columns(2)
    with g1: st.markdown('<div class="box-imagem" style="min-height:450px;"><span class="tag-midia">GIF / VÍDEO</span><span class="desc-midia">Auditório ganhando vida.</span></div>', unsafe_allow_html=True)
    with g2: st.markdown('<div class="box-imagem" style="min-height:450px;"><span class="tag-midia">FOTO</span><span class="desc-midia">Expressões faciais de curiosidade.</span></div>', unsafe_allow_html=True)

    # --- CAPÍTULO 2: MEDO ---
    st.markdown('<h2 class="subtitulo-capitulo">Vencendo o Medo do Desconhecido e o Preconceito</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.25rem;">Talvez a maior acrobacia realizada neste projeto não tenha sido física. O colchonete revelou que muitos de nós somos prisioneiros dos nossos próprios medos. O projeto foi o martelo que estilhaçou todo reflexo do olhar maldoso lá de fora. Eles aprenderam que a escola é o lugar para se abrir a cabeça e derrubar essas barreiras.</p>', unsafe_allow_html=True)
    st.markdown('<div class="box-imagem" style="min-height:400px;"><span class="tag-midia">VÍDEO DE SUPERAÇÃO</span><span class="desc-midia">O sorriso de alívio ao executar uma "estrelinha" pela primeira vez.</span></div>', unsafe_allow_html=True)

    # --- CAPÍTULO 3: COLETIVO ---
    st.markdown('<h2 class="subtitulo-capitulo">Construindo o Coletivo: Paciência e Fraternidade</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.25rem;">Diferente da frieza das competições tradicionais, a GPT não carrega a balança dos jurados. Sem a pressão de ser o melhor, o que floresceu foi a empatia. As coreografias geométricas provaram que cada corpo é essencial para manter a figura acrobática em pé.</p>', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3: st.markdown('<div class="box-imagem"><span class="tag-midia">FOTO APOIO</span><span class="desc-midia">O toque de cuidado entre os alunos.</span></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="box-imagem"><span class="tag-midia">FOTO RODA</span><span class="desc-midia">Roda de conversa e questionários.</span></div>', unsafe_allow_html=True)

    # --- CONTRACAPA ---
    st.markdown('<hr style="border: 0.5px solid #eae5d9; margin-top: 5rem;">', unsafe_allow_html=True)
    st.markdown('<p class="frase-impacto">"Apresentar a poesia da GPT para a comunidade é a forma definitiva de mostrar que a ginástica é verdadeiramente PARA TODOS."</p>', unsafe_allow_html=True)
    st.markdown('<div class="box-imagem" style="min-height:500px;"><span class="tag-midia">FOTOGRAFIA FINAL</span><span class="desc-midia">Grande foto em grupo celebrando a força do corpo.</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-weight:bold; color:#8c3a3a !important; margin-top: 2rem;">UFSJ | PIBID | MINAS GERAIS, 2024</p>', unsafe_allow_html=True)

    # --- BOTÃO LADO B ---
    st.markdown('<div style="margin-top: 6rem; text-align: center; border-top:1px dashed #ccc; padding-top:4rem;">', unsafe_allow_html=True)
    st.button("⚠️ ACESSAR ANEXO CONFIDENCIAL: O GUIA DO PROFESSOR", on_click=alternar_dimensao)
    st.markdown('</div>', unsafe_allow_html=True)
