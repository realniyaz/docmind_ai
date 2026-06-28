import streamlit as st


def load_css():

    st.markdown("""
<style>

/*==============================================================
GOOGLE FONT
==============================================================*/

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');


/*==============================================================
ROOT VARIABLES
==============================================================*/

:root{

--primary:#2563EB;
--primary-hover:#1D4ED8;
--primary-light:#DBEAFE;

--success:#22C55E;
--warning:#F59E0B;
--danger:#EF4444;

--background:#F5F7FB;
--surface:#FFFFFF;
--surface-light:#F8FAFC;

--text:#111827;
--text-light:#6B7280;

--border:#E5E7EB;

--radius-sm:10px;
--radius:18px;
--radius-lg:26px;

--shadow-sm:
0 2px 8px rgba(0,0,0,.04);

--shadow:
0 8px 25px rgba(0,0,0,.06);

--shadow-lg:
0 20px 45px rgba(0,0,0,.08);

}


/*==============================================================
GLOBAL
==============================================================*/

html,
body,
[class*="css"]{

font-family:'Inter',sans-serif;

color:var(--text);

scroll-behavior:smooth;

}

.stApp{

background:var(--background);

}


/*==============================================================
REMOVE STREAMLIT BRANDING
==============================================================*/

#MainMenu{

visibility:hidden;

}

footer{

visibility:hidden;

}

header{

visibility:hidden;

}


/*==============================================================
PAGE
==============================================================*/

.block-container{

padding-top:2rem;

padding-bottom:2rem;

padding-left:3rem;

padding-right:3rem;

max-width:1600px;

}


/*==============================================================
SIDEBAR
==============================================================*/

[data-testid="stSidebar"]{

background:#FFFFFF;

border-right:1px solid var(--border);

padding-top:20px;

}

[data-testid="stSidebar"] h1{

font-size:30px;

font-weight:800;

margin-bottom:4px;

color:var(--text);

}

[data-testid="stSidebar"] h2{

font-size:22px;

font-weight:700;

color:var(--text);

}

[data-testid="stSidebar"] h3{

font-size:17px;

font-weight:700;

margin-bottom:12px;

color:var(--text);

}

[data-testid="stSidebar"] .stDivider{

margin-top:20px;

margin-bottom:20px;

}


/*==============================================================
BUTTONS
==============================================================*/

.stButton>button{

width:100%;

height:48px;

border:none;

border-radius:14px;

background:var(--primary);

color:white;

font-weight:600;

font-size:15px;

transition:.3s;

box-shadow:var(--shadow-sm);

}

.stButton>button:hover{

background:var(--primary-hover);

transform:translateY(-2px);

box-shadow:var(--shadow);

}

.stButton>button:active{

transform:scale(.98);

}


/*==============================================================
TEXT INPUT
==============================================================*/

.stTextInput input{

border-radius:14px;

border:1px solid var(--border);

padding:12px;

}


/*==============================================================
CHAT INPUT
==============================================================*/

[data-testid="stChatInput"]{

background:white;

border-radius:18px;

padding:8px;

box-shadow:var(--shadow);

border:1px solid var(--border);

}


/*==============================================================
FILE UPLOADER
==============================================================*/

[data-testid="stFileUploader"]{

background:transparent;

border:none;

padding:0;

}

[data-testid="stFileUploaderDropzone"]{

background:white;

border:2px dashed #CBD5E1;

border-radius:18px;

padding:25px;

transition:.3s;

}

[data-testid="stFileUploaderDropzone"]:hover{

border-color:var(--primary);

background:#F8FAFF;

box-shadow:var(--shadow);

}


/*==============================================================
CARDS
==============================================================*/

.card{

background:white;

padding:24px;

border-radius:20px;

border:1px solid var(--border);

box-shadow:var(--shadow);

margin-bottom:20px;

transition:.3s;

}

.card:hover{

transform:translateY(-3px);

box-shadow:var(--shadow-lg);

}


/*==============================================================
HEADINGS
==============================================================*/

h1{

font-size:42px;

font-weight:800;

color:var(--text);

}

h2{

font-size:30px;

font-weight:700;

color:var(--text);

}

h3{

font-size:22px;

font-weight:700;

color:var(--text);

margin-bottom:10px;

}


/*==============================================================
TEXT
==============================================================*/

p{

font-size:15px;

line-height:1.8;

color:var(--text-light);

}

small{

color:var(--text-light);

}


/*==============================================================
LINKS
==============================================================*/

a{

color:var(--primary);

text-decoration:none;

transition:.3s;

}

a:hover{

color:var(--primary-hover);

}


/*==============================================================
METRICS
==============================================================*/

[data-testid="metric-container"]{

background:white;

padding:20px;

border-radius:18px;

border:1px solid var(--border);

box-shadow:var(--shadow-sm);

}


/*==============================================================
DIVIDER
==============================================================*/

hr{

border:none;

height:1px;

background:var(--border);

margin:20px 0;

}


/*==============================================================
SUCCESS
==============================================================*/

.stSuccess{

border-radius:14px;

}


/*==============================================================
WARNING
==============================================================*/

.stWarning{

border-radius:14px;

}


/*==============================================================
INFO
==============================================================*/

.stInfo{

border-radius:14px;

}


/*==============================================================
ERROR
==============================================================*/

.stError{

border-radius:14px;

}

/*==============================================================
HERO
==============================================================*/

.hero{

display:flex;

justify-content:space-between;

align-items:center;

gap:50px;

background:linear-gradient(135deg,#FFFFFF,#F8FAFC);

border:1px solid var(--border);

border-radius:26px;

padding:35px 42px;

box-shadow:var(--shadow);

margin-bottom:30px;

overflow:hidden;

position:relative;

}

.hero::before{

content:"";

position:absolute;

right:-80px;

top:-80px;

width:220px;

height:220px;

background:rgba(37,99,235,.05);

border-radius:50%;

}

.hero-left{

flex:1;

z-index:2;

}

.hero-right{

width:260px;

z-index:2;

}

.hero-title{

font-size:38px;

font-weight:800;

margin-bottom:12px;

color:var(--text);

line-height:1.1;

}

.hero-sub{

font-size:16px;

line-height:1.8;

color:var(--text-light);

max-width:700px;

margin-bottom:22px;

}

.hero-tags{

display:flex;

flex-wrap:wrap;

gap:10px;

}

.hero-chip{

padding:8px 16px;

background:#EFF6FF;

border:1px solid #DBEAFE;

border-radius:999px;

font-size:13px;

font-weight:600;

color:#2563EB;

transition:.25s;

}

.hero-chip:hover{

background:#DBEAFE;

transform:translateY(-2px);

}

.hero-mini{

background:#F8FAFC;

border:1px solid var(--border);

border-radius:18px;

padding:18px;

}

.hero-mini-item{

padding:10px 0;

font-size:14px;

color:#4B5563;

border-bottom:1px solid #ECECEC;

}

.hero-mini-item:last-child{

border:none;

}


/*==============================================================
STATUS PILL
==============================================================*/

.status-pill{

display:inline-flex;

align-items:center;

justify-content:center;

padding:10px 18px;

background:#DCFCE7;

border:1px solid #BBF7D0;

border-radius:999px;

font-size:13px;

font-weight:700;

color:#15803D;

margin-bottom:18px;

}


/*==============================================================
METRIC CARD
==============================================================*/

.metric-card{

background:white;

border:1px solid var(--border);

border-radius:20px;

padding:24px;

text-align:center;

box-shadow:var(--shadow);

transition:.3s;

min-height:170px;

display:flex;

flex-direction:column;

justify-content:center;

}

.metric-card:hover{

transform:translateY(-4px);

box-shadow:var(--shadow-lg);

}

.metric-icon{

font-size:34px;

margin-bottom:14px;

}

.metric-value{

font-size:34px;

font-weight:800;

color:var(--text);

margin-bottom:8px;

}

.metric-title{

font-size:14px;

font-weight:500;

color:#6B7280;

}


/*==============================================================
KNOWLEDGE BASE CARD
==============================================================*/

.pdf-card{

background:white;

border:1px solid var(--border);

border-radius:22px;

padding:25px;

box-shadow:var(--shadow);

}

.pdf-header{

display:flex;

justify-content:space-between;

align-items:center;

margin-bottom:20px;

}

.pdf-title{

font-size:22px;

font-weight:700;

color:var(--text);

}

.pdf-file{

background:#F8FAFC;

border:1px solid var(--border);

border-radius:16px;

padding:18px;

margin-bottom:22px;

}

.pdf-file-name{

font-size:16px;

font-weight:700;

color:var(--text);

margin-bottom:6px;

word-break:break-word;

}

.pdf-file-status{

font-size:13px;

color:#6B7280;

}

.pdf-stats{

display:grid;

grid-template-columns:1fr 1fr;

gap:16px;

}

.pdf-stat{

background:#F8FAFC;

border-radius:16px;

padding:18px;

text-align:center;

transition:.25s;

}

.pdf-stat:hover{

background:#EFF6FF;

}

.pdf-stat-icon{

font-size:24px;

margin-bottom:8px;

}

.pdf-stat-value{

font-size:28px;

font-weight:700;

color:var(--text);

margin-bottom:6px;

}

.pdf-stat-title{

font-size:13px;

color:#6B7280;

}


/*==============================================================
INFO CARD
==============================================================*/

.info-card{

background:white;

border-radius:22px;

padding:30px;

border:1px solid var(--border);

box-shadow:var(--shadow);

}

.info-title{

font-size:26px;

font-weight:700;

margin-bottom:16px;

color:var(--text);

}

.info-body{

line-height:1.9;

font-size:15px;

color:#6B7280;

}


/*==============================================================
SOURCE CARD
==============================================================*/

.source-card{

background:#F8FAFC;

border-left:5px solid var(--primary);

border-radius:16px;

padding:16px;

margin-bottom:12px;

transition:.25s;

}

.source-card:hover{

background:#EFF6FF;

}

.source-title{

font-size:15px;

font-weight:700;

color:var(--text);

margin-bottom:6px;

}

.source-page{

font-size:13px;

color:#6B7280;

}
                
/*==============================================================
CHAT CONTAINER
==============================================================*/

.chat-container{

background:#FFFFFF;

border:1px solid var(--border);

border-radius:24px;

padding:25px;

box-shadow:var(--shadow);

min-height:700px;

}


/*==============================================================
CHAT HEADER
==============================================================*/

.chat-header{

display:flex;

justify-content:space-between;

align-items:center;

margin-bottom:20px;

padding-bottom:18px;

border-bottom:1px solid var(--border);

}

.chat-title{

font-size:24px;

font-weight:700;

color:var(--text);

}

.chat-sub{

font-size:14px;

color:var(--text-light);

}


/*==============================================================
CHAT MESSAGE
==============================================================*/

[data-testid="stChatMessage"]{

background:#FFFFFF;

border-radius:18px;

border:1px solid var(--border);

padding:18px;

margin-bottom:16px;

box-shadow:var(--shadow-sm);

transition:.25s;

}

[data-testid="stChatMessage"]:hover{

box-shadow:var(--shadow);

transform:translateY(-2px);

}


/*==============================================================
USER MESSAGE
==============================================================*/

.user-message{

background:#2563EB;

color:white;

padding:16px 18px;

border-radius:18px 18px 6px 18px;

margin-left:70px;

margin-bottom:15px;

box-shadow:var(--shadow);

}


/*==============================================================
ASSISTANT MESSAGE
==============================================================*/

.assistant-message{

background:#FFFFFF;

border:1px solid var(--border);

padding:18px;

border-radius:18px 18px 18px 6px;

margin-right:70px;

margin-bottom:18px;

box-shadow:var(--shadow-sm);

}


/*==============================================================
CHAT INPUT
==============================================================*/

[data-testid="stChatInput"]{

background:#FFFFFF;

border:1px solid var(--border);

border-radius:18px;

padding:8px;

box-shadow:var(--shadow);

}

[data-testid="stChatInput"] textarea{

font-size:15px;

}


/*==============================================================
SOURCE CARD
==============================================================*/

.source-card{

background:#F8FAFC;

border:1px solid var(--border);

border-left:5px solid var(--primary);

border-radius:14px;

padding:16px;

margin-bottom:12px;

transition:.25s;

}

.source-card:hover{

background:#EFF6FF;

}

.source-title{

font-size:15px;

font-weight:700;

margin-bottom:6px;

color:var(--text);

}

.source-page{

font-size:13px;

color:var(--text-light);

}


/*==============================================================
UPLOAD COMPONENT
==============================================================*/

.upload-container{

background:#FFFFFF;

border:2px dashed #CBD5E1;

border-radius:22px;

padding:30px;

text-align:center;

transition:.35s;

margin-bottom:18px;

}

.upload-container:hover{

background:#F8FAFF;

border-color:#2563EB;

transform:translateY(-2px);

box-shadow:var(--shadow);

}

.upload-icon{

font-size:60px;

margin-bottom:16px;

animation:floating 3s ease-in-out infinite;

}

.upload-title{

font-size:22px;

font-weight:700;

color:var(--text);

margin-bottom:10px;

}

.upload-description{

font-size:14px;

line-height:1.8;

color:#6B7280;

margin-bottom:18px;

}

.upload-footer{

display:flex;

justify-content:space-between;

font-size:13px;

color:#6B7280;

margin-top:12px;

}


/*==============================================================
FILE UPLOADER
==============================================================*/

[data-testid="stFileUploader"]{

background:transparent;

border:none;

padding-top:10px;

}

[data-testid="stFileUploaderDropzone"]{

background:#FFFFFF;

border:2px dashed #D1D5DB;

border-radius:18px;

padding:24px;

transition:.3s;

}

[data-testid="stFileUploaderDropzone"]:hover{

border-color:#2563EB;

background:#F8FAFF;

}

[data-testid="stFileUploaderDropzone"] small{

display:none;

}


/*==============================================================
EXPANDER
==============================================================*/

.streamlit-expanderHeader{

font-size:15px;

font-weight:600;

color:var(--text);

}

.streamlit-expanderContent{

padding-top:15px;

}


/*==============================================================
STATUS
==============================================================*/

.status-success{

background:#DCFCE7;

color:#15803D;

padding:8px 16px;

border-radius:999px;

font-size:13px;

font-weight:700;

display:inline-block;

}

.status-warning{

background:#FEF3C7;

color:#B45309;

padding:8px 16px;

border-radius:999px;

font-size:13px;

font-weight:700;

display:inline-block;

}


/*==============================================================
EMPTY STATE
==============================================================*/

.empty-chat{

text-align:center;

padding:80px 30px;

}

.empty-chat-icon{

font-size:70px;

margin-bottom:20px;

}

.empty-chat-title{

font-size:28px;

font-weight:700;

margin-bottom:12px;

}

.empty-chat-sub{

font-size:15px;

line-height:1.8;

color:#6B7280;

max-width:500px;

margin:auto;

}


/*==============================================================
LOADING
==============================================================*/

@keyframes pulse{

0%{

opacity:.4;

}

50%{

opacity:1;

}

100%{

opacity:.4;

}

}

.loading{

animation:pulse 1.5s infinite;

}


/*==============================================================
FLOATING
==============================================================*/

@keyframes floating{

0%{

transform:translateY(0px);

}

50%{

transform:translateY(-4px);

}

100%{

transform:translateY(0px);

}

}
                
/*==============================================================
SCROLLBAR
==============================================================*/

::-webkit-scrollbar{

width:10px;

height:10px;

}

::-webkit-scrollbar-track{

background:#F3F4F6;

border-radius:20px;

}

::-webkit-scrollbar-thumb{

background:#CBD5E1;

border-radius:20px;

transition:.3s;

}

::-webkit-scrollbar-thumb:hover{

background:#94A3B8;

}


/*==============================================================
TABLES
==============================================================*/

table{

width:100%;

border-collapse:collapse;

background:white;

border-radius:18px;

overflow:hidden;

box-shadow:var(--shadow);

}

thead{

background:#F8FAFC;

}

th{

padding:16px;

text-align:left;

font-weight:700;

color:#374151;

}

td{

padding:16px;

border-top:1px solid #F1F5F9;

color:#6B7280;

}


/*==============================================================
CODE
==============================================================*/

pre{

background:#111827;

border-radius:16px;

padding:18px;

overflow-x:auto;

}

code{

background:#EEF2FF;

padding:4px 8px;

border-radius:8px;

font-size:13px;

color:#1E3A8A;

}


/*==============================================================
BLOCKQUOTE
==============================================================*/

blockquote{

margin:20px 0;

padding:18px;

border-left:5px solid var(--primary);

background:#F8FAFC;

border-radius:12px;

color:#4B5563;

}


/*==============================================================
IMAGES
==============================================================*/

img{

border-radius:16px;

max-width:100%;

}


/*==============================================================
SELECTION
==============================================================*/

::selection{

background:#DBEAFE;

color:#111827;

}


/*==============================================================
ANIMATIONS
==============================================================*/

.hero,
.card,
.metric-card,
.pdf-card,
.upload-container,
.source-card,
.chat-container{

animation:fadeUp .45s ease;

}

@keyframes fadeUp{

0%{

opacity:0;

transform:translateY(18px);

}

100%{

opacity:1;

transform:translateY(0);

}

}


/*==============================================================
HOVER EFFECTS
==============================================================*/

.card:hover,
.metric-card:hover,
.pdf-card:hover,
.chat-container:hover{

transform:translateY(-4px);

box-shadow:var(--shadow-lg);

}

.hero-chip:hover{

transform:translateY(-2px);

}

.status-pill:hover{

transform:scale(1.03);

}


/*==============================================================
TRANSITIONS
==============================================================*/

*{

transition:

background .25s ease,

color .25s ease,

border .25s ease,

box-shadow .25s ease,

transform .25s ease;

}


/*==============================================================
UTILITY CLASSES
==============================================================*/

.text-center{

text-align:center;

}

.text-right{

text-align:right;

}

.mt-10{

margin-top:10px;

}

.mt-20{

margin-top:20px;

}

.mt-30{

margin-top:30px;

}

.mb-10{

margin-bottom:10px;

}

.mb-20{

margin-bottom:20px;

}

.mb-30{

margin-bottom:30px;

}

.flex{

display:flex;

}

.flex-between{

display:flex;

justify-content:space-between;

align-items:center;

}

.flex-center{

display:flex;

justify-content:center;

align-items:center;

}

.gap-10{

gap:10px;

}

.gap-20{

gap:20px;

}

.round{

border-radius:999px;

}


/*==============================================================
RESPONSIVE
==============================================================*/

@media (max-width:1200px){

.block-container{

padding-left:2rem;

padding-right:2rem;

}

.hero{

flex-direction:column;

align-items:flex-start;

}

.hero-right{

width:100%;

margin-top:25px;

}

.hero-title{

font-size:32px;

}

.metric-card{

min-height:150px;

}

}

@media (max-width:900px){

.block-container{

padding:1.5rem;

}

.hero{

padding:28px;

}

.hero-title{

font-size:28px;

}

.hero-sub{

font-size:15px;

}

.hero-tags{

gap:8px;

}

.pdf-stats{

grid-template-columns:1fr;

}

.chat-container{

min-height:500px;

}

.user-message{

margin-left:0;

}

.assistant-message{

margin-right:0;

}

}

@media (max-width:640px){

.block-container{

padding:1rem;

}

.hero{

padding:22px;

border-radius:18px;

}

.hero-title{

font-size:24px;

}

.hero-sub{

font-size:14px;

}

.hero-chip{

font-size:12px;

padding:6px 12px;

}

.metric-card{

padding:18px;

}

.card{

padding:18px;

}

.pdf-card{

padding:18px;

}

.upload-container{

padding:22px;

}

.upload-title{

font-size:18px;

}

.chat-header{

flex-direction:column;

align-items:flex-start;

gap:10px;

}

}


/*==============================================================
PRINT
==============================================================*/

@media print{

body{

background:white;

}

.stSidebar{

display:none;

}

.chat-input{

display:none;

}

}


/*==============================================================
END OF STYLESHEET
==============================================================*/
</style>
""", unsafe_allow_html=True)