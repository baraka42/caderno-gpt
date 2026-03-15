import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Caderno Didático: A Poesia do Movimento",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- GERENCIADOR DE ESTADO E ROLAGEM ---
if 'mundo_invertido' not in st.session_state:
    st.session_state.mundo_invertido = False
if 'scroll_top' not in st.session_state:
    st.session_state.scroll_top = False

def alternar_fita():
    st.session_state.mundo_invertido = not st.session_state.mundo_invertido
    st.session_state.scroll_top = True

if st.session_state.scroll_top:
    components.html(
        "<script>window.parent.document.querySelector('.main').scrollTo({top: 0, behavior: 'smooth'});</script>",
        height=0
    )
    st.session_state.scroll_top = False

# ==============================================================================
# LADO B: O GUIA DO PROFESSOR (Dossiê Confidencial)
# ==============================================================================
if st.session_state.mundo_invertido:
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
            
            .stApp { background-color: #3b3a36 !important; }
            
            .block-container {
                max-width: 900px !important; padding: 4rem 5rem !important;
                background-color: #f4ecd8 !important;
                background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100' height='100' filter='url(%23noise)' opacity='0.05'/%3E%3C/svg%3E") !important;
                border: 1px solid #d1c7b7 !important; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4) !important;
                border-radius: 2px !important; margin-top: 2rem !important; margin-bottom: 2rem !important;
            }

            header {visibility: hidden !important;} footer {visibility: hidden !important;}
            
            h1, h2, h3, h4, h5, h6 { color: #1a1a1a !important; font-family: 'Special Elite', monospace !important; }
            p, span, div, li { color: #2b2b2b !important; }
            
            .dossie-texto { font-family: 'Special Elite', monospace !important; font-size: 1.25rem !important; line-height: 1.8 !important; text-align: left !important; margin-bottom: 1.5rem !important;}
            
            .carimbo-secreto {
                font-family: 'Special Elite', monospace !important; color: #b32424 !important; 
                border: 4px solid #b32424 !important; border-radius: 6px !important; padding: 10px 20px !important;
                display: inline-block !important; font-weight: bold !important; font-size: 3.5rem !important;
                text-transform: uppercase !important; transform: rotate(-3deg) !important; opacity: 0.8 !important;
                margin-bottom: 3rem !important; letter-spacing: 2px !important;
            }
            
            .dossie-capitulo { font-size: 2rem !important; font-weight: bold !important; border-bottom: 2px solid #b32424 !important; padding-bottom: 10px !important; display: inline-block !important; margin-bottom: 2rem !important;}
            
            .marca-texto { background-color: #e6d97e !important; color: #111 !important; padding: 2px 4px !important; }
            .censura { background-color: #1a1a1a !important; color: #1a1a1a !important; padding: 0 8px !important; transition: color 0.3s ease !important; border-radius: 2px !important;}
            .censura:hover { color: #f4ecd8 !important; }
            
            .caneta-vermelha { color: #b32424 !important; font-size: 1.8rem !important; transform: rotate(1deg) !important; display: inline-block !important; font-weight: bold !important;}

            .stButton { text-align: center !important; margin-top: 4rem !important; }
            .stButton > button { background-color: #e3d9c6 !important; color: #2b2b2b !important; border: 2px dashed #b32424 !important; font-family: 'Special Elite', monospace !important; font-size: 1.2rem !important; width: 100% !important; padding: 1rem !important; transition: all 0.3s !important;}
            .stButton > button:hover { background-color: #b32424 !important; color: #f4ecd8 !important; border: 2px solid #b32424 !important; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""<audio autoplay loop><source src="https://actions.google.com/sounds/v1/alarms/beeping_incidental.ogg" type="audio/ogg"></audio>""", unsafe_allow_html=True)

    st.markdown('<div style="text-align: center;"><div class="carimbo-secreto">Arquivo Confidencial</div></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="dossie-capitulo">Capítulo 1: O Portão</h2>', unsafe_allow_html=True)
    
    st.markdown('''
    <p class="dossie-texto">A maioria das pessoas vive sem saber de um segredo essencial: <span class="marca-texto">o peso das coisas não é o mesmo em todos os lugares.</span></p>
    
    <p class="dossie-texto">Quem trabalha em Escola sabe disso. E eu, Professor de Educação Física, deveria até saber mais que todo mundo. Eu estava prestes a testemunhar, mais uma vez, as consequências desse fenômeno.</p>
    
    <p class="dossie-texto">Mas antes de contar o que aconteceu, preciso explicar uma coisa.</p>
    
    <p class="dossie-texto">O "Ranca" não é uma simples brincadeira. Não é uma pelada desorganizada. O Ranca é uma força da natureza. <span class="marca-texto">O Ranca não tem MÃE!</span> É Um evento espontâneo com poderes magnéticos, capaz de atrair corpos desavisados e os envolver num ritual de suor, gritos e dedões do pé dilacerados. <span class="censura">“Toca essa bola, C@#$%%0!!!”</span></p>
    
    <p class="dossie-texto">Sabendo disso ou não, lá fui eu.</p>
    
    <p class="dossie-texto">Era o primeiro dia de tentativa de apresentar o projeto de Ginástica Para Todos para os alunos do Integral. Fui de sala em sala no horário do almoço, quando os alunos ainda não tinham terminado de comer, além dos que encontrava pelos corredores. O plano era simples: convidar todo mundo para ir até o auditório, fazer uma demonstração, explicar o que é a Ginástica Para Todos e tentar conquistar aquele povo para a nova prática. Porque nada conquista mais um adolescente do ensino integRal do que interromper a única pausa que ele tem no dia para falar sobre atividade física.</p>
    
    <p class="dossie-texto">Fui. Salas visitadas, alunos abordados, convites feitos. Tudo dentro do planejado. <em>Dialógico.</em></p>
    
    <p class="dossie-texto" style="text-align: center; font-size: 1.5rem; margin: 3rem 0;">Às onze e meia da manhã do dia dez de março, testemunhei o inevitável.</p>
    
    <p class="dossie-texto" style="text-align: center;"><span class="caneta-vermelha" style="font-size: 2.5rem;">Alguém abriu o portão da quadra.</span></p>
    
    <p class="dossie-texto">Não foi um evento grandioso. Não teve anúncio, não teve alarde. Foi só um portão se abrindo. Mas, para quem tem intimidade com escola, sabe que aquilo é equivalente ao sinal do recreio em dia que a merenda é cachorro-quente. Mais que depressa, a maioria dos alunos bateu em retirada. Não foi desinteresse, não foi maldade. Foi pura e simplesmente a força da gravidade local agindo. Eles correram para a quadra em busca de outra dose para saciar a coceira das pernas. O Ranca.</p>
    
    <p class="dossie-texto">Lá no auditório, esperei. E esperei. E continuei esperando.</p>
    
    <p class="dossie-texto">No final, alguns poucos alunos restaram. Não eram necessariamente os mais interessados em ginástica. Eram, muito provavelmente, os que sentiram vergonha de me deixar falando sozinho. Eles ficaram até o fim, ouviram a explicação inteira, nunca tinha testemunhado tamanha delicadeza, alguns até acenaram com a cabeça em momentos estratégicos.</p>
    
    <p class="dossie-texto">Lá fora, no chão quente da quadra, o Ranca rugia.</p>
    
    <p class="dossie-texto">E eu entendi, naquele dia, que o universo tem suas próprias leis. Você pode planejar, convidar, explicar, demonstrar. Pode ir de sala em sala no horário do almoço, abordar aluno por aluno nos corredores. Pode ser o sujeito mais otimista e sonhador da face da Terra.</p>
    
    <p class="dossie-texto">Mas se alguém abrir o portão da quadra, não adianta.</p>
    
    <p class="dossie-texto" style="text-align: center; margin-top: 3rem;"><span class="caneta-vermelha" style="font-size: 2.8rem; border: 3px solid #b32424 !important; padding: 15px !important; display: inline-block !important; transform: rotate(-2deg) !important;">O Ranca é inevitável!</span></p>
    ''', unsafe_allow_html=True)

    st.button("FECHAR DOSSIÊ E RETORNAR AO CADERNO DIDÁTICO", on_click=alternar_fita)

# ==============================================================================
# LADO A: O CADERNO DIDÁTICO (A Poesia do Movimento)
# ==============================================================================
else:
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=Lora:ital,wght@0,400;0,600;1,400;1,600&display=swap');

            .stApp { background-color: #e8e6df !important; }
            .block-container {
                max-width: 1150px !important; padding: 5rem !important; background-color: #fffdf8 !important;
                box-shadow: 0 25px 70px rgba(0,0,0,0.1) !important; border-radius: 4px !important; 
                border-left: 1px solid #eae5d9 !important; border-right: 1px solid #eae5d9 !important; margin-top: 2rem !important; margin-bottom: 2rem !important;
            }
            header {visibility: hidden !important;} footer {visibility: hidden !important;}

            /* Trava de Cores absolutas */
            h1, h2, h3, h4, h5, h6 { color: #1a1a1a !important; font-family: 'Playfair Display', serif !important; }
            p, span, div, li, a { color: #2c2c2c !important; font-family: 'Lora', serif !important; }

            /* Estrutura de Páginas */
            .quebra-pagina { border-top: 2px dashed #d4cbb8 !important; margin: 5rem 0 !important; opacity: 0.5 !important;}

            /* --- CAPA E CONTRACAPA --- */
            .capa-container { display: block; text-align: center !important; margin-bottom: 4rem !important;}
            .instituicao-capa { font-family: 'Playfair Display', serif !important; font-size: 1.2rem !important; letter-spacing: 4px !important; text-transform: uppercase !important; color: #8c3a3a !important; margin-bottom: 2rem !important;}
            .titulo-capa { font-size: 4.5rem !important; font-weight: 700 !important; margin: 1rem 0 !important; line-height: 1.2 !important;}
            .subtitulo-capa { font-size: 2rem !important; font-style: italic !important; color: #555555 !important; margin-bottom: 3rem !important;}
            
            .contracapa-container { display: block; text-align: center !important; margin-top: 4rem !important; padding: 4rem 2rem !important; background-color: #faf8f2 !important; border: 1px solid #eae5d9 !important;}
            .frase-contracapa { font-family: 'Playfair Display', serif !important; font-size: 2.8rem !important; font-style: italic !important; color: #8c3a3a !important; line-height: 1.4 !important; margin-bottom: 3rem !important;}

            .ficha-catalografica { border: 2px solid #d4cbb8 !important; padding: 2.5rem !important; max-width: 700px !important; margin: 5rem auto !important; font-size: 1rem !important; color: #444 !important; line-height: 1.5 !important; background-color: #faf8f2 !important; text-align: left !important;}
            .ficha-header { font-weight: bold !important; text-align: center !important; margin-bottom: 1.5rem !important; text-transform: uppercase !important; font-size: 1.1rem !important;}

            /* --- TIPOGRAFIA DO TEXTO PRINCIPAL --- */
            .texto { font-size: 1.25rem !important; line-height: 1.85 !important; text-align: justify !important; margin-bottom: 1.5rem !important; }
            .texto-colunas { column-count: 2 !important; column-gap: 3.5rem !important; column-rule: 1px solid #eae5d9 !important; text-align: justify !important; }
            .dropcap::first-letter { float: left !important; font-size: 5.5rem !important; line-height: 0.8 !important; padding-top: 8px !important; padding-right: 12px !important; color: #8c3a3a !important; font-weight: 700 !important; }
            .subtitulo-capitulo { font-size: 2.5rem !important; color: #8c3a3a !important; border-bottom: 1px solid #eae5d9 !important; padding-bottom: 0.8rem !important; margin-top: 2rem !important; margin-bottom: 2.5rem !important; font-style: italic !important;}
            
            /* --- ESPAÇOS PARA IMAGENS (PLACEHOLDERS CORRIGIDOS) --- */
            .box-imagem { background-color: #f5f5f5 !important; border: 2px dashed #cccccc !important; border-radius: 4px !important; padding: 2rem !important; text-align: center !important; margin: 2rem 0 !important; width: 100% !important; min-height: 300px !important; display: flex !important; flex-direction: column !important; justify-content: center !important; align-items: center !important;}
            .box-imagem-full { min-height: 500px !important; margin: 0 !important; border: 2px solid #b3a996 !important; background-color: #ede9de !important;}
            .box-imagem span.tag { font-family: sans-serif !important; text-transform: uppercase !important; font-size: 1rem !important; font-weight: bold !important; color: #888888 !important; margin-bottom: 15px !important; letter-spacing: 2px !important;}
            .box-imagem span.desc { font-style: italic !important; color: #555555 !important; font-size: 1.2rem !important; max-width: 80% !important; text-align: center !important; line-height: 1.5 !important;}

            /* --- BOTÃO LADO B --- */
            .caixa-secreta { margin-top: 4rem !important; padding-top: 2rem !important; text-align: center !important;}
            .stButton { text-align: center !important; }
            .stButton > button { background-color: #ffffff !important; border: 1px solid #d4cbb8 !important; color: #8c3a3a !important; font-family: 'Lora', serif !important; font-size: 1.1rem !important; padding: 15px 30px !important; box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important; transition: all 0.3s !important; text-transform: uppercase !important; letter-spacing: 2px !important;}
            .stButton > button:hover { background-color: #8c3a3a !important; color: #ffffff !important; border: 1px solid #8c3a3a !important;}
        </style>
    """, unsafe_allow_html=True)

    # =========================================================
    # PÁGINA 1: CAPA
    # =========================================================
    st.markdown('''
    <div class="capa-container">
        <p class="instituicao-capa">E. E. Professora Ayna Torres | PIBID / UFSJ</p>
        <h1 class="titulo-capa">RELATÓRIO DA AÇÃO EXTENSIONISTA:<br>ENTRE O PLANEJAR, O FAZER E O SONHAR</h1>
        <p class="subtitulo-capa">A Poesia do Movimento</p>
        
        <div class="box-imagem box-imagem-full">
            <span class="tag">Espaço para a CAPA (Cena Inteira)</span>
            <span class="desc">Insira aqui a fotografia de maior impacto do projeto. Pode ser o auditório montado, um salto perfeito ou a silhueta dos alunos contra a luz. Esta é a vitrine do Caderno.</span>
        </div>
        
        <p class="texto" style="text-align: center; font-size: 1.2rem; margin-top: 2rem;">Minas Gerais, 2024</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    # =========================================================
    # PÁGINA 2: FICHA CATALOGRÁFICA E SUMÁRIO
    # =========================================================
    st.markdown('''
    <div class="ficha-catalografica">
        <div class="ficha-header">Dados Internacionais de Catalogação na Publicação (CIP)</div>
        <p style="margin-left: 2rem; text-indent: -2rem;">T694c</p>
        <p style="margin-left: 2rem;">Equipe PIBID/GPT - E.E. Professora Ayna Torres.</p>
        <p style="margin-left: 4rem; text-indent: -2rem;">Relatório da Ação Extensionista : entre o planejar, o fazer e o sonhar / [Autoria Coletiva] ; coordenação de Priscila de Sousa Martins, Cláudia Estéfana Santos Maciel. – São João del-Rei, MG : UFSJ/PIBID, 2024.</p>
        <p style="margin-left: 4rem;">Modo de acesso: World Wide Web</p>
        <p style="margin-left: 4rem;">Caderno Didático e Relatório de Vivências.</p>
        <p style="margin-left: 4rem;">1. Ginástica para Todos. 2. Educação Física Escolar. 3. Extensão Universitária. I. Martins, Priscila de Sousa (Coord.). II. Maciel, Cláudia Estéfana Santos (Coord.). III. Título.</p>
        <p style="text-align: right; margin-top: 1rem;">CDD 372.86</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    # =========================================================
    # PÁGINA 3: INTRODUÇÃO E CAPÍTULO 1
    # =========================================================
    st.markdown('<h2 class="subtitulo-capitulo" style="margin-top: 0 !important;">Apresentação</h2>', unsafe_allow_html=True)
    st.markdown('''
    <p class="texto dropcap">Neste caderno, datas e ponteiros do relógio importam menos do que as transformações que ocorreram nos espaços da Escola Estadual Professora Ayna Torres. A Ginástica para Todos (GPT) não foi apenas uma sequência de aulas práticas; foi um desafio, foi mudança, foi conflito e foi divertido demais!</p>
    <p class="texto">Deixamos os relatos cronológicos de lado para organizar nossas memórias através dos sentimentos, das barreiras quebradas e das conquistas coletivas.</p>
    ''', unsafe_allow_html=True)

    st.markdown('<h2 class="subtitulo-capitulo">O Peso do Tempo e o Despertar do Corpo</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.markdown('''
        <p class="texto dropcap">O tempo no Ensino Médio em Tempo Integral (EMTI) pode ser um rio longo, denso e exaustivo. Permanecer quase dez horas no ambiente escolar exige muito dos estudantes, um esforço que, nas palavras deles, "acaba com qualquer um" e exige muita coluna.</p>
        <p class="texto">O longo intervalo do almoço era vencido por corpos sentados, intermináveis partidas de Truco e prática deliberada de Futsal. Não que ficar sentado após o almoço seja algo negativo, na verdade é o fisiologicamente recomendado. Mas intervalo de almoço é verdadeiramente longo e visto como tedioso pelos alunos.</p>
        <p class="texto">O convite para o movimento encontrou, de início, a resistência natural de quem teme o novo. No primeiro dia de projeto, quando o portão se abriu, muitos alunos bateram em retirada para a quadra, buscando o conforto das práticas habituais.</p>
        <p class="texto">Mas com insistência, apoio dos bolsistas do PIBID e alguns vídeos legais, a semente da curiosidade foi plantada. Aos poucos, a rotina foi quebrada, e o auditório virou um refúgio de leveza onde o tempo, antes arrastado, passou a voar.</p>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
        <div class="box-imagem">
            <span class="tag">Fotografia de Contraste</span>
            <span class="desc">Insira a imagem que mostre o pátio vazio ou os primeiros alunos entrando curiosos no auditório para descobrir os colchonetes.</span>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    # =========================================================
    # PÁGINA 4: GALERIA VISUAL EXCLUSIVA 1 (SEM TEXTO)
    # =========================================================
    st.markdown('<h2 style="text-align: center; font-style: italic; color: #8c3a3a !important;">— Galeria Visual I: O Despertar —</h2>', unsafe_allow_html=True)
    
    st.markdown('''
        <div class="box-imagem box-imagem-full">
            <span class="tag">Página Exclusiva para GIF / Vídeo em Loop</span>
            <span class="desc">Aproveite esta página inteira para colocar um GIF ou Vídeo dinâmico (sem áudio) que mostre a ação acontecendo. Sem textos para roubar a atenção.</span>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    # =========================================================
    # PÁGINA 5: CAPÍTULOS 2 E 3
    # =========================================================
    st.markdown('<h2 class="subtitulo-capitulo" style="margin-top: 0 !important;">Vencendo o Medo do Desconhecido e o Preconceito</h2>', unsafe_allow_html=True)

    st.markdown('''
    <div class="texto-colunas">
        <p class="texto dropcap">Talvez a maior acrobacia realizada neste projeto não tenha sido física. O colchonete revelou que muitos de nós somos prisioneiros dos nossos próprios medos. Os alunos descobriram que o bloqueio mental é o verdadeiro causador de lesões: quando a gente evita o movimento por medo de se machucar, acaba se machucando.</p>
        <p class="texto">Havia preconceito a ser quebrado. O julgamento da sociedade pesava, rotulando quem praticava a ginástica com termos pejorativos. As meninas e os meninos enfrentavam o medo da sexualização e do olhar malicioso diante do básico: posições de quatro apoios e espacates, consideradas equivocadamente “vulgares”.</p>
        <p class="texto">O projeto foi o martelo que estilhaçou todo reflexo do olhar maldoso lá de fora. O ambiente seguro mostrou que a malícia habita a mente de quem assiste, e não a pureza do movimento. Eles aprenderam que a escola é exatamente o lugar para se abrir a cabeça e derrubar essas barreiras.</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('''
    <div class="box-imagem">
        <span class="tag">Vídeo / Foto Sequencial</span>
        <span class="desc">Alunos superando o medo inicial; capture o sorriso de alívio ao executar uma "estrelinha" ou um salto pela primeira vez.</span>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('<h2 class="subtitulo-capitulo">Construindo o Coletivo: Paciência e Fraternidade</h2>', unsafe_allow_html=True)

    col3, col4 = st.columns([1, 1.2], gap="large")

    with col3:
        st.markdown('''
        <div class="box-imagem" style="height: 100%;">
            <span class="tag">Retrato do Cuidado</span>
            <span class="desc">O toque de apoio; alunos auxiliando uns aos outros na execução das figuras acrobáticas em grupo.</span>
        </div>
        ''', unsafe_allow_html=True)

    with col4:
        st.markdown('''
        <p class="texto dropcap">Diferente da frieza das competições tradicionais, a GPT não carrega a balança dos jurados, as notas ou a rivalidade que cria inimizades. Sem a pressão de ser o melhor, o que floresceu foi a empatia.</p>
        <p class="texto">O corpo aprendeu novas rimas: pontes, velas, rolamentos à frente, saltos grupados, afastados e a execução precisa da estrelinha. Mas a alma aprendeu a virtude da paciência.</p>
        <p class="texto">A orientação calma ensinou os alunos a terem cautela com a dificuldade do outro. Rapidamente, eles mesmos começaram a se ajudar e a compreender que ninguém é igual a ninguém.</p>
        ''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    # =========================================================
    # PÁGINA 6: GALERIA VISUAL EXCLUSIVA 2 (MOSAICO)
    # =========================================================
    st.markdown('<h2 style="text-align: center; font-style: italic; color: #8c3a3a !important;">— Galeria Visual II: O Coletivo —</h2>', unsafe_allow_html=True)
    
    g_col1, g_col2 = st.columns(2, gap="large")
    with g_col1:
        st.markdown('''
        <div class="box-imagem box-imagem-full" style="min-height: 400px !important;">
            <span class="tag">Foto da Acrobacia</span>
            <span class="desc">Coreografia geométrica: a prova de que cada corpo, com seu próprio ritmo, é essencial para manter a figura em pé.</span>
        </div>
        ''', unsafe_allow_html=True)
    with g_col2:
        st.markdown('''
        <div class="box-imagem box-imagem-full" style="min-height: 400px !important;">
            <span class="tag">Foto da Escuta</span>
            <span class="desc">A roda de conversa e o preenchimento reflexivo dos questionários (TCLEs), momento de escuta e conexão.</span>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('''
    <p class="texto" style="text-align: center; margin-top: 1rem;">A ginástica uniu diferenças em um só movimento, respeitando o espaço e o limite de cada um.</p>
    ''', unsafe_allow_html=True)

    st.markdown('<hr class="quebra-pagina">', unsafe_allow_html=True)

    # =========================================================
    # PÁGINA 7: O FUTURO E A CONTRACAPA
    # =========================================================
    st.markdown('<h2 class="subtitulo-capitulo" style="margin-top: 0 !important;">A Semente que rola: O Futuro da GPT no Coletivo</h2>', unsafe_allow_html=True)

    st.markdown('''
    <div class="texto-colunas">
        <p class="texto dropcap">O fim do projeto é, na verdade, um começo. Transformados pela flexibilidade que ganharam no corpo e na mente, os alunos sonham mais alto.</p>
        <p class="texto">Há um desejo de plantar essa semente, levando a GPT para as crianças do 6º ano do ensino fundamental. Eles sabem que corpos mais jovens absorvem o movimento mais rápido e que mentes mais novas podem crescer blindadas contra os preconceitos que eles próprios tiveram que desconstruir.</p>
        <p class="texto">E o auditório da escola já ficou pequeno. O novo sonho pulsa nas ruas da cidade: há o desejo de levar as coreografias para além dos muros da escola, nas aglomerações da cidade aos finais de semana. Apresentar a poesia da GPT para a comunidade é a forma definitiva de mostrar que a ginástica é verdadeiramente PARA TODOS.</p>
    </div>
    ''', unsafe_allow_html=True)

    # A Contracapa
    st.markdown('''
    <div class="contracapa-container">
        <p class="frase-contracapa">"Apresentar a poesia da GPT para a comunidade é a forma definitiva de mostrar que a ginástica é verdadeiramente PARA TODOS."</p>
        
        <div class="box-imagem box-imagem-full" style="width: 100%;">
            <span class="tag">A GRANDE FOTO FINAL (CONTRACAPA)</span>
            <span class="desc">Insira a grande foto em grupo do último encontro, com a equipe da universidade (Priscila e Cláudia) e o brilho nos olhos de quem descobriu a força do próprio corpo.</span>
        </div>
        
        <p class="texto" style="text-align: center; margin-top: 3rem; color: #888888 !important; font-size: 1rem !important;">
            A execução deste projeto foi possível graças à parceria entre a Escola Estadual Professora Ayna Torres, a Universidade Federal de São João del-Rei (UFSJ) e o Programa Institucional de Bolsas de Iniciação à Docência (PIBID / CAPES).
        </p>
    </div>
    ''', unsafe_allow_html=True)

    # Botão Lado B (Anexo Confidencial)
    st.markdown('''
    <div class="caixa-secreta">
        <p style="color: #8c3a3a !important; font-family: 'Special Elite', monospace !important; font-size: 1.2rem !important; margin-bottom: 5px !important; font-weight: bold !important;">[ATENÇÃO: ANEXO NÃO OFICIAL DETECTADO]</p>
        <p style="color: #555555 !important; font-style: italic !important; font-size: 1rem !important; margin-bottom: 20px !important;">Um dossiê adicional escrito nos bastidores foi ocultado neste documento.</p>
    ''', unsafe_allow_html=True)
    st.button("ACESSAR ARQUIVO CONFIDENCIAL: A VERDADEIRA HISTÓRIA DO PORTÃO", on_click=alternar_fita)
    st.markdown('</div>', unsafe_allow_html=True)
