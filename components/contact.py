import streamlit as st

def render_contact(config):
    """Renders a compact, aesthetic, centered contact & feedback form."""
    st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)

    # Centered compact card layout
    c_left, c_center, c_right = st.columns([1, 2.2, 1])

    with c_center:
        with st.container(border=True):
            st.subheader("Contact & Feedback")
            st.caption("Leave feedback or send a message. This form responds immediately upon submission.")
            
            with st.form("contact_form", clear_on_submit=True):
                n_col, e_col = st.columns(2)
                with n_col:
                    sender_name = st.text_input("Name *", placeholder="Your Name")
                with e_col:
                    sender_email = st.text_input("Email *", placeholder="you@email.com")
                
                sender_msg = st.text_area("Message *", placeholder="Write your message here...", height=110)
                btn_submit = st.form_submit_button("Send Message", use_container_width=True)
                
                if btn_submit:
                    if not sender_name.strip() or not sender_email.strip() or not sender_msg.strip():
                        st.error("Please fill out all required fields.")
                    else:
                        st.session_state.feedback_list.append({"name": sender_name, "message": sender_msg})
                        st.success(f"Thank you, {sender_name}! Your message has been received.")
