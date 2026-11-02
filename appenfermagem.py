import streamlit as st

st.set_page_config(page_title="Anotação de Enfermagem", layout="centered")

st.title("🩺 Gerador de Anotaçãoo de Enfermagem")
st.write("Preencha os campos e marque os itens conforme o exame físico:")

# --- 1. NEUROLÓGICO (GLASGOW, RASS E PUPILAS) ---
st.subheader("1. Neurológico, RASS e Pupilas")

col1, col2, col3 = st.columns(3)
with col1:
    ao = st.selectbox("Abertura Ocular (AO):", [
        (4, "Espontânea"), 
        (3, "À voz"), 
        (2, "À pressão"), 
        (1, "Nenhuma")
    ], format_func=lambda x: f"AO{x[0]} - {x[1]}")
with col2:
    rv = st.selectbox("Resposta Verbal (RV):", [
        (5, "Orientado"), 
        (4, "Confuso"), 
        (3, "Palavras inapropriadas"), 
        (2, "Sons incompreensíveis"), 
        (1, "Ausente / Tubo orotraqueal (T)")
    ], format_func=lambda x: f"RV{x[0]} - {x[1]}")
with col3:
    rm = st.selectbox("Resposta Motora (RM):", [
        (6, "Obedece comandos"), 
        (5, "Localiza dor"), 
        (4, "Flexão de retirada"), 
        (3, "Flexão anormal"), 
        (2, "Extensão anormal"), 
        (1, "Nenhuma")
    ], format_func=lambda x: f"RM{x[0]} - {x[1]}")

glasgow_total = ao[0] + rv[0] + rm[0]
rv_sigla = "1T" if rv[0] == 1 else str(rv[0])
glasgow_str = f"G{glasgow_total}T (AO{ao[0]}, RV{rv_sigla}, RM{rm[0]})"

rass = st.selectbox("RASS:", ["-5", "-4", "-3", "-2", "-1", "0", "+1", "+2", "+3", "+4"], index=1)

col_p1, col_p2 = st.columns(2)
with col_p1:
    pupila_tipo = st.selectbox("Pupilas:", ["isocóricas", "anisocóricas", "midriáticas", "mióticas"])
with col_p2:
    pupila_reacao = st.selectbox("Fotorreação:", ["fotorreagentes", "não fotorreagentes"])

pupila_str = f"pupilas {pupila_tipo} {pupila_reacao}"


# --- 2. COMPORTAMENTO NO LEITO, CRÂNIO E CERVICAL ---
st.subheader("2. Comportamento no Leito, Crânio e Cervical")
comportamento = st.text_input("Comportamento no leito:", "apresenta-se sedado, acamado, hipocorado, eupneico, afebril, anictérico, acianótico")

tem_fo_cranio = st.checkbox("Possui FO / Lesão em Crânio")
fo_cranio_local = ""
fo_cranio_estado = ""
if tem_fo_cranio:
    fo_cranio_local = st.selectbox("Local da FO em Crânio:", ["parietal", "occipital", "frontal"])
    fo_cranio_estado = st.selectbox("Estado da FO em Crânio:", ["limpa e seca", "com secreção", "com deiscência"])

tem_dreno_cabeca = st.checkbox("Possui Dreno na Cabeça")
dreno_cabeca_tipo = st.selectbox("Tipo de dreno na cabeça:", ["DVE", "Portovac"]) if tem_dreno_cabeca else ""

tem_cervical = st.checkbox("Possui FO ou Dreno em Região Cervical")
cervical_opcao = ""
if tem_cervical:
    cervical_opcao = st.selectbox("Selecione a condição cervical:", [
        "FO cervical a direita", 
        "FO cervical a esquerda", 
        "FO cervical bilateral", 
        "dreno JP a esquerda", 
        "dreno JP a direita", 
        "dreno JP bilateral"
    ])


# --- 3. TÓRAX E DISPOSITIVOS TORÁCICOS ---
st.subheader("3. Tórax e Aparelho Cardiopulmonar")
expansibilidade = st.selectbox("Expansibilidade do Tórax:", [
    "Tórax simétrico com boa expansibilidade preservada", 
    "Tórax com expansibilidade reduzida"
])

ausculta_pulm = st.multiselect("Ausculta Pulmonar:", [
    "MV presentes", 
    "MV reduzidos em ápices", 
    "MV reduzidos em bases", 
    "MV reduzidos", 
    "roncos", 
    "estertores", 
    "crepitações", 
    "sibilos"
])

ausculta_card = st.selectbox("Ausculta Cardíaca:", ["BRNF 2T", "arrítmica"])

