# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import redturtle.conditionedclassicportlet


class RedturtleConditionedclassicportletLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=redturtle.conditionedclassicportlet)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'redturtle.conditionedclassicportlet:default')


REDTURTLE_CONDITIONEDCLASSICPORTLET_FIXTURE = RedturtleConditionedclassicportletLayer()


REDTURTLE_CONDITIONEDCLASSICPORTLET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(REDTURTLE_CONDITIONEDCLASSICPORTLET_FIXTURE,),
    name='RedturtleConditionedclassicportletLayer:IntegrationTesting',
)


REDTURTLE_CONDITIONEDCLASSICPORTLET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(REDTURTLE_CONDITIONEDCLASSICPORTLET_FIXTURE,),
    name='RedturtleConditionedclassicportletLayer:FunctionalTesting',
)


REDTURTLE_CONDITIONEDCLASSICPORTLET_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        REDTURTLE_CONDITIONEDCLASSICPORTLET_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RedturtleConditionedclassicportletLayer:AcceptanceTesting',
)
