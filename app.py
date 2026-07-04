import streamlit as st

# ---------------------------------
# 페이지 설정
# ---------------------------------
st.set_page_config(
    page_title="첫 웹사이트",
    page_icon="😊",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = "main"

# ---------------------------------
# CSS
# ---------------------------------

st.markdown("""
<style>

/* 전체 배경 */

.stApp{

background:linear-gradient(
135deg,
#CFEFFF 0%,
#B7E8FF 50%,
#DDF6FF 100%
);

height:100vh;

}


/* 카드 */

.card{

max-width:900px;

margin:120px auto;

padding:70px;

background:rgba(255,255,255,0.35);

backdrop-filter:blur(10px);

border-radius:30px;

box-shadow:0 10px 35px rgba(0,0,0,0.15);

animation:fadeIn 1.2s;

}


/* 제목 */

.title{

text-align:center;

font-size:clamp(30px,3vw,46px);

font-weight:bold;

color:#123A8F;

line-height:1.4;

margin-bottom:60px;

}


/* 결과 */

.message{

text-align:center;

font-size:clamp(30px,3vw,46px);

font-weight:bold;

color:#123A8F;

line-height:1.4;

margin-bottom:60px;

}


/* 버튼 */

div.stButton>button{

width:230px;

height:58px;

border-radius:15px;

border:2px solid #123A8F;

background:white;

color:#123A8F;

font-size:20px;

font-weight:bold;

box-shadow:0 5px 15px rgba(0,0,0,0.15);

transition:0.25s;

}


div.stButton>button:hover{

transform:translateY(-3px) scale(1.05);

background:#EAF7FF;

box-shadow:0 8px 20px rgba(0,0,0,0.2);

}


/* 등장 애니메이션 */

@keyframes fadeIn{

from{

opacity:0;

transform:translateY(25px);

}

to{

opacity:1;

transform:translateY(0);

}

}

</style>
""", unsafe_allow_html=True)

# ---------------------------------
# 메인 화면
# ---------------------------------

if st.session_state.page == "main":

    st.markdown("""
    <div class="card">

    <div class="title">
    😊 안녕하세요,<br>
    저는 당신의 첫 웹앱입니다 😊
    </div>

    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2,1,2])

    with c2:
        if st.button("나도 인사하기", use_container_width=True):
            st.session_state.page = "result"
            st.rerun()

# ---------------------------------
# 결과 화면
# ---------------------------------

else:

    st.balloons()

    st.markdown("""
    <div class="card">

    <div class="message">
    🎉 첫 웹페이지 제작을 축하해요! 🎉
    </div>

    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2,1,2])

    with c2:
        if st.button("돌아가기", use_container_width=True):
            st.session_state.page = "main"
            st.rerun()
