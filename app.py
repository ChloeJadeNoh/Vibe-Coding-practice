import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="첫 웹사이트",
    page_icon="😊",
    layout="centered"
)

# 상태 저장
if "page" not in st.session_state:
    st.session_state.page = "main"

# CSS
st.markdown("""
<style>
.stApp{
    background-color:#BFEFFF;
}

.title{
    text-align:center;
    color:#123A8F;
    font-size:42px;
    font-weight:bold;
    margin-top:180px;
}

.message{
    text-align:center;
    color:#123A8F;
    font-size:40px;
    font-weight:bold;
    margin-top:180px;
}

div.stButton{
    text-align:center;
}

div.stButton > button{
    margin-top:30px;
    background:white;
    color:#123A8F;
    border-radius:10px;
    font-size:20px;
    padding:10px 28px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- 메인 화면 ----------------

if st.session_state.page == "main":

    st.markdown(
        """
        <div class="title">
            😊 안녕하세요, 저는 당신의 첫 웹사이트입니다 😊
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("나도 인사하기"):
        st.session_state.page = "result"
        st.rerun()

# ---------------- 결과 화면 ----------------

else:

    # 폭죽 효과
    st.balloons()

    st.markdown(
        """
        <div class="message">
            🎉 첫 웹페이지 제작을 축하해요! 🎉
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("돌아가기"):
        st.session_state.page = "main"
        st.rerun()
