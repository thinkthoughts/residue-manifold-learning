setup:
	pip install -r requirements.txt

run:
	jupyter notebook

paper:
	@echo "Edit paper/paper.md"

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
