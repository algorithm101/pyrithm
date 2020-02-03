# Copyright 2020 The Algorithm101 Authors.
#
# The old school Makefile, following are required targets. The Makefile is written
# to allow building multiple binaries. You are free to add more targets or change
# existing implementations, as long as the semantics are preserved.
#
#   make              - default to 'all' target
#   make all          - run lint, test
#   make lint         - code analysis
#   make test         - run unit test (or plus integration test)
#   make test-docker  - run unit test (in docker containers)
#   make cp           - cp pkg/pxxxx from template
#   make clean        - clean up targets
#   make help         - show help doc
#
# Not included but recommended targets:
#   make e2e-test
#
# The makefile is also responsible to populate project version information.
#

#
# Tweak the variables based on your project.
#

# This repo's root import path.
ROOT := 

# Target binaries. You can build multiple binaries for a single project.
TARGETS := 

# Container image prefix and suffix added to targets.
# The final built images are:
#   $[REGISTRY]/$[IMAGE_PREFIX]$[TARGET]$[IMAGE_SUFFIX]:$[VERSION]
# $[REGISTRY] is an item from $[REGISTRIES], $[TARGET] is an item from $[TARGETS].
IMAGE_PREFIX ?= $(strip )
IMAGE_SUFFIX ?= $(strip )

# Container registries.
REGISTRY ?= 

# Container registry for base images.
BASE_REGISTRY ?= 

#
# These variables should not need tweaking.
#

# It's necessary to set this because some environments don't link sh -> bash.
export SHELL := /bin/bash

# It's necessary to set the errexit flags for the bash shell.
export SHELLOPTS := errexit

# Project main package location (can be multiple ones).
CMD_DIR := ./cmd

# Project output directory.
OUTPUT_DIR := ./bin

# Build direcotory.
BUILD_DIR := ./build

# Current version of the project.
VERSION ?= $(shell git describe --tags --always --dirty)

# Available cpus for compiling.
export CPUS ?= $(shell /bin/bash hack/read_cpus_available.sh)

# Track code version with Docker Label.
DOCKER_LABELS ?= git-describe="$(shell date -u +v%Y%m%d)-$(shell git describe --tags --always --dirty)"

# python standard bin directory.

#
# Define all targets. At least the following commands are required:
#

# All targets.
.PHONY: all

all: lint test ## run lint, test, default

lint: ## code analysis
# ifeq (, $(shell which pylint))
#	pip3 install pylint
# endif
	pylint ./pkg/ --rcfile=./.pylintrc

test: ## run unit test (or plus integration test)
	cd ./pkg && coverage run main.py && coverage xml

help: ## display this help string
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	
.PHONY: clean
clean:
	@-rm -vrf ${OUTPUT_DIR}
	@-rm -f .coverage
