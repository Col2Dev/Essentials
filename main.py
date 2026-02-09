import streamlit as st
import json

# LOAD JSON FILE
with open("kjv.json", "r", encoding="utf-8") as f:
    bible = json.load(f)

#PAGE CONFIGURATION
st.set_page_config(
    page_title="Apostolic Word: Bible",
    page_icon=None,
    layout="wide"
)


def main():

    # Sidebar
    with st.sidebar:
        st.title("Apostolic Word")
        st.divider()
        st.title("Bible" )
        st.divider()
    
        books = list(bible.keys())
        book = st.selectbox("Book:", books)

        st.divider()

        chapters = list(bible[book].keys())
        chapter = st.selectbox("Chapter:", chapters)

    # ---------------- Layout ----------------
    col1, col2, col3 = st.columns([3, 6,3])

    # Bible Column
    with col1:
        pass

    # Teaching Column
    with col2:
        st.divider()
        st.markdown("## Bible")
        st.divider()

        verses = bible[book][chapter]
        
        st.markdown(f"**{book} {chapter}**")
        for verse_num, verse_text in verses.items():
            
            st.write(verse_num + " " + verse_text)
            st.write("")
            
    with col3: 
        pass
#RUN APP
if __name__ == "__main__":
    main()

