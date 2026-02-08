import streamlit as st

# Must be first Streamlit command
st.set_page_config(
    page_title="Nebula",
    page_icon="🌌",
    layout="wide"
)

def main():

    # ---------------- Sidebar ----------------
    with st.sidebar:
        st.title("🌌 Nebula")
        st.divider()

        options = ["Repent", "Baptism", "Holy Ghost"]

        selection = st.pills(
            "Current Page:",
            options,
            default="Repent"
        )

    # ------------- Main Content -------------
    with st.container():

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:

            # ---------------- REPENT PAGE ----------------
            if selection == "Repent":

                st.markdown("""
## Acts 2:38

**- "Repent** and be **baptized** every one of you in the *NAME*  of **Jesus Christ** for the remission of sins, and ye shall receive the  **gift of the Holy Ghost"**

---

## Repentance

Repentance is the act of acknowledging sins, asking for forgiveness, and turning from them.

It is a state of the soul that is granted by God, and you simply cannot repent by just saying sorry and then further continuing in sin.

It is a death of the old man.
""")

            # ---------------- BAPTISM PAGE ----------------
            elif selection == "Baptism":

                st.markdown("""
## Baptism

Baptism is a symbol of burial

You bury the old man which washes away your past self, and makes you a new man.
You start with a new slate and your sins are no longer on your record. This means God does not remember them anymore.

It is a remission of sins.
""")

            # ---------------- HOLY GHOST PAGE ----------------
            elif selection == "Holy Ghost":

                st.markdown("""
## Gift of the Holy Ghost

The Gift of the Holy Ghost is the Lord's Spirit coming down from heaven and coming to live on the inside of you.

The way you will know He is living in you is when you start to speak in an unknown language according to **Acts 2:4**.

The Lord's spirit will manifest inside you and give you the power over:

**Flesh  
Devils  
And Much More**
""")


if __name__ == "__main__":
    main()
