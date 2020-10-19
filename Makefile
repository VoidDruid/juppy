BASE_TAG=juppy-base
IMAGE_TAG=juppy
OUT=out

.PHONY: build-base build-min build

build-base:
	docker build -t $(BASE_TAG) -f juppy-base/Dockerfile juppy-base
	python3 copy_envs.py $(BASE_TAG) $(OUT)

# Expects image juppy-base to exist
build-min:
	docker build -t $(IMAGE_TAG) -f juppy/Dockerfile juppy
	python3 copy_envs.py $(IMAGE_TAG) $(OUT)

build: build-base build-min
