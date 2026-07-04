import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="첫 웹사이트",
    page_icon="😊",
    layout="wide"
)

# -----------------------------
# 상태 저장
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "main"

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

/* 전체 배경 */
.stApp{
    background: linear-gradient(
        180deg,
        #CFEFFF 0%,
        #B8E6FF 100%
    );
}

/* Streamlit 기본 여백 제거 */
.block-container{
    padding-top:6rem;
}

/* 제목 */
.title{
    text-align:center;
    color:#123A8F;

    font-size:clamp(34px,4vw,54px);
    font-weight:700;

    line-height:1.25;

    margin-top:80px;
    margin-bottom:60px;
}

/* 결과 문구 */
.message{
    text-align:center;
    color:#123A8F;

    font-size:clamp(34px,4vw,54px);
    font-weight:700;

    line-height:1.3;

    margin-top:80px;
    margin-bottom:60px;
}

/* 버튼 */
div.stButton > button{

    width:240px;
    height:58px;

    border-radius:15px;

    border:2px solid #123A8F;

    background:white;

    color:#123A8F;

    font-size:20px;

    font-weight:600;

    transition:0.25s;

    box-shadow:0 6px 16px rgba(0,0,0,.15);

}

div.stButton > button:hover{

    background:#EDF8FF;

    transform:translateY(-2px);

    box-shadow:0 10px 24px rgba(0,0,0,.18);

}

/* 버튼 가운데 정렬 */
.center-button{
    display:flex;
    justify-content:center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 메인 화면
# -----------------------------
if st.session_state.page == "main":

    st.markdown("""
    <div class="title">
        😊 안녕하세요 😊<br>
        저는 당신의 첫 웹앱입니다
    </div>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([4,2,4])

    with center:
        if st.button("나도 인사하기", use_container_width=True):
            st.session_state.page = "result"
            st.rerun()

# -----------------------------
# 결과 화면
# -----------------------------
else:

    st.balloons()

    st.markdown("""
    <div class="message">
        🎉<br>
        첫 웹페이지 제작을 축하해요!
    </div>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([4,2,4])

    with center:
        if st.button("돌아가기", use_container_width=True):
            st.session_state.page = "main"
            st.rerun()
