include demo_package/Makefile

_build_package:
	make build

_collect_packages:
	./collect-dists.py demo_package .packages/

run: _build_package _collect_packages
	docker run -it --rm --name my-pypi -p 8080:8080 --volume ./.packages:/data/packages pypiserver/pypiserver