tem_portocath = st.checkbox("Port-cath")
portocath_lado = st.selectbox("Lado do Port-cath:", ["hemitórax direito", "hemitórax esquerdo"]) if tem_portocath else ""
portocath_ag = st.checkbox("Port-cath agulhado") if tem_portocath else False

tem_dreno_torax = st.checkbox("Drenos Torácicos / Pleurais")
dreno_torax_tipo = ""
dreno_torax_lado = ""
if tem_dreno_torax:
    dreno_torax_tipo = st.selectbox("Tipo de dreno torácico:", [
        "dreno JP", 
        "dreno de tórax", 
        "dreno tubular com selo d'água", 
        "pigtail"
    ])
    dreno_torax_lado = st.selectbox("Lado do dreno torácico:", ["hemitórax direito", "hemitórax esquerdo"])
    dreno_torax_det = st.text_input("Detalhes do débito/curativo do dreno:", "com débito sanguinolento, oscilante")


# --- 4. ABDÔMEN, OSTOMIAS E SONDAS NASOENTERAIS/GÁSTRICAS ---
st.subheader("4. Abdômen, Ostomias e Sondas")
abd_forma = st.selectbox("Forma do Abdômen:", ["plano", "globoso", "escavado", "gravídico", "ascítico"])
abd_palpacao = st.selectbox("Palpação:", ["flácido à palpação", "depressível à palpação", "tenso à palpação"])
rha = st.selectbox("RHA:", ["presentes", "ausentes", "reduzidos"])
percussao = st.selectbox("Percussão:", ["timpânico", "maciço"])

tem_fo_abd = st.checkbox("FO Abdominal")
fo_abd_tipo = ""
fo_abd_estado = ""
if tem_fo_abd:
    fo_abd_tipo = st.selectbox("Tipo de FO Abdominal:", ["abdominal longitudinal", "transversal", "em picos"])
    fo_abd_estado = st.selectbox("Estado da FO Abdominal:", ["limpa e seca", "com secreção", "com deiscência"])

tem_ostomia = st.checkbox("Ostomia")
ostomia_tipo = ""
ostomia_status = ""
if tem_ostomia:
    ostomia_tipo = st.selectbox("Tipo de ostomia:", ["colostomia", "ileostomia", "gastrostomia"])
    if ostomia_tipo in ["colostomia", "ileostomia"]:
        ostomia_status = st.selectbox("Status:", ["funcionante", "não funcionante"])
    else:
        ostomia_status = st.selectbox("Status:", ["aberta", "fechada", "recebendo dieta enteral"])

tem_dreno_abd = st.checkbox("Drenos Abdominais")
dreno_abd_tipo = ""
dreno_abd_local = ""
if tem_dreno_abd:
    dreno_abd_tipo = st.selectbox("Tipo de dreno abdominal:", ["dreno tubular", "dreno JP"])
    dreno_abd_local = st.selectbox("Local do dreno:", ["flanco direito", "flanco esquerdo", "hipocôndrio direito", "hipocôndrio esquerdo", "epigástrio"])

tem_cne = st.checkbox("CNE / CNG")
cne_narina = ""
cne_status = ""
cne_vazao = ""
if tem_cne:
    cne_narina = st.selectbox("Narina:", ["narina D", "narina E"])
    cne_status = st.selectbox("Condição CNE:", ["aberta", "fechada", "recebendo dieta enteral"])
    if cne_status == "recebendo dieta enteral":
        cne_vazao = st.text_input("Vazão da Dieta (ex: a 10ml/h):", "a 10ml/h")


# --- 5. SUPORTE RESPIRATÓRIO (VM / OXIGENIOTERAPIA) ---
st.subheader("5. Suporte Respiratório")
tipo_suporte = st.selectbox("Tipo de Suporte:", ["Nenhum / Espontâneo", "Tubo Orotraqueal (TOT) em VM", "Cateter O2", "Máscara Não Reinalante (MNR)", "Máscara de Reservatório"])

tot_num = ""
tot_rl = ""
vm_det = ""
if tipo_suporte == "Tubo Orotraqueal (TOT) em VM":
    tot_num = st.selectbox("Número do Tubo:", ["6,0", "6,5", "7,0", "7,5", "8,0", "8,5", "9,0"], index=3)
    tot_rl = st.text_input("Fixação RL (cm):", "24cm")
    vm_det = st.text_input("Parâmetros VM:", "modo pressão controlada, FiO2 40%, peep 7")


# --- 6. ACESSOS VASCULARES ---
st.subheader("6. Acessos Vasculares, Diálise e Peridural")
tem_acesso_perf = st.checkbox("Acesso Venoso Periférico (AVP)")
avp_det = st.text_input("Detalhes AVP:", "AVP em MSD (jelco 22, 30/10) ocluído com película transparente") if tem_acesso_perf else ""

