include make_env

VERSION ?= latest
CONTAINER_NAME ?= nyx
CONTAINER_INSTANCE ?= default

.PHONY: run
build:
	docker build -f docker/Dockerfile -t $(NS)/$(IMAGE_NAME):$(VERSION) \
	--build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) \
	docker/context
run:
	docker run -u $(shell id -u):$(shell id -g) \
	--rm --runtime=nvidia --name \
	$(CONTAINER_NAME)-$(CONTAINER_INSTANCE) \
	$(PORTS) $(VOLUMES) $(NS)/$(IMAGE_NAME):$(VERSION)

shell:
	docker exec -it $(CONTAINER_NAME)-$(CONTAINER_INSTANCE) bash