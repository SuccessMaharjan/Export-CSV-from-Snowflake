import streamlit as st
import subprocess

def run_makefile():
    result = subprocess.run(['make'], capture_output=True, text=True)
    return result.stdout, result.stderr

st.title('Run Makefile from Streamlit')

if st.button('Export Snowflake CSV Data'):
    status_placeholder = st.empty()
    with st.spinner('Exporting CSV...'):
        status_placeholder.info('Exporting CSV ...')
        stdout, stderr = run_makefile()
        status_placeholder.success('CSV Export and Load to Target Snowflake completed.')

    st.subheader('Output')
    st.text(stdout)
    st.subheader('Errors')
    st.text(stderr)
