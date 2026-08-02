#!/usr/bin/env python3
"""Deploy a PBIP project to a Fabric workspace using fabric-cicd."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Deploy Belgium Pulse PBIP to Microsoft Fabric")
    parser.add_argument("--workspace-name", required=True, help="Target Fabric workspace name")
    parser.add_argument("--environment", default="dev", help="Deployment environment label")
    parser.add_argument(
        "--repository-directory",
        default="powerbi/pbip",
        help="Directory containing the saved PBIP project",
    )
    parser.add_argument(
        "--spn-auth",
        action="store_true",
        help="Use Azure CLI credentials in CI instead of an interactive browser login",
    )
    args = parser.parse_args()

    from azure.identity import AzureCliCredential, InteractiveBrowserCredential
    from fabric_cicd import FabricWorkspace, publish_all_items

    repository_directory = Path(args.repository_directory).resolve()
    if not repository_directory.exists():
        raise SystemExit(
            f"PBIP directory not found: {repository_directory}. "
            "Create it first using the steps in powerbi/README.md."
        )

    credential = AzureCliCredential() if args.spn_auth else InteractiveBrowserCredential()
    workspace = FabricWorkspace(
        workspace_name=args.workspace_name,
        environment=args.environment,
        repository_directory=str(repository_directory),
        item_type_in_scope=["SemanticModel", "Report"],
        token_credential=credential,
    )
    publish_all_items(workspace)


if __name__ == "__main__":
    main()

