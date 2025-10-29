.PHONY: setup preprocess train explain clean

setup: 
	pip install -r requirements.txt

preprocess:
	python3 scripts/preprocess_data.py

train:
	python3 scripts/train_model.py

clean:
	rm -rf __pycache__ models/*.xgb shap_plots/
