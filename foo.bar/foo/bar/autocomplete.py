from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid, Interface
from zope.schema.interfaces import IContextSourceBinder
#from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
#from plone.app.textfield import RichText
#from plone.namedfile.field import NamedImage, NamedFile
#from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable


from foo.bar import MessageFactory as _

from plone.formwidget.autocomplete import AutocompleteFieldWidget, AutocompleteMultiFieldWidget
from plone.formwidget.contenttree import PathSourceBinder


class Iautocomplete(form.Schema, IImageScaleTraversable):
    """
    test autocomplete
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/autocomplete.xml to define the content type.

    form.model("models/autocomplete.xml")

    form.widget(single=AutocompleteFieldWidget)
    single = schema.Choice(
        title=_(u"Single"),
        source=PathSourceBinder(portal_type='Document'),
        required=False,)

    form.widget(multiple=AutocompleteMultiFieldWidget)
    multiple = schema.Set(
            title=_(u'Multiple'),
            value_type=schema.Choice(source=PathSourceBinder(portal_type='Document')),
            required=False,
        )


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class autocomplete(Container):
    grok.implements(Iautocomplete)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# autocomplete_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(Iautocomplete)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
