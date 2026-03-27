#!/usr/bin/env bash
set -euo pipefail

cd /workspaces/lifelike

COMPOSE_ARGS=(
	-p lifelike
	-f docker/docker-compose.yml
	-f docker/docker-compose.services.yml
	-f docker/docker-compose.dev.yml
)

run_compose() {
	docker compose "${COMPOSE_ARGS[@]}" up -d --build --wait
}

retry_with_compatible_api_if_needed() {
	local err_log
	local max_api
	err_log="$(mktemp)"

	if run_compose 2> >(tee "$err_log" >&2); then
		rm -f "$err_log"
		return 0
	fi

	max_api="$(sed -n 's/.*Maximum supported API version is \([0-9.]\+\).*/\1/p' "$err_log" | tail -n 1)"
	rm -f "$err_log"

	if [[ -z "$max_api" ]]; then
		return 1
	fi

	echo "Detected Docker API mismatch. Retrying with DOCKER_API_VERSION=$max_api"
	DOCKER_API_VERSION="$max_api" run_compose
}

echo "Building and starting the full Lifelike Afterhours stack (development mode)..."
retry_with_compatible_api_if_needed

echo "Lifelike Afterhours stack is ready. The client will be available on http://localhost:8080"
