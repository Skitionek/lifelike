HELM_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: helm-lint helm-dependency-update helm-schema-gen helm-docs helm-package helm-install helm-install-single-node


helm-lint: ##@helm Run helm lint on mycelium chart
	helm lint ${HELM_DIR}/mycelium --strict ${args}

helm-dependency-update: ##@helm Install or update chart dependencies
	helm dependency update ${HELM_DIR}/mycelium ${args}

helm-schema-gen: ##@helm Generate Helm chart values JSON schema
	helm schema-gen ${HELM_DIR}/mycelium/values.yaml > ${HELM_DIR}/mycelium/values.schema.json

helm-docs: ##@helm Generate Helm chart README docs
	helm-docs -c ${HELM_DIR}/mycelium -s file

helm-package: ##@helm Generate mycelium helm chart package
	helm package ${HELM_DIR}/mycelium --dependency-update --destination ${HELM_DIR} ${args}

registry:=https://helm.apps.mycelium.cloud
u:=mycelium
helm-publish: helm-lint helm-schema-gen helm-docs ##@helm Publish a new version of mycelium helm chart to the ChartMuseum registry
	helm cm-push ${HELM_DIR}/mycelium ${registry} -u ${u} -p ${p} ${args}

namespace:=mycelium
helm-install: ##@helm Install or upgrade mycelium chart <n=namespace>
	@echo "Executing helm command (copy and modify if needed):\n"
	helm upgrade \
      --namespace ${namespace} \
      --install \
      --create-namespace \
      mycelium ${HELM_DIR}/mycelium \
      ${args}

helm-install-single-node: args:=--values ${HELM_DIR}/mycelium/examples/single-node.yaml
helm-install-single-node: helm-install ##@helm Install or upgrade mycelium chart using the single-node.yaml example values
