import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Caderno Didático: GPT",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CONTROLE DE MODO NOTURNO ---
col_vazia, col_toggle = st.columns([8, 2])
with col_toggle:
    modo_noturno = st.toggle("Modo Noturno")

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
# LADO B: O GUIA DO PROFESSOR (Dossiê Confidencial)
# ==============================================================================
if st.session_state.mundo_invertido:
    st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    .stApp {{ background-color: {bg_app} !important; }}
    .block-container {{
        max-width: 900px !important; padding: 4rem 5rem !important;
        background-color: {bg_dossie} !important;
        border: 3px solid {color_border} !important; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4) !important;
    }}
    h1, h2, h3, p, span, div, li {{ color: {color_dossie_text} !important; font-family: 'Special Elite', monospace !important; background: transparent !important; }}
    .dossie-texto {{ font-size: 1.25rem !important; line-height: 1.8 !important; text-align: justify !important; margin-bottom: 1.5rem !important; }}
    .carimbo {{ color: #b32424 !important; border: 4px solid #b32424 !important; padding: 10px 20px !important; font-size: 3rem !important; text-transform: uppercase !important; transform: rotate(-3deg); display: inline-block !important; margin-bottom: 2rem !important; opacity: 0.8 !important;}}
    .marca-texto {{ background-color: #e6d97e !important; color: #111 !important; padding: 0 5px !important; }}
    .censura {{ background-color: #1a1a1a !important; color: #1a1a1a !important; padding: 0 5px !important; border-radius: 2px; transition: 0.3s; }}
    .censura:hover {{ color: #fff !important; cursor: help; }}
    .btn-audio-b {{ background: transparent; border: 1px solid #b32424; color: #b32424; padding: 8px 20px; border-radius: 20px; cursor: pointer; font-family: 'Special Elite', monospace; font-size: 1rem; transition: 0.3s; display: block; margin: 0 auto 3rem auto; }}
    .btn-audio-b:hover {{ background: #b32424; color: {bg_dossie}; }}
    header, footer {{ visibility: hidden !important; }}
    .stButton > button {{ background-color: transparent !important; color: #b32424 !important; border: 2px dashed #b32424 !important; width: 100% !important; font-family: 'Special Elite', monospace !important; font-size: 1.2rem !important; padding: 1rem !important; transition: 0.3s;}}
    .stButton > button:hover {{ background-color: #b32424 !important; color: {bg_dossie} !important; }}
    @media (max-width: 768px) {{ .block-container {{ padding: 2rem 1.5rem !important; }} .carimbo {{ font-size: 2rem !important; }} .dossie-texto {{ font-size: 1.1rem !important; }} }}
</style>
""", unsafe_allow_html=True)

    st.markdown('<div style="text-align:center;"><div class="carimbo">Arquivo Confidencial</div></div>', unsafe_allow_html=True)
    
    st.markdown("""
<audio id="trilhaB" loop>
  <source src="NOME_AUDIO_LADO_B.mp3" type="audio/mpeg">
</audio>
<button class="btn-audio-b" onclick="var a=document.getElementById('trilhaB'); if(a.paused){a.play(); this.innerText='⏸ PAUSAR GRAVAÇÃO';} else {a.pause(); this.innerText='▶ OUVIR GRAVAÇÃO';}">▶ OUVIR GRAVAÇÃO</button>
""", unsafe_allow_html=True)

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

    st.button("FECHAR DOSSIÊ E VOLTAR AO RELATÓRIO", on_click=alternar_dimensao)

# ==============================================================================
# LADO A: O CADERNO DIDÁTICO (A Poesia do Movimento)
# ==============================================================================
else:
    st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=Lora:ital,wght@0,400;0,600;1,400;1,600&display=swap');
    .stApp {{ background-color: {bg_app} !important; transition: background-color 0.3s; }}
    .block-container {{ max-width: 1150px !important; padding: 6rem 5rem !important; background-color: {bg_paper} !important; box-shadow: 0 25px 70px rgba(0,0,0,0.08) !important; border: 1px solid {color_border} !important; transition: background-color 0.3s; }}
    h1, h2, h3, h4 {{ color: {color_title} !important; font-family: 'Playfair Display', serif !important; background: transparent !important; }}
    p, span, div, li {{ color: {color_text} !important; font-family: 'Lora', serif !important; background: transparent !important; }}
    .quebra-pagina {{ margin: 6rem 0; border: none; border-top: 1px solid {color_border}; opacity: 0.7; }}
    .ornamento {{ text-align: center; color: {color_border}; font-size: 2.5rem; margin: 2rem 0; line-height: 0; }}
    .titulo-capa {{ font-size: 3.5rem !important; font-weight: 700 !important; text-align: center !important; line-height: 1.2 !important; margin-bottom: 1rem !important; }}
    .subtitulo-capitulo {{ font-size: 2.2rem !important; color: {color_accent} !important; border-bottom: 1px solid {color_border} !important; padding-bottom: 0.8rem !important; margin-top: 1rem !important; margin-bottom: 2.5rem !important; font-style: italic !important;}}
    .dropcap::first-letter {{ float: left !important; font-size: 5rem !important; line-height: 0.8 !important; padding-top: 8px !important; padding-right: 12px !important; color: {color_accent} !important; font-weight: 700 !important; }}
    .texto {{ text-align: justify !important; font-size: 1.2rem !important; line-height: 1.8 !important; margin-bottom: 1.5rem !important; }}
    .box-imagem-paisagem {{ aspect-ratio: 16 / 9; background-color: {bg_img_box} !important; border: 1px dashed #bbb !important; border-radius: 4px !important; display: flex !important; flex-direction: column !important; justify-content: center !important; align-items: center !important; width: 100% !important; margin: 1rem 0 0.5rem 0 !important; padding: 20px !important; }}
    .box-imagem-retrato {{ aspect-ratio: 9 / 16; background-color: {bg_img_box} !important; border: 1px dashed #bbb !important; border-radius: 4px !important; display: flex !important; flex-direction: column !important; justify-content: center !important; align-items: center !important; width: 100% !important; margin: 1rem 0 0.5rem 0 !important; padding: 20px !important; }}
    .tag-midia {{ font-family: sans-serif !important; text-transform: uppercase !important; font-size: 0.9rem !important; font-weight: bold !important; color: #999 !important; margin-bottom: 10px !important; text-align: center !important;}}
    .desc-midia {{ font-style: italic !important; color: {color_text} !important; font-size: 1.1rem !important; text-align: center !important; max-width: 80% !important;}}
    .legenda-img {{ font-size: 0.95rem !important; color: #777 !important; text-align: center !important; font-style: italic !important; margin-bottom: 2rem !important; font-family: 'Lora', serif !important; }}
    .ficha-catalografica-container {{ font-family: 'Times New Roman', Times, serif !important; color: {color_text} !important; max-width: 650px; margin: 4rem auto; font-size: 1rem; }}
    .ficha-box {{ border: 1px solid {color_text} !important; padding: 1.5rem; display: flex; margin-top: 1.5rem; margin-bottom: 1.5rem; }}
    .ficha-texto {{ font-family: 'Times New Roman', Times, serif !important; color: {color_text} !important; }}
    .epigrafe-container {{ text-align: center; margin-bottom: 2rem; }}
    .epigrafe-texto {{ font-family: 'Playfair Display', serif !important; font-size: 1.1rem !important; font-style: italic !important; color: {color_accent} !important; line-height: 1.4 !important; margin-bottom: 0.5rem !important;}}
    .epigrafe-autor {{ font-family: 'Lora', serif !important; font-size: 0.85rem !important; color: #777 !important; text-transform: uppercase; letter-spacing: 1px;}}
    .btn-audio-a {{ background: transparent; border: 1px solid {color_accent}; color: {color_accent}; padding: 8px 20px; border-radius: 20px; cursor: pointer; font-family: 'Lora', serif; font-size: 1rem; transition: 0.3s; display: block; margin: 0 auto 3rem auto; }}
    .btn-audio-a:hover {{ background: {color_accent}; color: {bg_paper}; }}
    header, footer {{ visibility: hidden !important; }}
    .stButton > button {{ background-color: transparent !important; border: 1px solid {color_border} !important; color: {color_accent} !important; width: 100% !important; padding: 20px !important; text-transform: uppercase !important; letter-spacing: 2px !important; transition: 0.3s;}}
    .stButton > button:hover {{ background-color: {color_accent} !important; color: {bg_paper} !important; }}
    @media (max-width: 768px) {{ .block-container {{ padding: 2rem 1rem !important; border: 1px solid {color_border} !important; }} .titulo-capa {{ font-size: 2.2rem !important; }} .subtitulo-capitulo {{ font-size: 1.8rem !important; }} .texto {{ font-size: 1.1rem !important; }} .dropcap::first-letter {{ font-size: 4rem !important; }} div[data-testid="column"] {{ width: 100% !important; flex: unset !important; }} .ficha-box {{ flex-direction: column; }} }}
</style>
""", unsafe_allow_html=True)

    st.markdown("""
<audio id="trilhaA" loop>
  <source src="NOME_AUDIO_LADO_A.mp3" type="audio/mpeg">
</audio>
<button class="btn-audio-a" onclick="var a=document.getElementById('trilhaA'); if(a.paused){a.play(); this.innerText='⏸ Pausar Trilha Poética';} else {a.pause(); this.innerText='▶ Ouvir Trilha Poética';}">▶ Ouvir Trilha Poética</button>
""", unsafe_allow_html=True)

    st.markdown(f'<p style="text-align:center; letter-spacing: 4px; color: {color_accent} !important; font-weight:bold; margin-bottom: 2rem;">UFVJM | PIBID</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="titulo-capa">RELATÓRIO DA AÇÃO EXTENSIONISTA:<br>ENTRE O PLANEJAR, O FAZER E O SONHAR</h1>', unsafe_allow_html=True)
    
    st.markdown('''
<div class="box-imagem-paisagem">
<span class="tag-midia">FOTOGRAFIA / CAPA (16:9 HORIZONTAL)</span>
<span class="desc-midia">Insira aqui a fotografia de maior impacto do projeto.</span>
</div>
<div class="legenda-img">Fotografia de Capa: Título ou descrição da imagem.</div>
''', unsafe_allow_html=True)

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
<span class="ficha-texto">A Poesia do Movimento / organizadores Nome Sobrenome, Nome Sobrenome, Nome Sobrenome; fotografia Nome Sobrenome, Nome Sobrenome; diagramação Nome Sobrenome. - Diamantina: UFVJM, 2024.</span><br><br>
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

    st.markdown('''
<div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
<div class="box-imagem-paisagem">
<span class="tag-midia">FOTOGRAFIA (16:9 HORIZONTAL)</span>
<span class="desc-midia">Fotografia de respiro visual antes da Apresentação.</span>
</div>
<div class="legenda-img" style="margin-bottom: 3rem;">Figura 1: Breve descrição da cena capturada.</div>
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

    st.markdown('<h2 class="subtitulo-capitulo">O Peso do Tempo e o Despertar do Corpo</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.markdown('''
<p class="texto">O tempo no Ensino Médio em Tempo Integral (EMTI) pode ser um rio longo, denso e exaustivo. Permanecer quase dez horas no ambiente escolar exige muito dos estudantes, um esforço que, nas palavras deles, "acaba com qualquer um" e exige muita coluna.</p>
<p class="texto">O longo intervalo do almoço era vencido por corpos sentados, intermináveis partidas de Truco e prática deliberada de Futsal. Não que ficar sentado após o almoço seja algo negativo, na verdade é o fisiologicamente recomendado. Mas intervalo de almoço é verdadeiramente longo e visto como tedioso pelos alunos.</p>
<p class="texto">O convite para o movimento encontrou, de início, a resistência natural de quem teme o novo. No primeiro dia de projeto, quando o portão se abriu, muitos alunos bateram em retirada para a quadra, buscando o conforto das práticas habituais. Mas com insistência, apoio dos bolsistas do PIBID e alguns vídeos legais, a semente da curiosidade foi plantada. Aos poucos, a rotina foi quebrada, e o auditório virou um refúgio de leveza onde o tempo, antes arrastado, passou a voar.</p>
''', unsafe_allow_html=True)
    with col2:
        st.markdown('''
<div class="box-imagem-retrato">
<span class="tag-midia">FOTO (9:16 VERTICAL)</span>
<span class="desc-midia">O contraste entre o pátio vazio e os primeiros alunos entrando no auditório, descobrindo os colchonetes.</span>
</div>
<div class="legenda-img">Figura 2: Alunos entrando no auditório.</div>
''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown(f'<h3 style="text-align: center; color: {color_accent} !important; font-style: italic; margin-bottom: 2rem;">Galeria: A Descoberta</h3>', unsafe_allow_html=True)
    st.markdown('''
<div class="box-imagem-paisagem">
<span class="tag-midia">VÍDEO OU GIF EM LOOP (16:9 HORIZONTAL)</span>
<span class="desc-midia">Espaço dedicado a um registro do ambiente se transformando.</span>
</div>
<div class="legenda-img">Registro 1: Auditório ganhando vida com as primeiras movimentações.</div>
''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown('<h2 class="subtitulo-capitulo">Vencendo o Medo do Desconhecido e o Preconceito</h2>', unsafe_allow_html=True)
    st.markdown('''
<p class="texto">Talvez a maior acrobacia realizada neste projeto não tenha sido física. O colchonete revelou que muitos de nós somos prisioneiros dos nossos próprios medos. Os alunos descobriram que o bloqueio mental é o verdadeiro causador de lesões: quando a gente evita o movimento por medo de se machucar, acaba se machucando.</p>
<p class="texto">Havia preconceito a ser quebrados. O julgamento da sociedade pesava, rotulando quem praticava a ginástica com termos pejorativos. As meninas e os meninos enfrentavam o medo da sexualização e do olhar malicioso diante do básico: posições de quatro apoios e espacates, consideradas equivocadamente “vulgares”.</p>
<p class="texto">O projeto foi o martelo que estilhaçou todo reflexo do olhar maldoso lá de fora. O ambiente seguro mostrou que a malícia habita a mente de quem assiste, e não a pureza do movimento. Eles aprenderam que a escola é exatamente o lugar para se abrir a cabeça e derrubar essas barreiras.</p>
''', unsafe_allow_html=True)
    
    st.markdown('''
<div class="box-imagem-paisagem">
<span class="tag-midia">VÍDEO/FOTO (16:9 HORIZONTAL)</span>
<span class="desc-midia">Alunos superando o medo inicial; o sorriso de alívio ao executar uma "estrelinha" ou um salto pela primeira vez.</span>
</div>
<div class="legenda-img">Figura 3: O sorriso após superar o medo da primeira acrobacia.</div>
''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown('<h2 class="subtitulo-capitulo">Construindo o Coletivo: Paciência e Fraternidade</h2>', unsafe_allow_html=True)
    st.markdown('''
<p class="texto">Diferente da frieza das competições tradicionais, a GPT não carrega a balança dos jurados, as notas ou a rivalidade que cria inimizades. Sem a pressão de ser o melhor, o que floresceu foi a empatia.</p>
<p class="texto">O corpo aprendeu novas rimas: pontes, velas, rolamentos à frente, saltos grupados, afastados e a execução precisa da estrelinha. Mas a alma aprendeu a virtude da paciência. A orientação calma ensinou os alunos a terem cautela com a dificuldade do outro. Rapidamente, eles mesmos começaram a se ajudar e a compreender que ninguém é igual a ninguém.</p>
<p class="texto">As coreografias geométricas não foram apenas demonstrações físicas, mas a prova de que cada corpo, com seu próprio ritmo, é essencial para manter a figura acrobática em pé. A ginástica uniu diferenças em um só movimento, respeitando o espaço e o limite de cada um.</p>
''', unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="large")
    with col3:
        st.markdown('''
<div class="box-imagem-retrato">
<span class="tag-midia">FOTO (9:16 VERTICAL)</span>
<span class="desc-midia">O toque de cuidado; alunos auxiliando uns aos outros.</span>
</div>
<div class="legenda-img">Figura 4: Alunos em apoio mútuo.</div>
''', unsafe_allow_html=True)
    with col4:
        st.markdown('''
<div class="box-imagem-retrato">
<span class="tag-midia">FOTO (9:16 VERTICAL)</span>
<span class="desc-midia">A roda de conversa e conexão.</span>
</div>
<div class="legenda-img">Figura 5: Preenchimento dos TCLEs em roda.</div>
''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown(f'<h3 style="text-align: center; color: {color_accent} !important; font-style: italic; margin-bottom: 2rem;">Galeria: O Movimento Coletivo</h3>', unsafe_allow_html=True)
    
    g_col1, g_col2 = st.columns(2, gap="large")
    with g_col1:
        st.markdown('''
<div class="box-imagem-retrato">
<span class="tag-midia">FOTO (9:16 VERTICAL)</span>
<span class="desc-midia">Coreografia geométrica.</span>
</div>
<div class="legenda-img">Figura 6: Formação geométrica em grupo.</div>
''', unsafe_allow_html=True)
    with g_col2:
        st.markdown('''
<div class="box-imagem-retrato">
<span class="tag-midia">FOTO (9:16 VERTICAL)</span>
<span class="desc-midia">O coletivo em ação.</span>
</div>
<div class="legenda-img">Figura 7: Sincronia e movimento coletivo.</div>
''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    st.markdown('<h2 class="subtitulo-capitulo">A Semente que rola: O Futuro da GPT no Coletivo</h2>', unsafe_allow_html=True)
    st.markdown('''
<p class="texto">O fim do projeto é, na verdade, um começo. Transformados pela flexibilidade que ganharam no corpo e na mente, os alunos sonham mais alto.</p>
<p class="texto">Há um desejo de plantar essa semente, levando a GPT para as crianças do 6º ano do ensino fundamental. Eles sabem que corpos mais jovens absorvem o movimento mais rápido e que mentes mais novas podem crescer blindadas contra os preconceitos que eles próprios tiveram que desconstruir.</p>
<p class="texto">E o auditório da escola já ficou pequeno. O novo sonho pulsa nas ruas da cidade: há o desejo de levar as coreografias para além dos muros da escola, nas aglomerações da cidade aos finais de semana. Apresentar a poesia da GPT para a comunidade é a forma definitiva de mostrar que a ginástica é verdadeiramente PARA TODOS.</p>
''', unsafe_allow_html=True)

    st.markdown('''
<div class="box-imagem-paisagem">
<span class="tag-midia">FOTO FINAL (16:9 HORIZONTAL)</span>
<span class="desc-midia">A grande foto em grupo do último encontro, com a equipe da universidade e o brilho nos olhos.</span>
</div>
<div class="legenda-img">Figura 8: Encerramento do projeto. Ginástica para Todos!</div>
''', unsafe_allow_html=True)

    st.markdown(f'<div style="margin-top: 6rem; text-align: center; border-top: 1px dashed {color_border}; padding-top:4rem;">', unsafe_allow_html=True)
    st.button("ACESSAR ANEXO CONFIDENCIAL", on_click=alternar_dimensao)
    st.markdown('</div>', unsafe_allow_html=True)
