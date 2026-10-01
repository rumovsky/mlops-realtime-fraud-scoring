import pandas as pd
import streamlit as st


st.set_page_config(page_title="Realtime fraud scoring", page_icon="✅")
st.title("Realtime fraud scoring")
st.write("Минимальный интерфейс для проверки загрузки CSV.")

uploaded_file = st.file_uploader("Загрузите CSV-файл", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
    except Exception as error:
        st.error(f"Не удалось прочитать CSV: {error}")
    else:
        st.success("OK: CSV-файл успешно загружен.")
        st.write(f"Строк: {len(data)}; столбцов: {len(data.columns)}")
        st.dataframe(data.head(10), use_container_width=True)
