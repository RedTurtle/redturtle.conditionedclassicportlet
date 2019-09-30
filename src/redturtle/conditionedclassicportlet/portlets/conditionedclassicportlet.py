# -*- coding: utf-8 -*-
from Products.CMFCore.Expression import Expression, getExprContext
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.portlets import base
from plone.app.portlets.portlets.classic import AddForm as baseAddForm
from plone.app.portlets.portlets.classic import EditForm as baseEditForm
from plone.app.portlets.portlets.classic import IClassicPortlet
from plone.app.portlets.portlets.classic import Renderer as baseRenderer
from plone.portlets.interfaces import IPortletDataProvider
from redturtle.conditionedclassicportlet import _
from zope import schema
from zope.interface import implementer
import six


class ITalesConditionedClassicPortletPortlet(IClassicPortlet):
    tales_expression = schema.TextLine(
        title=_(u'Write a tales expression to calculate portlet availability'),
        description=_(u'This field is evaluated as expression'),
        required=True,
        default=u'python: True'
    )


@implementer(ITalesConditionedClassicPortletPortlet)
class Assignment(base.Assignment):
    schema = ITalesConditionedClassicPortletPortlet

    def __init__(self, template='', macro='', tales_expression=''):
        self.template = template
        self.macro = macro
        self.tales_expression = tales_expression


    @property
    def title(self):
        return _(u'Tales conditioned static portlet: {}'.format(self.data.tales_expression))

class AddForm(baseAddForm):
    schema = ITalesConditionedClassicPortletPortlet
    label = _(u"Add Conditioned Classic Portlet")
    description = _(u"A classic portlet allows you to use legacy portlet "
                    u"templates.")

    def create(self, data):
        return Assignment(template=data.get('template', ''),
                          macro=data.get('macro', ''),
                          tales_expression=data.get('tales_expression', ''))


class EditForm(baseEditForm):
    schema = ITalesConditionedClassicPortletPortlet
    label = _(u"Edit Conditioned Classic Portlet")
    description = _(u"A classic portlet allows you to use legacy portlet "
                    u"templates.")


class Renderer(baseRenderer):
    _template = ViewPageTemplateFile('conditionedclassicportlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    def render(self):
        return self._template()

    def get_expression(self, context, expression_string, **kwargs):
        """ Get TALES expression

        :param context: [required] TALES expression context
        :param string expression_string: [required] TALES expression string
        :param dict kwargs: additional arguments for expression
        :returns: result of TALES expression
        """
        if six.PY2 and isinstance(expression_string, six.text_type):
            expression_string = expression_string.encode("utf-8")

        expression_context = getExprContext(context, context)
        for key in kwargs:
            expression_context.setGlobal(key, kwargs[key])
        expression = Expression(expression_string)
        return expression(expression_context)

    @property
    def available(self):
        portlet_expression = self.data.tales_expression
        expression_value = self.get_expression(self.context, portlet_expression)
        print(expression_value)
        return expression_value

