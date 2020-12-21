include make_env

VERSION ?= latest
CONTAINER_NAME ?= nyx-lab
CONTAINER_INSTANCE ?= default

.PHONY: run

run-new:
	tensorman run --gpu --python3 \
	$(PORTS) \
	--root \
	--jupyter \
	--name $(CONTAINER_NAME) \
	bash

run:
	tensorman '=$(CONTAINER_NAME)' \
	run \
	--gpu \
	--python3 \
	$(PORTS) \
	--root \
	--jupyter \
	bash
