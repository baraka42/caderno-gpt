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
<p class="dossie-texto" style="font-size:1.3rem; margin-top:2rem;">A maioria das pessoas vive sem saber de um segredo essencial: o peso das coisas não é o mesmo em todos os lugares.</p>
<p class="dossie-texto" style="font-size:1.3rem;">Quem trabalha em Escola sabe disso. E eu, Professor de Educação Física, deveria até saber mais que todo mundo. Eu estava prestes a testemunhar, mais uma vez, as consequências desse fenômeno.</p>
<p class="dossie-texto" style="font-size:1.3rem;">Mas antes de contar o que aconteceu, preciso explicar uma coisa.</p>
<p class="dossie-texto" style="font-size:1.3rem;">O "Ranca" não é uma simples brincadeira. Não é uma pelada desorganizada. O Ranca é uma força da natureza. <span class="marca-texto">O Ranca não tem MÃE!</span> É Um evento espontâneo com poderes magnéticos, capaz de atrair corpos desavisados e os envolver num ritual de suor, gritos e dedões do pé dilacerados. <span class="censura">“Toca essa bola, C@#$%%0!!!”</span></p>
<p class="dossie-texto" style="font-size:1.3rem;">Sabendo disso ou não, lá fui eu.</p>
<p class="dossie-texto" style="font-size:1.3rem;">Era o primeiro dia de tentativa de apresentar o projeto de Ginástica Para Todos para os alunos do Integral. Fui de sala em sala no horário do almoço, quando os alunos ainda não tinham terminado de comer, além dos que encontrava pelos corredores. O plano era simples: convidar todo mundo para ir até o auditório, fazer uma demonstração, explicar o que é a Ginástica Para Todos e tentar conquistar aquele povo para a nova prática. Porque nada conquista mais um adolescente do ensino integral do que interromper a única pausa que ele tem no dia para falar sobre atividade física.</p>
<p class="dossie-texto" style="font-size:1.3rem;">Fui. Salas visitadas, alunos abordados, convites feitos. Tudo dentro do planejado. Dialógico.</p>
<p class="dossie-texto" style="text-align: center; font-size: 1.5rem; margin: 3rem 0; font-weight:bold;">Às onze e meia da manhã do dia dez de março, testemunhei o inevitável.</p>
<p class="dossie-texto" style="text-align: center; font-size: 2rem; color: #b32424 !important; border: 2px solid #b32424; padding: 10px; transform: rotate(1deg);">Alguém abriu o portão da quadra.</p>
<p class="dossie-texto" style="font-size:1.3rem;">Não foi um evento grandioso. Não teve anúncio, não teve alarde. Foi só um portão se abrindo. Mas, para quem tem intimidade com escola, sabe que aquilo é equivalente ao sinal do recreio em dia que a merenda é cachorro-quente. Mais que depressa, a maioria dos alunos bateu em retirada. Não foi desinteresse, não foi maldade. Foi pura e simplesmente a força da gravidade local agindo. Eles correram para a quadra em busca de outra dose para saciar a coceira das pernas. O Ranca.</p>
<p class="dossie-texto" style="font-size:1.3rem;">Lá no auditório, esperei. E esperei. E continuei esperando.</p>
<p class="dossie-texto" style="font-size:1.3rem;">No final, alguns poucos alunos restaram. Não eram necessariamente os mais interessados em ginástica. Eram, muito provavelmente, os que sentiram vergonha de me deixar falando sozinho. Eles ficaram até o fim, ouviram a explicação inteira, nunca tinha testemunhado tamanha delicadeza, alguns até acenaram com a cabeça em momentos estratégicos.</p>
<p class="dossie-texto" style="font-size:1.3rem;">Lá fora, no chão quente da quadra, o Ranca rugia.</p>
<p class="dossie-texto" style="font-size:1.3rem;">E eu entendi, naquele dia, que o universo tem suas próprias leis. Você pode planejar, convidar, explicar, demonstrar. Pode ir de sala em sala no horário do almoço, abordar aluno por aluno nos corredores. Pode ser o sujeito mais otimista e sonhador da face da Terra.</p>
<p class="dossie-texto" style="font-size:1.3rem;">Mas se alguém abrir o portão da quadra, não adianta.</p>
<p class="dossie-texto" style="font-size:2.5rem; text-align: center; margin-top: 3rem; color: #b32424 !important; font-weight:bold;">O Ranca é inevitável!</p>
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
    .titulo-capa { font-size: 4rem !important; font-weight: 700 !important; text-align: center !important; line-height: 1.2 !important; margin-bottom: 1rem !important; }
    .subtitulo-capitulo { font-size: 2.5rem !important; color: #8c3a3a !important; border-bottom: 1px solid #eae5d9 !important; padding-bottom: 0.8rem !important; margin-top: 5rem !important; font-style: italic !important;}
    .dropcap::first-letter { float: left !important; font-size: 5.5rem !important; line-height: 0.8 !important; padding-right: 12px !important; color: #8c3a3a !important; font-weight: 700 !important; }
    
    .box-imagem { background-color: #f5f5f5 !important; border: 2px dashed #cccccc !important; border-radius: 4px !important; padding: 40px !important; text-align: center !important; margin: 2rem 0 !important; display: block !important; width: 100% !important;}
    .tag-midia { font-family: sans-serif !important; text-transform: uppercase !important; font-size: 0.9rem !important; font-weight: bold !important; color: #888 !important; display: block !important; margin-bottom: 15px !important;}
    .desc-midia { font-style: italic !important; color: #555 !important; font-size: 1.2rem !important; display: block !important; line-height: 1.5 !important;}
    
    .secao-galeria { background-color: #faf9f6 !important; padding: 4rem 2rem !important; border: 1px solid #eee !important; margin: 4rem 0 !important; text-align: center !important;}
    .frase-impacto { font-family: 'Playfair Display', serif !important; font-size: 2.8rem !important; font-style: italic !important; color: #8c3a3a !important; text-align: center !important; margin: 4rem 0 !important; padding: 0 10% !important; line-height: 1.4 !important;}
    
    header, footer { visibility: hidden !important; }
    .stButton > button { background-color: #fffdf8 !important; border: 1px solid #d4cbb8 !important; color: #8c3a3a !important; width: 100% !important; padding: 20px !important; text-transform: uppercase !important; letter-spacing: 2px !important; }
</style>
""", unsafe_allow_html=True)

    # --- PÁGINA 1: CAPA ---
    st.markdown('<p style="text-align:center; letter-spacing: 4px; color: #8c3a3a !important; font-weight:bold;">E. E. PROFESSORA AYNA TORRES | PIBID</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="titulo-capa">RELATÓRIO DA AÇÃO EXTENSIONISTA:<br>ENTRE O PLANEJAR, O FAZER E O SONHAR</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size: 1.8rem; font-style: italic; color: #555 !important;">A Poesia do Movimento</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="box-imagem" style="min-height:500px;"><span class="tag-midia">Fotografia de Capa</span><span class="desc-midia">Insira aqui a imagem de maior impacto do seu Caderno Didático (ex: auditório cheio ou movimento capturado).</span></div>', unsafe_allow_html=True)
    
    st.markdown('<p style="text-align: center; font-size: 1.3rem; margin-top: 2rem;">Minas Gerais, 2024</p>', unsafe_allow_html=True)

    # --- INTRODUÇÃO ---
    st.markdown('<h2 class="subtitulo-capitulo">Apresentação</h2>', unsafe_allow_html=True)
    st.markdown('<p class="texto dropcap" style="font-size:1.3rem;">Neste caderno, datas e ponteiros do relógio importam menos do que as transformações que ocorreram nos espaços da Escola Estadual Professora Ayna Torres. A Ginástica para Todos (GPT) não foi apenas uma sequência de aulas práticas; foi um desafio, foi mudança, foi conflito e foi divertido demais!</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto" style="font-size:1.3rem;">Deixamos os relatos cronológicos de lado para organizar nossas memórias através dos sentimentos, das barreiras quebradas e das conquistas coletivas.</p>', unsafe_allow_html=True)

    # --- CAPÍTULO 1: O PESO DO TEMPO ---
    st.markdown('<h2 class="subtitulo-capitulo">O Peso do Tempo e o Despertar do Corpo</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.markdown('''
<p class="texto" style="font-size:1.25rem;">O tempo no Ensino Médio em Tempo Integral (EMTI) pode ser um rio longo, denso e exaustivo. Permanecer quase dez horas no ambiente escolar exige muito dos estudantes, um esforço que, nas palavras deles, "acaba com qualquer um" e exige muita coluna.</p>
<p class="texto" style="font-size:1.25rem;">O longo intervalo do almoço era vencido por corpos sentados, intermináveis partidas de Truco e prática deliberada de Futsal. Não que ficar sentado após o almoço seja algo negativo, na verdade é o fisiologicamente recomendado. Mas intervalo de almoço é verdadeiramente longo e visto como tedioso pelos alunos.</p>
<p class="texto" style="font-size:1.25rem;">O convite para o movimento encontrou, de início, a resistência natural de quem teme o novo. No primeiro dia de projeto, quando o portão se abriu, muitos alunos bateram em retirada para a quadra, buscando o conforto das práticas habituais. Mas com insistência, apoio dos bolsistas do PIBID e alguns vídeos legais, a semente da curiosidade foi plantada. Aos poucos, a rotina foi quebrada, e o auditório virou um refúgio de leveza onde o tempo, antes arrastado, passou a voar.</p>
''', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="box-imagem"><span class="tag-midia">FOTO: O DESPERTAR</span><span class="desc-midia">Contraste entre o pátio vazio e os primeiros alunos entrando no auditório.</span></div>', unsafe_allow_html=True)

    # --- PÁGINA: GALERIA VISUAL I ---
    st.markdown('<div class="secao-galeria"><h3 style="margin-bottom:2rem; font-style:italic; color:#8c3a3a !important;">— Mosaico Visual I: A Descoberta do Movimento —</h3>', unsafe_allow_html=True)
    g1, g2 = st.columns(2)
    with g1: st.markdown('<div class="box-imagem" style="min-height:450px;"><span class="tag-midia">GIF / VÍDEO EM LOOP</span><span class="desc-midia">Auditório ganhando vida ou sequência de movimentos iniciais.</span></div>', unsafe_allow_html=True)
    with g2: st.markdown('<div class="box-imagem" style="min-height:450px;"><span class="tag-midia">FOTO DE DETALHE</span><span class="desc-midia">A descoberta dos colchonetes ou expressões faciais de curiosidade.</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CAPÍTULO 2: VENCENDO O MEDO ---
    st.markdown('<h2 class="subtitulo-capitulo">Vencendo o Medo do Desconhecido e o Preconceito</h2>', unsafe_allow_html=True)
    st.markdown('''
<p class="texto" style="font-size:1.25rem;">Talvez a maior acrobacia realizada neste projeto não tenha sido física. O colchonete revelou que muitos de nós somos prisioneiros dos nossos próprios medos. Os alunos descobriram que o bloqueio mental é o verdadeiro causador de lesões: quando a gente evita o movimento por medo de se machucar, acaba se machucando.</p>
<p class="texto" style="font-size:1.25rem;">Havia preconceito a ser quebrado. O julgamento da sociedade pesava, rotulando quem praticava a ginástica com termos pejorativos. As meninas e os meninos enfrentavam o medo da sexualização e do olhar malicioso diante do básico: posições de quatro apoios e espacates, consideradas equivocadamente “vulgares”.</p>
<p class="texto" style="font-size:1.25rem;">O projeto foi o martelo que estilhaçou todo reflexo do olhar maldoso lá de fora. O ambiente seguro mostrou que a malícia habita a mente de quem assiste, e não a pureza do movimento. Eles aprenderam que a escola é exatamente o lugar para se abrir a cabeça e derrubar essas barreiras.</p>
''', unsafe_allow_html=True)
    st.markdown('<div class="box-imagem" style="min-height:400px;"><span class="tag-midia">VÍDEO / FOTO DE SUPERAÇÃO</span><span class="desc-midia">O sorriso de alívio ao executar uma "estrelinha" ou um salto pela primeira vez.</span></div>', unsafe_allow_html=True)

    # --- CAPÍTULO 3: COLETIVO ---
    st.markdown('<h2 class="subtitulo-capitulo">Construindo o Coletivo: Paciência e Fraternidade</h2>', unsafe_allow_html=True)
    st.markdown('''
<p class="texto" style="font-size:1.25rem;">Diferente da frieza das competições tradicionais, a GPT não carrega a balança dos jurados, as notas ou a rivalidade que cria inimizades. Sem a pressão de ser o melhor, o que floresceu foi a empatia.</p>
<p class="texto" style="font-size:1.25rem;">O corpo aprendeu novas rimas: pontes, velas, rolamentos à frente, saltos grupados, afastados e a execução precisa da estrelinha. Mas a alma aprendeu a virtude da paciência. A orientação calma ensinou os alunos a terem cautela com a dificuldade do outro. Rapidamente, eles mesmos começaram a se ajudar e a compreender que ninguém é igual a ninguém.</p>
<p class="texto" style="font-size:1.25rem;">As coreografias geométricas não foram apenas demonstrações físicas, mas a prova de que cada corpo, com seu próprio ritmo, é essencial para manter a figura acrobática em pé. A ginástica uniu diferenças em um só movimento, respeitando o espaço e o limite de cada um.</p>
''', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3: st.markdown('<div class="box-imagem"><span class="tag-midia">FOTO APOIO</span><span class="desc-midia">O toque de cuidado; alunos auxiliando uns aos outros nas acrobacias.</span></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="box-imagem"><span class="tag-midia">FOTO RODA</span><span class="desc-midia">Roda de conversa e o preenchimento reflexivo dos questionários (TCLEs).</span></div>', unsafe_allow_html=True)

    # --- CAPÍTULO 4: O FUTURO ---
    st.markdown('<h2 class="subtitulo-capitulo">A Semente que rola: O Futuro da GPT no Coletivo</h2>', unsafe_allow_html=True)
    st.markdown('''
<p class="texto" style="font-size:1.25rem;">O fim do projeto é, na verdade, um começo. Transformados pela flexibilidade que ganharam no corpo e na mente, os alunos sonham mais alto. Há um desejo de plantar essa semente, levando a GPT para as crianças do 6º ano do ensino fundamental. Eles sabem que corpos mais jovens absorvem o movimento mais rápido e que mentes mais novas podem crescer blindadas contra os preconceitos que eles próprios tiveram que desconstruir.</p>
<p class="texto" style="font-size:1.25rem;">E o auditório da escola já ficou pequeno. O novo sonho pulsa nas ruas da cidade: há o desejo de levar as coreografias para além dos muros da escola, nas aglomerações da cidade aos finais de semana. Apresentar a poesia da GPT para a comunidade é a forma definitiva de mostrar que a ginástica é verdadeiramente PARA TODOS.</p>
''', unsafe_allow_html=True)

    # --- PÁGINA FINAL: CONTRACAPA ---
    st.markdown('<div style="background-color: #faf8f2; border: 1px solid #eae5d9; padding: 4rem 2rem; text-align: center; margin-top:4rem;">', unsafe_allow_html=True)
    st.markdown('<p class="frase-impacto">"Apresentar a poesia da GPT para a comunidade é a forma definitiva de mostrar que a ginástica é verdadeiramente PARA TODOS."</p>', unsafe_allow_html=True)
    st.markdown('<div class="box-imagem" style="min-height:500px; background-color:white !important;"><span class="tag-midia">GRANDE FOTO FINAL (CONTRACAPA)</span><span class="desc-midia">Foto em grupo do último encontro, com equipe e alunos celebrando.</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight:bold; color:#8c3a3a !important; margin-top:2rem;">UFSJ | PIBID | MINAS GERAIS, 2024</p></div>', unsafe_allow_html=True)

    # --- BOTÃO LADO B ---
    st.markdown('<div style="margin-top: 5rem; text-align: center; border-top:1px dashed #ccc; padding-top:3rem;">', unsafe_allow_html=True)
    st.button("⚠️ ACESSAR ANEXO CONFIDENCIAL: O GUIA DO PROFESSOR", on_click=alternar_dimensao)
    st.markdown('</div>', unsafe_allow_html=True)
