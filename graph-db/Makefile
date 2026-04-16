# ============================================================================
# Graph-DB convenience targets
#
# Usage examples:
#   make extract         DOMAIN=kegg
#   make changelog       DOMAIN=kegg AUTHOR="Jane" CHANGELOG_DIR=lifelike-graph
#   make full-load       DOMAIN=kegg AUTHOR="Jane"
#   make migrate
#   make dev-up
#
# Required env vars for the extractor (or set in extractor/src/common/properties.ini):
#   NEO4J_URI, NEO4J_DATABASE, NEO4J_USERNAME, NEO4J_PASSWORD
#   AZURE_ACCOUNT_STORAGE_NAME, AZURE_ACCOUNT_STORAGE_KEY
# ============================================================================

PYTHON        ?= python3
APP           := extractor/src/app.py
DOMAIN        ?= kegg
AUTHOR        ?= $(USER)
PREFIX        ?=
CHANGELOG_DIR ?= lifelike-graph
INITIAL_LOAD  ?=

_PREFIX_ARG        := $(if $(PREFIX),--prefix $(PREFIX),)
_INITIAL_LOAD_ARG  := $(if $(INITIAL_LOAD),--initial-load,)

# ── Extract: parse raw sources and upload TSVs to Azure ───────────────────
.PHONY: extract
extract:
	$(PYTHON) $(APP) $(_PREFIX_ARG) $(DOMAIN)

# ── Generate changelog: produce next changelog-NNNN.xml in the right dir ──
.PHONY: changelog
changelog:
	$(PYTHON) $(APP) $(_PREFIX_ARG) generate-changelog \
		--author "$(AUTHOR)" \
		--changelog-dir $(CHANGELOG_DIR) \
		$(_INITIAL_LOAD_ARG) \
		$(DOMAIN)

# ── Full load: extract + changelog in one shot ────────────────────────────
.PHONY: full-load
full-load:
	$(PYTHON) $(APP) $(_PREFIX_ARG) full-load \
		--author "$(AUTHOR)" \
		--changelog-dir $(CHANGELOG_DIR) \
		$(_INITIAL_LOAD_ARG) \
		$(DOMAIN)

# ── Start a local Neo4j + migrator stack (requires docker-compose) ────────
.PHONY: dev-up
dev-up:
	docker compose up -d neo4j migrator

# ── Run Liquibase migrations against the local stack ─────────────────────
.PHONY: migrate
migrate:
	docker compose run --rm migrator update

# ── Tear down the local stack ─────────────────────────────────────────────
.PHONY: dev-down
dev-down:
	docker compose down

.PHONY: help
help:
	@echo ""
	@echo "Graph-DB Makefile targets"
	@echo "--------------------------"
	@echo "  extract       DOMAIN=<domain>               Parse + upload TSVs"
	@echo "  changelog     DOMAIN=<domain> AUTHOR=<name> Generate changelog XML"
	@echo "  full-load     DOMAIN=<domain> AUTHOR=<name> Extract + changelog"
	@echo "  dev-up                                       Start local Neo4j + migrator"
	@echo "  migrate                                      Run Liquibase against local stack"
	@echo "  dev-down                                     Stop local stack"
	@echo ""
	@echo "Optional variables: PREFIX, CHANGELOG_DIR (default: lifelike-graph), INITIAL_LOAD=1"
	@echo ""
	@echo "Available domains (extract):    $(shell echo $(DOMAINS_EXTRACT))"
	@echo "Available domains (changelog):  $(shell echo $(DOMAINS_CHANGELOG))"
