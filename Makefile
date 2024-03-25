all: help

UID!=id -u
GID!=id -g

generate:  ## Generate python library from the OpenAPI specification
	mkdir -p out
	docker run --rm -v $(PWD):/local openapitools/openapi-generator-cli:latest generate -i /local/ShippingAPI_OAS.yaml -g python -o /local/out/pbclient --package-name pbclient -p packageVersion=2.0.0
	docker run --rm -v $(PWD):/local openapitools/openapi-generator-cli:latest chown -R $(UID):$(GID) /local/out/pbclient

validate:
	docker run --rm -v $(PWD):/local openapitools/openapi-generator-cli:latest validate -i /local/ShippingAPI_OAS.yaml

help:  ## Show this help.
	@grep -E "^[^._][a-zA-Z_-]*:" Makefile | awk -F '[:#]' '{print $$1, ":", $$NF}' | sort | column -t -s:

.SILENT: generate help
.PHONY: generate help
