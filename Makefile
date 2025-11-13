.PHONY: help build up down restart logs shell clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

build: ## Build the Docker image
	docker compose build

up: ## Start the development environment
	docker compose up

up-d: ## Start the development environment in detached mode
	docker compose up -d

down: ## Stop the development environment
	docker compose down

restart: ## Restart the development environment
	docker compose restart

logs: ## Show logs from the container
	docker compose logs -f atrain

shell: ## Open a bash shell in the running container
	docker compose exec atrain bash

clean: ## Remove containers, networks, and volumes
	docker compose down -v

init-models: ## Initialize and download required ML models
	docker compose exec atrain python -m aTrain init

dev-local: ## Run aTrain in development mode locally (without Docker)
	python -m aTrain dev
