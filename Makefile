all: help

UID!=id -u
GID!=id -g

generate:  ## Generate python library from the OpenAPI specification
	mkdir -p out
	docker run --rm -v $(PWD):/local openapitools/openapi-generator-cli generate -i /local/ShippingAPI_OAS.yaml -g python-nextgen -o /local/out/pbclient --package-name pbclient
	docker run --rm -v $(PWD):/local openapitools/openapi-generator-cli chown -R $(UID):$(GID) /local/out/pbclient

help:  ## Show this help.
	@grep -E "^[^._][a-zA-Z_-]*:" Makefile | awk -F '[:#]' '{print $$1, ":", $$NF}' | sort | column -t -s:

.SILENT: generate help
.PHONY: generate help
