_build_container:
	docker build --network host --tag tmp/package-builder .

_run_container:
	docker run --rm -it --network host --volume ./dist:/root/package/dist tmp/package-builder

build: _build_container _run_container
