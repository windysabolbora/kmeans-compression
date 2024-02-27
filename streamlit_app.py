import streamlit as st

# Define the Streamlit app
def app():
    # Session state to track form progress
    if "current_form" not in st.session_state:
        st.session_state["current_form"] = "form1"
    
    # Form 1 for login
    if st.session_state["current_form"] == "form1":
        form1 = st.form("login")
        username = form1.text_input("Enter username")
        password = form1.text_input("Enter password", type="password")
        submit1 = form1.form_submit_button("Login")
    
        if submit1:
            # Validate credentials and update session state
            if username == "admin" and password == "secret":
                st.session_state["current_form"] = "form2"
            else:
                st.error("Invalid credentials")
    
    # Form 2 for product selection
    if st.session_state["current_form"] == "form2":
        form2 = st.form("product_selection")
        product = form2.selectbox("Choose your product", ["Product A", "Product B"])
        submit2 = form2.form_submit_button("Submit")
    
        if submit2:
            st.write(f"You selected {product}")
            
if __name__ == "__main__":
    app()
