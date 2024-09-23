# Displaying 2 texts in a window

import streamlit as st

def main():
    st.title("Two Column Layout in Streamlit")
    # Inserting a horizontal line
    st.markdown("---") 

    col1, col2 = st.columns(2) # evenly split the screen into two columns

    with col1:
        st.header("Column 1")
        st.write("Here's some text in column 1. You can add any elements you want here like text, charts, images, etc.")

    with col2:
        st.header("Column 2")
        st.write("And here's some text in column 2. Similarly, this column can have its own independent content.")
    
    # Inserting a horizontal line
    st.markdown("---") 
    st.write("Content outside the columns, back to full width.")

    # col_1, col_2 = st.columns(2) # evenly split the screen into two columns

    # with col_1:
    #     st.header("Column 1")
    #     st.markdown("""
    #                 ```python
    #                 Here's some text in column 1. You can add any elements you want here like text, charts, images, etc.
    #                 ```
    #                 """)

    # with col_2:
    #     st.header("Column 2")
    #     st.markdown("""
    #                 ```python
    #                 And here's some text in column 2. Similarly, this column can have its own independent content.
    #                 ```
    #                 """)

    col1_, col2_, col3_ = st.columns([2, 0.1, 2]) # 2:0.1:2 ratio

    with col1_:
        st.header("Answer A")
        st.write("This is the left column. You can add text, widgets, or other content here.")

    with col2_:
        # Using Markdown to vertically align the pipe character as a line
        st.markdown("""
        |  
        |  
        |  
        |  
        |  
        |  
        |  
        |  
        |  
        """, unsafe_allow_html=False)

    with col3_:
        st.header("Answer B")
        st.write("This is the right column. Similarly, you can add any type of content here.")

    
    st.title("Streamlit Text Formatting")

    st.header("Header Example")
    st.subheader("Subheader Example")

    st.markdown("""
    - **Bold Text**
    - *Italic Text*
    - `Inline Code`
    
    1. List item 1
    2. List item 2

    [Streamlit](https://streamlit.io)

    ```python
    # Code block example
    print("Hello, Streamlit!")
    ```
    """)

if __name__ == "__main__":
    main()