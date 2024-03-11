import streamlit as st
from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plt
import numpy as np
#import warnings; warnings.simplefilter('ignore')
from sklearn.cluster import MiniBatchKMeans

# Define the Streamlit app
def app():
    if "reset_app" not in st.session_state:
        st.session_state.reset_app = False

    st.title('Image Compression Using K-Means Clustering')
    # Use session state to track the current form
    if "current_form" not in st.session_state:
        st.session_state["current_form"] = 1    

    if "data" not in st.session_state:
        st.session_state.data = []

    if "image" not in st.session_state:
        st.session_state.image = []



    # Display the appropriate form based on the current form state
    if st.session_state["current_form"] == 1:
        display_form1()
    elif st.session_state["current_form"] == 2:
        display_form2()
    elif st.session_state["current_form"] == 3:
        display_form3()

def display_form1():
    st.session_state["current_form"] = 1
    form1 = st.form("intro")
    form1.subheader('K-Means Clustering Classifier')

    text = """Louie F. Cervantes, M. Eng. (Information Engineering) \n\n
    CCS 229 - Intelligent Systems
    Computer Science Department
    College of Information and Communications Technology
    West Visayas State University"""
    form1.text(text)
                
    text = """Importing the K-means Clustering Algorithm: 
    \nfrom sklearn.cluster import MiniBatchKMeans: 
    This line imports a specific implementation of K-means called 
    MiniBatchKMeans from the scikit-learn library. 
    This variant is often more efficient for large datasets.
    \nCreating a K-means Model:
    \nkmeans = MiniBatchKMeans(16): This line creates a K-means 
    model with 16 clusters. It means the algorithm will group 
    the image's pixel colors into 16 representative colors.
    \nFitting the Model to Image Data:\
    kmeans.fit(data): This line applies the K-means algorithm to 
    the image data, which is likely represented as an array of 
    pixel colors. The algorithm iteratively groups the colors 
    into clusters based on their similarity.
    \nRecoloring the Image with Cluster Centroids:
    new_colors = kmeans.cluster_centers_[kmeans.predict(data)]: 
    This line creates a new array of colors for the image. It does this by:
    kmeans.predict(data): Assigning each pixel to its closest cluster centroid.
    kmeans.cluster_centers_: Using the actual colors of those centroids as the new pixel colors.
    \nVisualizing the Compressed Image:
    plot_pixels(data, colors=new_colors, title='Reduced color space: 16 colors'): This line (presumably from a custom plotting function) displays the image using the reduced set of 16 colors. You'll likely see a slightly less detailed, but visually similar image.
    \nCreating a Recolored Image Array:
    flower_recolored = new_colors.reshape(flower.shape): This line 
    reshapes the array of new colors to match the original image's
    dimensions, creating a complete recolored image array that 
    can be saved or further processed.
    \nK-means reduces the number of colors in the image to 16, a form of compression.
    Visually, compression results in a less detailed but recognizable image.
    MiniBatchKMeans processes data in batches, making it efficient for large images."""
    form1.write(text)        

    submit1 = form1.form_submit_button("Start")

    if submit1:
        # Go to the next form        
        display_form2()

def display_form2():
    st.session_state["current_form"] = 2
    form2 = st.form("view_image")

    # Define the options for the radio button
    options = ["Image 1", "Image 2"]

    # Create the radio button and store the selected option
    selected_option = st.sidebar.radio("Select an image:", options)

    # Display a message based on the selected option (optional)
    if selected_option == "Image 1":
        st.session_state.image = load_sample_image('flower.jpg')
    else:
        st.session_state.image = load_sample_image('china.jpg')

    form2.subheader('Original Image')        
    
    fig, ax = plt.subplots(figsize=(6, 3))
    ax = plt.axes(xticks=[], yticks=[])
    ax.imshow(st.session_state.image)
    form2.pyplot(fig)

    data = st.session_state.image / 255.0
    data = data.reshape(427 * 640, 3)

    plot_pixels(form2, data, title= 'Input color space: 16 million possible colors')
    st.session_state['data'] = data
    
    submit2 = form2.form_submit_button("Compress")
    if submit2:        
        display_form3()

def display_form3():
    st.session_state["current_form"] = 3
    form3 = st.form("compressed")
    form3.subheader('Compressed Image')
    
    kmeans = MiniBatchKMeans(16)    
    data = st.session_state.data
    image = st.session_state.image
    kmeans.fit(data)
    new_colors = kmeans.cluster_centers_[kmeans.predict(data)]

    plot_pixels(form3, data, colors = new_colors, title='Reduced color space: 16 colors')
    flower_recolored = new_colors.reshape(image.shape)

    fig, ax = plt.subplots(1, 2, figsize=(16,6), subplot_kw=dict(xticks=[], yticks=[]))
    fig.subplots_adjust(wspace=0.05)
    ax[0].imshow(image)
    ax[0].set_title('Original Image', size = 16)
    ax[1].imshow(flower_recolored)
    ax[1].set_title('16-color image', size=16)
    form3.pyplot(fig)

    submit3 = form3.form_submit_button("Reset")
    if submit3:
        st.session_state.reset_app = True
        st.session_state.clear()

def plot_pixels(form, data, title, colors=None, N=1000):
    if colors is None:
        colors = data
        rng = np.random.RandomState(0)
        i = rng.permutation(data.shape[0])[:N]
        colors = colors[i]
        R, G, B = data[i].T
        fig, ax = plt.subplots(1, 2, figsize=(16, 6))
        ax[0].scatter(R, G, color=colors, marker='.')
        ax[0].set(xlabel='red', ylabel='green', xlim=(0, 1), ylim=(0, 1))
        ax[1].scatter(R, B, color=colors, marker='.')
        ax[1].set(xlabel='red', ylabel='blue', xlim=(0, 1), ylim=(0, 1))  
        fig.suptitle(title, size=20) 
        form.pyplot(fig)

if __name__ == "__main__":
    app()
