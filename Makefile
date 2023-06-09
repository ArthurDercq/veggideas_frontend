install_requirements:
	@pip install -r requirements.txt

streamlit:
	-@streamlit run streamlit.py