tem_picc = st.checkbox("PICC")
picc_det = st.text_input("Detalhes PICC:", "PICC MN/DL em MSE ocluído com película transparente") if tem_picc else ""

tem_cvc = st.checkbox("CVC / Shilley / Permicath")
cvc_tipo = st.selectbox("Tipo de Cateter:", ["CVC", "Shilley", "Permicath"]) if tem_cvc else ""
cvc_local = st.selectbox("Local:", ["VJD", "VJE", "VSCE", "VSCD", "VFD", "VFE"]) if tem_cvc else ""
cvc_curativo = st.selectbox("Tipo de Curativo:", ["filme transparente", "gaze + filme transparente"]) if tem_cvc else ""
cvc_sinais = st.checkbox("Apresenta sinais flogísticos / sujidades") if tem_cvc else False
cvc_infusao = st.text_input("Infusões / Vazões:", "recebendo Noradrenalina 5ml/h, Propofol 15ml/h") if tem_cvc else ""

tem_dialise = st.checkbox("Em Terapia Dialítica Contínua")
dialise_det = st.text_input("Detalhes da Diálise:", "máquina Multifiltrate, controles em impresso próprio") if tem_dialise else ""

tem_peridural = st.checkbox("Cateter Peridural com PCA")
peridural_det = st.text_input("Detalhes Peridural/PCA:", "com PCA (Bupivacaína + Fentanil), fluxo 4ml/h") if tem_peridural else ""


# --- 7. ELIMINAÇÕES / CVD ---
st.subheader("7. Sistema Urinário e Diurese")
tipo_diurese = st.selectbox("Controle de Diurese / Eliminação:", ["micção espontânea", "CVD", "Bricker"])
cvd_fr = ""
debito_cor = ""
if tipo_diurese == "CVD":
    cvd_fr = st.selectbox("Calibre CVD (Fr):", [12, 14, 16, 18, 20, 22, 24], index=2)
    debito_cor = st.selectbox("Cor do Débito:", ["límpido", "claro", "concentrado", "colúrico", "hematúrico"])


# --- 8. MEMBROS (MMSS / MMII) ---
st.subheader("8. Membros (MMSS e MMII)")
mmss_edema = st.checkbox("Edema em MMSS")
mmii_edema = st.checkbox("Edema em MMII")

mmss_hematoma = st.checkbox("Hematoma em MMSS")
mmii_hematoma = st.checkbox("Hematoma em MMII")

contencao_mmss = st.checkbox("Contenção mecânica em MMSS")
contencao_mmii = st.checkbox("Contenção mecânica em MMII")
garroteamento = st.checkbox("Sinais de garroteamento")

perfusao_status = st.selectbox("Perfusão Periférica:", ["regular perfusão periférica", "boa perfusão periférica", "má perfusão periférica"])
pulsos = st.selectbox("Pulsos:", ["pulsos cheios", "pulsos filiformes"])
tec = st.selectbox("TEC (Tempo de Enchimento Capilar):", ["TEC < 2s", "TEC > 2s"])
usa_fralda = st.checkbox("Em uso de fralda", value=True)


# --- 9. LESÕES E DOR ---
st.subheader("9. Pele, Lesões por Pressão e Dor")
tem_lpp = st.checkbox("Apresenta Lesão por Pressão (LPP)")
lpp_estagio = ""
lpp_descricao = ""
if tem_lpp:
    lpp_estagio = st.selectbox("Estágio/Classificação LPP:", ["Grau I", "Grau II", "Grau III", "Grau IV", "tissular profunda", "not classificável"])
    lpp_descricao = st.text_input("Descrição da LPP:", "em região sacra de aproximadamente 5x3cm com tecido necrótico")

queixa_dor = st.selectbox("Queixa de Dor:", ["sem sinais de dor", "refere dor leve", "refere dor moderada", "refere dor intensa"])


# ==========================================
# MONTAGEM AUTOMÁTICA DA EVOLUÇÃO CÉFALO-CAUDAL (FLUIDA POR VÍRGULAS)
# ==========================================
texto = f"07:00 Recebo plantão com paciente no leito, grades e decúbito elevados, rodas travadas, monitorização multiparâmetros, {glasgow_str}, RASS {rass}, {pupila_str}, {comportamento}. "

# Crânio / Cervical fluidos
craneo_partes = []
if tem_fo_cranio:
    craneo_partes.append(f"FO em região {fo_cranio_local}, {fo_cranio_estado}")
if tem_dreno_cabeca:
    craneo_partes.append(f"com {dreno_cabeca_tipo}")
if tem_cervical:
    craneo_partes.append(f"região cervical com {cervical_opcao}")

