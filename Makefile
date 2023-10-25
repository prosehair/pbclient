all: help

UID!=id -u
GID!=id -g

generate:  ## Generate python library from the OpenAPI specification
	mkdir -p out
	docker run --rm -v $(PWD):/local openapitools/openapi-generator-cli:v7.0.0 generate -i /local/ShippingAPI_OAS.yaml -g python -o /local/out/pbclient --package-name pbclient
	docker run --rm -v $(PWD):/local openapitools/openapi-generator-cli:v7.0.0 chown -R $(UID):$(GID) /local/out/pbclient

validate:
	docker run --rm -v $(PWD):/local openapitools/openapi-generator-cli:v7.0.0 validate -i /local/ShippingAPI_OAS.yaml

help:  ## Show this help.
	@grep -E "^[^._][a-zA-Z_-]*:" Makefile | awk -F '[:#]' '{print $$1, ":", $$NF}' | sort | column -t -s:

.SILENT: generate help
.PHONY: generate help
