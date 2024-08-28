_build_container:
	docker build --tag tmp/package-builder .

_run_container:
	docker run --rm -it --volume ./dist:/root/package/dist tmp/package-builder

build: _build_container _run_container
