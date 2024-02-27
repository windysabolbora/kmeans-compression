import streamlit as st

# Define the Streamlit app
def app():
    # Session state to track form progress
    if "current_form" not in st.session_state:
        st.session_state["current_form"] = "form1"
    
    # Form 1 for login
    if st.session_state["current_form"] == "form1":
        form1 = st.form("intro")
        st.title('SVM Regressor')

        #insert the rest of the information here
        submit1 = form1.form_submit_button("Start")
    
        if submit1:
            # Go to the next form
            st.session_state["current_form"] = "form2"
    
    # Form 2 for classifier training
    if st.session_state["current_form"] == "form2":        
        form2 = st.form("training")
        st.title('Classifier Training')        
        # insert the rest of the code to train the classifier here        

        submit2 = form2.form_submit_button("Submit")
    
        if submit2:
            st.session_state["current_form"] = "form3"

    # Form 3 for the price prediction using the trained model
        form3 = st.form(""prediction)
        st.title('Prediction')        

        submit3 = form2.form_submit_button("Submit")

        if submit3:
            st.text('replace with the result of the prediction model.')
            st.session_state["current_form"] = "form3"

            
if __name__ == "__main__":
    app()
