"""
instructions:
$ git clone git@github.com:messari/subgraphs.git in the project's root dir

scan the messari subgraphs repository and build an overview of production ready
subgraphs with:
- filename to their graphql schema
- subgraph type (lending, dex-amm, generic, governance, bridge, yield-aggregator, nft-marketplace)
- network(s)
- their subgraph id, both for hosted and/or decentralised subgraphs
"""
import json
import os

import yaml


class SubgraphService:
    def __init__(self, protocol, chain):
        self.protocol = protocol
        self.chain = chain
        self.deployments_json = json.load(
            open(os.getcwdb().decode("utf-8") + "/subgraphs/deployment/deployment.json")
        )
        self.deployments = self.deployments_json[protocol]
        if (
            "decentralized-network"
            in self.deployments["deployments"][f"{protocol}-{chain}"]["services"]
        ):
            self.service_type = "decentralized-network"
        elif (
            "hosted-service"
            in self.deployments["deployments"][f"{protocol}-{chain}"]["services"]
        ):
            self.service_type = "hosted-service"
        try:
            self.query_id = self.deployments["deployments"][f"{protocol}-{chain}"][
                "services"
            ][self.service_type]["query-id"]
        except AttributeError:
            # protocol does not have any deployments
            raise NotImplementedError
        self.base = self.deployments["base"]
        self.template_filename = self.deployments["deployments"][f"{protocol}-{chain}"][
            "files"
        ]["template"]
        self.template_file_location = f"subgraphs/subgraphs/{self.base}/protocols/{self.protocol}/config/templates/{self.template_filename}"

    def parse_template_file(self):
        # TODO: yaml.constructor.ConstructorError: while constructing a mapping
        with open(self.template_file_location, "r") as stream:
            yaml_content = yaml.safe_load(stream)
        print(yaml_content)
