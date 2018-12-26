#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyarchops_SKELETON` package."""

from suitable import Api
from pyarchops_SKELETON import SKELETON
from tests.test_helpers import ephemeral_docker_container


def test_SKELETON_using_docker():
    """Test the SKELETON."""

    with ephemeral_docker_container(
            image='azulinho/pyarchops-base'
    ) as container:
        connection_string = "{}:{}".format(
            container['ip'], container['port']
        )
        print('connection strings is ' + connection_string)
        api = Api(connection_string,
                  connection='smart',
                  remote_user=container['user'],
                  private_key_file=container['pkey'],
                  become=True,
                  become_user='root',
                  sudo=True,
                  ssh_extra_args='-o StrictHostKeyChecking=no')

        try:
            result = SKELETON.apply(api)['contacted'][connection_string]
        except Exception as error:
            raise error

        assert result['msg'] == 'REPLACE ME'
