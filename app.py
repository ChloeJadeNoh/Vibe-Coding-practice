import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="첫 웹사이트",
    page_icon="😊",
    layout="centered"
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

.stApp{
    background-color:#BFEFFF;
}

/* 제목 */
.title{
    text-align:center;
    color:#123A8F;
    font-size:42px;
    font-weight:bold;
    margin-top:180px;
}

/* 축하 문구 */
.message{
    text-align:center;
    color:#123A8F;
    font-size:42px;
    font-weight:bold;
    margin-top:170px;
}

/* 버튼 전체 가운데 정렬 */
div.stButton{
    display:flex;
    justify-content:center;
    margin-top:35px;
}

/* 버튼 꾸미기 */
div.stButton > button{
    background:white;
    color:#123A8F;
    font-size:20px;
    border-radius:12px;
    padding:10px 30px;
    border:2px solid #123A8F;
}

div.stButton > button:hover{
    background:#EAF7FF;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 메인 화면
# -----------------------------
if st.session_state.page == "main":

    st.markdown("""
        <div class="title">
            😊 안녕하세요, 저는 당신의 첫 웹사이트입니다 😊
        </div>
    """, unsafe_allow_html=True)

    if st.button("나도 인사하기"):
        st.session_state.page = "result"
        st.rerun()

# -----------------------------
# 결과 화면
# -----------------------------
else:

    # 폭죽 효과
    st.balloons()

    st.markdown("""
        <div class="message">
            🎉 첫 웹페이지 제작을 축하해요! 🎉
        </div>
    """, unsafe_allow_html=True)

    if st.button("돌아가기"):
        st.session_state.page = "main"
        st.rerun()
