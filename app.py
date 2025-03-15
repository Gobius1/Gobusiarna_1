import streamlit as st
import openai

# Nastavení API klíče (musíš mít v Streamlit secrets)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ID asistenta (nahraď správným ID tvého asistenta!)
ASSISTANT_ID = "asst_7SArgO1kADdwIEIDmeCiLbWl"

# Inicializace OpenAI klienta
client = openai.OpenAI()

# Titulek aplikace
st.title("Predikce(Předpověď děje)")

# Vysvětlení aplikace
st.write("Zadejte otázku a zjistěte, jak by mohla vypadat historie jinak!")

# Textové pole pro vstup uživatele
user_input = st.text_input("Zadejte svou otázku:")

# Když uživatel zadá otázku a stiskne Enter
if user_input:
    with st.spinner("Asistent přemýšlí..."):
        response = client.beta.threads.create_and_run(
            assistant_id=ASSISTANT_ID,
            thread={
                "messages": [
                    {"role": "user", "content": user_input}
                ]
            }
        )
        # Zobrazení odpovědi asistenta
        message = response.latest_message.content
        st.write("**Asistent:**", message)
