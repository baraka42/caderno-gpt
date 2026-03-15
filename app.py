import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Caderno Didático: GPT",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CONTROLE DE NAVEGAÇÃO ---
if 'mundo_invertido' not in st.session_state:
    st.session_state.mundo_invertido = False
if 'ir_para_o_topo' not in st.session_state:
    st.session_state.ir_para_o_topo = False

def alternar_dimensao():
    st.session_state.mundo_invertido = not st.session_state.mundo_invertido
    st.session_state.ir_para_o_topo = True

if st.session_state.ir_para_o_topo:
    components.html("<script>window.parent.document.querySelector('.main').scrollTo({top: 0, behavior: 'smooth'});</script>", height=0)
    st.session_state.ir_para_o_topo = False

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
    h1, h2, h3, p, span, div, li { color: #2b2b2b !important; font-family: 'Special Elite', monospace !important; }
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
<p style="font-size:1.3rem; margin-top:2rem;">A maioria das pessoas vive sem saber de um segredo essencial: <span class="marca-texto">o peso das coisas não é o mesmo em todos os lugares.</span></p>
<p style="font-size:1.3rem;">O "Ranca" não é uma simples brincadeira. O Ranca é uma força da natureza. <span class="marca-texto">O Ranca não tem MÃE!</span> É Um evento espontâneo com poderes magnéticos. <span class="censura">“Toca essa bola, C@#$%%0!!!”</span></p>
<p style="text-align: center; margin: 3rem 0; font-weight:bold; font-size:2rem; color:#b32424 !important;">Alguém abriu o portão da quadra.</p>
<p style="font-size:1.3rem;">Não foi grandioso. Foi só um portão se abrindo. Mas aquilo é equivalente ao sinal do recreio em dia que a merenda é cachorro-quente. Os alunos correram para a quadra em busca de outra dose para saciar a coceira das pernas. O Ranca rugia lá fora no chão quente.</p>
<p style="font-size:2.5rem; text-align: center; margin-top: 3rem; color: #b32424 !important; border: 3px solid #b32424; padding:10px;">O Ranca é inevitável!</p>
''', unsafe_allow_html=True)

    st.button("FECHAR DOSSIÊ E VOLTAR AO RELATÓRIO", on_click=alternar_dimensao)

# ==============================================================================
# LADO A: O CADERNO DIDÁTICO (A Poesia do Movimento)
# ==============================================================================
else:
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=Lora:ital,wght@0,400;0,600;1,400;1,600&display=swap');
    .stApp { background-color: #e8e6df !important; }
    .block-container {
        max-width: 1100px !important; padding: 5rem !important; background-color: #fffdf8 !important;
        box-shadow: 0 25px 70px rgba(0,0,0,0.1) !important; border-left: 1px solid #eae5d9 !important; border-right: 1px solid #eae5d9 !important;
    }
    h1, h2, h3, h4 { color: #1a1a1a !important; font-family: 'Playfair Display', serif !important; }
    p, span, div, li { color: #2c2c2c !important; font-family: 'Lora', serif !important; }
    .titulo-capa { font-size: 4.5rem !important; font-weight: 700 !important; text-align: center !important; line-height: 1.1 !important; margin-bottom: 1rem !important; }
    .subtitulo-capitulo { font-size: 2.5rem !important; color: #8c3a3a !important; border-bottom: 1px solid #eae5d9 !important; padding-bottom: 0.8rem !important; margin-top: 5rem !important; font-style: italic !important;}
    .dropcap::first-letter { float: left !important; font-size: 5.5rem !important; line-height: 0.8 !important; padding-right: 12px !important; color: #8c3a3a !important; font-weight: 700 !important; }
    
    /* CAIXA DE IMAGEM CORRIGIDA (SEM RECUO PARA NÃO VIRAR CÓDIGO) */
    .box-imagem { background-color: #f5f5f5 !important; border: 2px dashed #cccccc !important; border-radius: 4px !important; padding: 40px 20px !important; text-align: center !important; margin: 2.5rem 0 !important; width: 100% !important; min-height: 350px !important; display: block !important;}
    .box-imagem-full { min-height: 550px !important; background-color: #fcfbf7 !important; border: 1px solid #d4cbb8 !important;}
    .tag-midia { font-family: sans-serif !important; text-transform: uppercase !important; font-size: 0.9rem !important; font-weight: bold !important; color: #888 !important; display: block !important; margin-bottom: 15px !important;}
    .desc-midia { font-style: italic !important; color: #555 !important; font-size: 1.3rem !important; display: block !important; line-height: 1.5 !important;}
    
    .secao-galeria { background-color: #faf9f6 !important; padding: 4rem 2rem !important; border: 1px solid #eee !important; margin: 4rem 0 !important; text-align: center !important;}
    .frase-impacto { font-family: 'Playfair Display', serif !important; font-size: 2.8rem !important; font-style: italic !important; color: #8c3a3a !important; text-align: center !important; margin: 4rem 0 !important; padding: 0 10% !important;}
    
    header, footer { visibility: hidden !important; }
    .stButton > button { background-color: #fffdf8 !important; border: 1px solid #d4cbb8 !important; color: #8c3a3a !important; width: 100% !important; padding: 20px !important; text-transform: uppercase !important; letter-spacing: 2px !important; }
</style>
""", unsafe_allow_html=True)

    # --- PÁGINA 1: CAPA ---
    st.markdown('<p style="text-align:center; letter-spacing: 4px; color: #8c3a3a !important; font-weight:bold;">E. E. PROFESSORA AYNA TORRES | PIBID</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="titulo-capa">RELATÓRIO DA AÇÃO EXTENSIONISTA:<br>ENTRE O PLANEJAR, O FAZER E O SONHAR</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size: 2rem; font-style: italic; color: #555 !important;">A Poesia do Movimento</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="box-imagem box-imagem-full"><span class="tag-midia">Fotografia de Capa</span><span class="desc-midia">Insira aqui a imagem de maior impacto do seu Caderno Didático.</span></div>', unsafe_allow_html=True)
    
    st.markdown('<p style="text-align: center; font-size: 1.3rem; margin-top: 2rem;">Minas Gerais, 2024</p>', unsafe_allow_html=True)

    # --- PÁGINA 2: INTRODUÇÃO ---
    st.markdown('<h2 class="subtitulo-capitulo">Apresentação</h2>', unsafe_allow_html=True)
    st.markdown('<p class="texto dropcap" style="font-size:1.3rem; line-height:1.9;">Neste caderno, datas e ponteiros do relógio importam menos do que as transformações que ocorreram nos espaços da Escola Estadual Professora Ayna Torres. A Ginástica para Todos (GPT) não foi apenas uma sequência de aulas práticas; foi um desafio, foi mudança, foi conflito e foi divertido demais!</p>', unsafe_allow_html=True)

    # --- CAPÍTULO 1: O PESO DO TEMPO ---
    st.markdown('<h2 class="subtitulo-capitulo">O Peso do Tempo e o Despertar do Corpo</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.markdown('''
<p class="texto" style="font-size:1.25rem;">O tempo no Ensino Médio em Tempo Integral (EMTI) pode ser um rio longo, denso e exaustivo. O longo intervalo do almoço era vencido por corpos sentados, intermináveis partidas de Truco e prática deliberada de Futsal.</p>
<p class="texto" style="font-size:1.25rem;">No primeiro dia de projeto, quando o portão se abriu, muitos alunos bateram em retirada para a quadra. Mas com insistência e apoio dos bolsistas do PIBID, a semente da curiosidade foi plantada. O auditório virou um refúgio de leveza onde o tempo passou a voar.</p>
''', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="box-imagem"><span class="tag-midia">FOTO 1</span><span class="desc-midia">Contraste entre o pátio vazio e os primeiros alunos entrando.</span></div>', unsafe_allow_html=True)

    # --- PÁGINA 3: GALERIA EXCLUSIVA (SEM TEXTO) ---
    st.markdown('<div class="secao-galeria"><h3 style="margin-bottom:2rem; font-style:italic; color:#8c3a3a !important;">Mosaico Visual I: A Descoberta do Movimento</h3>', unsafe_allow_html=True)
    g1, g2 = st.columns(2)
    with g1: st.markdown('<div class="box-imagem" style="min-height:450px;"><span class="tag-midia">GIF / VÍDEO LOOP</span><span class="desc-midia">O auditório ganhando vida.</span></div>', unsafe_allow_html=True)
    with g2: st.markdown('<div class="box-imagem" style="min-height:450px;"><span class="tag-midia">FOTO DETALHE</span><span class="desc-midia">Close nos colchonetes ou mãos se preparando.</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CAPÍTULO 2: VENCENDO O MEDO ---
    st.markdown('<h2 class="subtitulo-capitulo">Vencendo o Medo do Desconhecido e o Preconceito</h2>', unsafe_allow_html=True)
    st.markdown('<p class="texto" style="font-size:1.25rem;">Talvez a maior acrobacia realizada neste projeto não tenha sido física. O colchonete revelou que muitos de nós somos prisioneiros dos nossos próprios medos. O projeto foi o martelo que estilhaçou todo reflexo do olhar maldoso lá de fora. Eles aprenderam que a escola é exatamente o lugar para se abrir a cabeça e derrubar essas barreiras.</p>', unsafe_allow_html=True)
    st.markdown('<div class="box-imagem" style="min-height:400px;"><span class="tag-midia">VÍDEO DE SUPERAÇÃO</span><span class="desc-midia">O sorriso de alívio ao executar uma "estrelinha" pela primeira vez.</span></div>', unsafe_allow_html=True)

    # --- CAPÍTULO 3: COLETIVO ---
    st.markdown('<h2 class="subtitulo-capitulo">Construindo o Coletivo: Paciência e Fraternidade</h2>', unsafe_allow_html=True)
    st.markdown('<p class="texto" style="font-size:1.25rem;">Diferente da frieza das competições tradicionais, a GPT não carrega a balança dos jurados. Sem a pressão de ser o melhor, o que floresceu foi a empatia. As coreografias geométricas provaram que cada corpo, com seu próprio ritmo, é essencial para manter a figura acrobática em pé.</p>', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3: st.markdown('<div class="box-imagem"><span class="tag-midia">FOTO APOIO</span><span class="desc-midia">O toque de cuidado entre os alunos.</span></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="box-imagem"><span class="tag-midia">FOTO RODA</span><span class="desc-midia">Roda de conversa e preenchimento dos questionários.</span></div>', unsafe_allow_html=True)

    # --- CAPÍTULO 4: O FUTURO ---
    st.markdown('<h2 class="subtitulo-capitulo">A Semente que rola: O Futuro da GPT</h2>', unsafe_allow_html=True)
    st.markdown('<p class="texto" style="font-size:1.25rem;">O fim do projeto é um começo. O novo sonho pulsa nas ruas: levar as coreografias para além dos muros da escola. Mostrar que a ginástica é verdadeiramente PARA TODOS.</p>', unsafe_allow_html=True)

    # --- PÁGINA FINAL: CONTRACAPA ---
    st.markdown('<div class="contracapa-container">', unsafe_allow_html=True)
    st.markdown('<p class="frase-impacto">"Apresentar a poesia da GPT para a comunidade é a forma definitiva de mostrar que a ginástica é verdadeiramente PARA TODOS."</p>', unsafe_allow_html=True)
    st.markdown('<div class="box-imagem box-imagem-full" style="min-height:450px;"><span class="tag-midia">FOTO FINAL DE GRUPO</span><span class="desc-midia">Equipe, alunos e o brilho nos olhos.</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="margin-top:2rem; font-weight:bold; color:#8c3a3a !important;">UFSJ | PIBID | MINAS GERAIS</p></div>', unsafe_allow_html=True)

    # --- BOTÃO LADO B ---
    st.markdown('<div style="margin-top: 5rem; text-align: center; border-top:1px dashed #ccc; padding-top:3rem;">', unsafe_allow_html=True)
    st.button("⚠️ ACESSAR ANEXO CONFIDENCIAL: O GUIA DO PROFESSOR", on_click=alternar_dimensao)
    st.markdown('</div>', unsafe_allow_html=True)
