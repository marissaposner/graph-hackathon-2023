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
PATH = "/subgraphs/subgraphs/" #TODO UPDATE

class SubgraphService:
    def get_prod_subgraphs(self):
        protocols = {}

        with os.scandir(os.getcwdb().decode("utf-8") + PATH) as it:
            for entry in it:
                # only consider directories that arent prefixed by a dot or underscore
                if not entry.name.startswith((".", "_")) and not entry.is_file():
                    protocols[entry.name] = {}

        # gather protocol names and include them if their schema adheres to the standard
        unfinished_protocols = []
        f = open(os.getcwdb().decode("utf-8") + "/subgraphs/deployment/deployment.json")
        deployment = json.load(f)
        for protocol in protocols:
            if protocol == "opensea":
                import pdb;pdb.set_trace()
            try:

                schema_file = os.path.join(os.getcwdb().decode("utf-8") + PATH, protocol, "schema.graphql")
                with open(schema_file) as f:
                    first_line = f.readline()
                    protocols[protocol]["schema_file"] = schema_file
                # gather deployment data for protocol
                if protocol in deployment:
                    protocols[protocol]["type"] = deployment[protocol]["schema"]
                    protocols[protocol]["deployments"] = {}  # network_label: {}}
                    for chain in deployment[protocol]["deployments"]:

                        # if deployment[protocol]["deployments"][chain]["status"] == "prod":
                        network_label = deployment[protocol]["deployments"][chain][
                            "network"
                        ]
                        protocols[protocol]["deployments"][network_label] = deployment[
                            protocol
                        ]["deployments"][chain]["services"]
                        if len(protocols[protocol]["deployments"]) == 0:
                            # no production ready deployments founds
                            unfinished_protocols.append(protocol)
                if "deployments" not in protocols[protocol]:
                    # no deployments founds
                    unfinished_protocols.append(protocol)
            except FileNotFoundError:
                # no graphql schema found
                unfinished_protocols.append(protocol)
        # for protocol in set(unfinished_protocols):
        #     protocols.pop(protocol)


        return protocols

    # dev: for debugging purposes
    # from pprint import pprint

    # pprint(protocols)
    # print(len(protocols))
