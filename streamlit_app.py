import streamlit as st

# Define the Streamlit app
def app():
    st.title('Predicting Housing Cost using the SVM Regressor')
    # Session state to track form progress
    if "current_form" not in st.session_state:
        st.session_state["current_form"] = "form1"
    
    # Form 1 for introduction
    if st.session_state["current_form"] == "form1":
        form1 = st.form("intro")
        form1.subheader('About the Classifier')
        form1.write("""
            (c) 2024 Louie F. Cervantes
            Department of Computer Science
            College of Information and Communications Technology
            West Visayas state University
        """)
                    
        form1.write('Replace with the actual description')        
        #insert the rest of the information here

        submit1 = form1.form_submit_button("Start")
    
        if submit1:
            # Go to the next form
            st.session_state["current_form"] = "form2"
    
    # Form 2 for classifier training
    if st.session_state["current_form"] == "form2":        
        form2 = st.form("training")
        form2.subheader('Classifier Training')        
        # insert the rest of the code to train the classifier here        

        submit2 = form2.form_submit_button("Train")
    
        if submit2:
            st.session_state["current_form"] = "form3"

    # Form 3 for the price prediction using the trained model
    if st.session_state["current_form"] == "form3":                    
        form3 = st.form("prediction")

        form3.subheader('Prediction')
        form3.text('replace with the result of the prediction model.')

        n_clusters = form3.slider(
            label="Number of Clusters:",
            min_value=2,
            max_value=6,
            value=2,  # Initial value
        )

        predictbn = form3.form_submit_button("Predict")
        if predictbn:                    
            form3.text('User selected nclusters = ' + str(n_clusters))

        submit3 = form3.form_submit_button("Reset")
        if submit3:
            st.session_state["current_form"] = "form1"

            
if __name__ == "__main__":
    app()
