include demo_package/Makefile

_build_package:
	make -C demo_package build

_collect_packages:
	./collect-dists.py demo_package .packages/

run_clean:
	docker run -it --rm --name my-pypi -p 8080:8080 --volume ./.packages:/data/packages pypiserver/pypiserver

run: _build_package _collect_packages run_clean
