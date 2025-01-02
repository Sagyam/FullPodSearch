.PHONY: dev build test lint clean

dev:
	docker-compose -f docker/development/docker-compose.yml up

build:
	docker-compose -f docker/development/docker-compose.yml build

test:
	cd frontend && npm test
	cd services/upload-service && cargo test
	cd services/processing-service && go test ./...
	cd services/search-service && pytest

lint:
	cd frontend && npm run lint
	cd services/upload-service && cargo clippy
	cd services/processing-service && golangci-lint run
	cd services/search-service && flake8

clean:
	docker-compose -f docker/development/docker-compose.yml down -v
	rm -rf **/node_modules **/target **/dist
