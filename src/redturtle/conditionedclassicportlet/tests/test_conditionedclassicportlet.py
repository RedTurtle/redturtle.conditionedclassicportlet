# -*- coding: utf-8 -*-
from redturtle.conditionedclassicportlet.testing import REDTURTLE_CONDITIONEDCLASSICPORTLET_FUNCTIONAL_TESTING
from redturtle.conditionedclassicportlet.testing import REDTURTLE_CONDITIONEDCLASSICPORTLET_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility

import unittest


class PortletIntegrationTest(unittest.TestCase):

    layer = REDTURTLE_CONDITIONEDCLASSICPORTLET_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.app = self.layer['app']
        self.request = self.app.REQUEST
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_conditionedclassicportlet_is_registered(self):
        portlet = getUtility(
            IPortletType,
            name='redturtle.conditionedclassicportlet.portlets.Conditionedclassicportlet',
        )
        self.assertEqual(portlet.addview, 'redturtle.conditionedclassicportlet.portlets.Conditionedclassicportlet')


class PortletFunctionalTest(unittest.TestCase):

    layer = REDTURTLE_CONDITIONEDCLASSICPORTLET_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
