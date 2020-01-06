BASE_TAG=juppy-base
IMAGE_TAG=juppy

.PHONY: build-base build-min build

build-base:
	cd juppy-base && docker build -t $(BASE_TAG) .

build-min:
	docker build -t $(IMAGE_TAG) -f juppy/Dockerfile .

build: build-base build-min
