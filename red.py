import streamlit as st

st.set_page_config(page_title=" Envelope ", page_icon="😌")

st.markdown(
    """
    <style>
    .title {
        text-align:center;
        color:#ff1493;
        font-size:40px;
        font-weight:bold;
    }
    .letter {
        background-color:#fffaf0;
        padding:20px;
        border-radius:15px;
        border:2px solid hotpink;
        text-align:center;
        color:#d1006c;
        font-size:22px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title"> important msg 🙈</p>', unsafe_allow_html=True)

if st.button(" Open Envelope "):
    st.markdown(
        """
        <div class="letter">
            <h2> kuchu puchu  </h2>
            <p>
                143  !! .<br>
                ahu ahu 🙈
                 umm hmm 😌
            </p>
            <h1></h1>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("Click the envelope button to open your special message 💌")