.PHONY: build
build:
	docker build -t aoc .

.PHONY: shell
shell:
	docker run -v `pwd`:/code --rm -it aoc sh
