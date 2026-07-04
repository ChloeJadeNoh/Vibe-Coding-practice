import streamlit as st
import time

st.set_page_config(
    page_title="첫 웹사이트",
    page_icon="🎁",
    layout="centered"
)

if "opened" not in st.session_state:
    st.session_state.opened = False

st.markdown("""
<style>

.stApp{
    background:#BFEFFF;
}

h1{
    text-align:center;
    color:#123A8F;
}

.result{
    text-align:center;
    color:#123A8F;
    font-size:38px;
    font-weight:bold;
    margin-top:20px;
}

.center{
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
}

/* 선물상자 */

.gift{
    width:220px;
    height:170px;
    position:relative;
    margin-top:30px;
}

.box{
    width:220px;
    height:130px;
    background:#FFD93D;
    position:absolute;
    bottom:0;
    border-radius:10px;
}

/* 뚜껑 */

.lid{
    width:240px;
    height:35px;
    background:#FFD93D;
    position:absolute;
    left:-10px;
    top:35px;
    border-radius:10px;
    transform-origin:left bottom;
}

/* 리본 세로 */

.ribbon-v{
    position:absolute;
    width:24px;
    height:170px;
    background:#FF69B4;
    left:98px;
    z-index:3;
}

/* 리본 가로 */

.ribbon-h{
    position:absolute;
    width:220px;
    height:24px;
    background:#FF69B4;
    top:85px;
    z-index:3;
}

/* 리본 매듭 */

.bow{
    width:42px;
    height:42px;
    border-radius:50%;
    background:#FF69B4;
    position:absolute;
    top:15px;
    left:89px;
    z-index:5;
}

.bow:before{
    content:"";
    width:32px;
    height:18px;
    border:6px solid #FF69B4;
    border-radius:50%;
    position:absolute;
    left:-28px;
    top:6px;
}

.bow:after{
    content:"";
    width:32px;
    height:18px;
    border:6px solid #FF69B4;
    border-radius:50%;
    position:absolute;
    right:-28px;
    top:6px;
}

/* 열림 애니메이션 */

.open .lid{
    animation:openGift 1s forwards;
}

@keyframes openGift{

0%{
transform:rotate(0deg);
}

100%{
transform:rotate(-45deg) translate(-30px,-40px);
}

}

div.stButton>button{
    display:block;
    margin:auto;
    margin-top:35px;
    font-size:20px;
    color:#123A8F;
    border-radius:10px;
    padding:10px 30px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------

if not st.session_state.opened:

    st.markdown(
        "<h1>😊 안녕하세요, 저는 당신의 첫 웹사이트입니다 😊</h1>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="center">

        <div class="gift">

            <div class="lid"></div>

            <div class="box"></div>

            <div class="ribbon-v"></div>

            <div class="ribbon-h"></div>

            <div class="bow"></div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button("나도 인사하기"):
        st.session_state.opened=True
        st.rerun()

# -------------------------------

else:

    st.balloons()

    st.markdown(
        """
        <div class="center">

            <div class="gift open">

                <div class="lid"></div>

                <div class="box"></div>

                <div class="ribbon-v"></div>

                <div class="ribbon-h"></div>

                <div class="bow"></div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(1)

    st.markdown(
        "<div class='result'>🎉 첫 웹페이지 제작을 축하해요! 🎉</div>",
        unsafe_allow_html=True
    )

    if st.button("돌아가기"):
        st.session_state.opened=False
        st.rerun()
