import pytest
import os
import json
from cloudtower.models import GetClustersRequestBody, ClusterWhereInput, GetVlansRequestBody, VlanWhereInput, VdsWhereInput


@pytest.fixture(scope="session")
def default_data():
    with open(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', "resource/default.json"))) as default_data:
        config = json.load(default_data)
    return config


@pytest.fixture(scope="class")
def default_cluster(client, default_data, cluster_api):
    cluster = cluster_api.get_clusters(get_clusters_request_body=GetClustersRequestBody(
        where=ClusterWhereInput(
            name=default_data["cluster"]
        )
    ))[0]
    if(cluster is None):
        raise Exception("default data is incorrect, please check the config file")
    return cluster


@pytest.fixture(scope="class")
def default_vlan(client, default_data, default_cluster, vlan_api):
    vlan = vlan_api.get_vlans(get_vlans_request_body=GetVlansRequestBody(
        where=VlanWhereInput(
            name="default",
            vds=VdsWhereInput(
                cluster=ClusterWhereInput(
                    id=default_cluster.id
                ),
                internal=False
            )
        )
    ))[0]
    if(vlan is None):
        raise Exception("default data is incorrect, please check the config file")
    return vlan
