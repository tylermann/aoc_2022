.PHONY: build
build:
	docker build -t aoc .

.PHONY: shell
shell:
	docker run `pwd`:/code --rm -it sh
