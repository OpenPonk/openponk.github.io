.PHONY: build deploy

build:
	mkdocs build --clean

deploy:
	mkdocs gh-deploy -b master --clean

push:
	git push origin source
	git push origin master
