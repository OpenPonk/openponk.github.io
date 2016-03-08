.PHONY: build deploy

build:
	mkdocs build --clean

deploy:
	mkdocs gh-deploy -b master --clean
