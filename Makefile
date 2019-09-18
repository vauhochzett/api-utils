.PHONY: build release upload

build:
	@echo "--> Building"
	python3 setup.py sdist bdist_wheel

upload:
	@echo "--> Uploading"
	twine upload dist/* --username ${TWINE_USERNAME} --password ${TWINE_PASSWORD}

release: build upload
