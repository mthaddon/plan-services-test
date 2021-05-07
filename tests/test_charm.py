# Copyright 2021 Tom Haddon
# See LICENSE file for licensing details.
#
# Learn more about testing at: https://juju.is/docs/sdk/testing

import unittest

from charm import PlanServicesTestCharm
from ops.model import ActiveStatus
from ops.testing import Harness


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = Harness(PlanServicesTestCharm)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()

    def test_config_changed(self):
        self.harness.update_config({"thing": "foo"})
        self.assertEqual(self.harness.model.unit.status, ActiveStatus())