if craneo_partes:
    texto += f"{', '.join(craneo_partes)}. "

# Tórax com vírgulas internas
torax_partes = [expansibilidade]
if ausculta_pulm:
    torax_partes.append(f"à AP {', '.join(ausculta_pulm)}")
torax_partes.append(f"à AC {ausculta_card}")

texto += f"{', '.join(torax_partes)}. "

if tem_portocath:
    texto += f"Port-cath em {portocath_lado}" + (" agulhado. " if portocath_ag else " não agulhado. ")

if tem_dreno_torax:
    texto += f"{dreno_torax_tipo} em {dreno_torax_lado} ({dreno_torax_det}). "

# Abdômen com vírgulas internas ligando tudo
abd_partes = [f"abdômen {abd_forma}", abd_palpacao, f"RHA {rha}", f"{percussao} à percussão"]
if tem_fo_abd:
    abd_partes.append(f"FO abdominal {fo_abd_tipo}, {fo_abd_estado}")
if tem_ostomia:
    if ostomia_tipo in ["colostomia", "ileostomia"]:
        abd_partes.append(f"{ostomia_tipo} acoplada à bolsa de Karaya, {ostomia_status}")
    else:
        abd_partes.append(f"{ostomia_tipo} {ostomia_status}")
if tem_dreno_abd:
    abd_partes.append(f"{dreno_abd_tipo} em {dreno_abd_local}")
if tem_cne:
    if cne_status == "recebendo dieta enteral":
        abd_partes.append(f"mantém CNE em {cne_narina} recebendo dieta enteral {cne_vazao}")
    else:
        abd_partes.append(f"mantém CNE em {cne_narina} {cne_status}")

texto += f"{', '.join(abd_partes)}. "

# Suporte respiratório
if tipo_suporte == "Tubo Orotraqueal (TOT) em VM":
    texto += f"IOT (COT {tot_num}, RL {tot_rl}) em VM ({vm_det}). "
elif tipo_suporte == "Cateter O2":
    texto += "Em uso de cateter de oxigênio. "
elif tipo_suporte == "Máscara Não Reinalante (MNR)":
    texto += "Em uso de máscara não reinalante. "
elif tipo_suporte == "Máscara de Reservatório":
    texto += "Em uso de máscara de reservatório. "

if tem_cvc:
    texto += f"{cvc_tipo} em {cvc_local} ocluído com {cvc_curativo}"
    if cvc_sinais:
        texto += ", com sinais flogísticos/sujidades"
    else:
        texto += ", sem sinais flogísticos"
    texto += f", {cvc_infusao}. "

if tem_picc:
    texto += f"{picc_det}. "
if tem_acesso_perf:
    texto += f"{avp_det}. "
if tem_dialise:
    texto += f"Em diálise contínua ({dialise_det}). "
if tem_peridural:
    texto += f"Cateter peridural em região lombar {peridural_det}. "

if tipo_diurese == "CVD":
    texto += f"CVD {cvd_fr}Fr em sistema fechado com débito {debito_cor}. "
elif tipo_diurese == "Bricker":
    texto += "Em uso de bolsa de Bricker. "
else:
    texto += "Em micção espontânea. "

# Membros (MMSS / MMII)
edemas_lista = []
if mmss_edema: edemas_lista.append("MMSS")
if mmii_edema: edemas_lista.append("MMII")
edema_txt = f"edema em {' e '.join(edemas_lista)}" if edemas_lista else "ausência de edemas"

hematomas_lista = []
if mmss_hematoma: hematomas_lista.append("MMSS")
if mmii_hematoma: hematomas_lista.append("MMII")
hematoma_txt = f"hematomas em {' e '.join(hematomas_lista)}" if hematomas_lista else ""

contencao_lista = []
if contencao_mmss: contencao_lista.append("MMSS")
if contencao_mmii: contencao_lista.append("MMII")
contencao_txt = f"contenção mecânica em {' e '.join(contencao_lista)}" if contencao_lista else ""

membros_partes = [edema_txt]
if hematoma_txt: membros_partes.append(hematoma_txt)
if contencao_txt: membros_partes.append(contencao_txt)
if garroteamento: membros_partes.append("sem sinais de garroteamento")

texto += f"Membros com {', '.join(membros_partes)}. "
texto += f"Pulsos {pulsos}, {perfusao_status}, {tec}. "

if usa_fralda:
    texto += "Em uso de fralda. "

if tem_lpp:
    texto += f"LPP ({lpp_estagio}) {lpp_descricao}. "

texto += f"{queixa_dor}."


# Exibição Final
st.subheader("📝 Texto Pronto para Copiar:")
st.text_area("Copie a evolução abaixo:", texto, height=250)