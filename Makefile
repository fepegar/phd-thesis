count:
	texcount root.tex -incbib -inc -sum -1

fixref:
	python scripts/bold_name_references.py

precommit:
	pre-commit run --all-files
