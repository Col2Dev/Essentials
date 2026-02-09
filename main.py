import streamlit as st
import json

# LOAD JSON FILE
with open("kjv.json", "r", encoding="utf-8") as f:
    bible = json.load(f)

#PAGE CONFIGURATION
st.set_page_config(
    page_title="Nebula",
    page_icon=None,
    layout="wide"
)


def main():

    # Sidebar
    with st.sidebar:
        st.title("Apostolic Word")
        st.divider()

        options = ["Repent", "Baptism", "Holy Ghost"]

        selection = st.pills(
            "Current Page:",
            options,
            default="Repent"
        )

        st.divider()

        books = list(bible.keys())
        book = st.selectbox("Book:", books)

        st.divider()

        chapters = list(bible[book].keys())
        chapter = st.selectbox("Chapter:", chapters)

    # ---------------- Layout ----------------
    col1, col2 = st.columns([1.5, 1.5])

    # Bible Column
    with col1:
        st.divider()
        st.markdown("## Bible")
        st.divider()

        verses = bible[book][chapter]
        
        st.markdown(f"**{book} {chapter}**")
        for verse_num, verse_text in verses.items():
            
            st.write(verse_num + " " + verse_text)
            st.write("")

    # Teaching Column
    with col2:
        if selection == "Repent":
            st.divider()
            st.markdown("## Acts 2:38")
            st.divider()
            st.markdown("""
**- "Repent** and be **baptized** every one of you in the NAME  
of Jesus Christ for the remission of sins,  
and ye shall receive the gift of the Holy Ghost"

---

## Repentance

Repentance is the act of acknowledging sins, asking for forgiveness, and turning from them.

It is a state of the soul that is granted by God.

It is a death of the old man.
""")
            st.divider()

        elif selection == "Baptism":
            st.divider()
            st.markdown("## Baptism")
            st.divider()
            st.markdown("""
Baptism is a symbol of burial.

You bury the old man which washes away your past self, and makes you a new man.

It is a remission of sins.
""")
            st.divider()

        elif selection == "Holy Ghost":
            st.divider()
            st.markdown("## Holy Ghost")
            st.divider()
            st.markdown("""
The Gift of the Holy Ghost is the Lord's Spirit coming down from heaven and living inside you.

You will know He is living in you when you begin to speak in an unknown language according to Acts 2:4.

The Lord's Spirit gives power over:

• Flesh  
• Devils  
• And more
""")
            st.divider()

#RUN APP
if __name__ == "__main__":
    main()

