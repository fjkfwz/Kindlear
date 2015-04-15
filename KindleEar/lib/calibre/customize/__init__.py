from __future__ import with_statement
__license__   = 'GPL v3'
__copyright__ = '2008, Kovid Goyal <kovid at kovidgoyal.net>'

platform = 'linux'

class PluginNotFound(ValueError):
    pass

class InvalidPlugin(ValueError):
    pass


class Plugin(object): # {{{
    '''
    A calibre plugin. Useful members include:

       * ``self.plugin_path``: Stores path to the zip file that contains
                               this plugin or None if it is a builtin
                               plugin
       * ``self.site_customization``: Stores a customization string entered
                                      by the user.

    Methods that should be overridden in sub classes:

       * :meth:`initialize`
       * :meth:`customization_help`

    Useful methods:

        * :meth:`temporary_file`

    '''
    #: List of platforms this plugin works on
    #: For example: ``['windows', 'osx', 'linux']``
    supported_platforms = []

    #: The name of this plugin. You must set it something other
    #: than Trivial Plugin for it to work.
    name           = 'Trivial Plugin'

    #: The version of this plugin as a 3-tuple (major, minor, revision)
    version        = (1, 0, 0)

    #: A short string describing what this plugin does
    description    = 'Does absolutely nothing'

    #: The author of this plugin
    author         = 'Unknown'

    #: When more than one plugin exists for a filetype,
    #: the plugins are run in order of decreasing priority
    #: i.e. plugins with higher priority will be run first.
    #: The highest possible priority is ``sys.maxint``.
    #: Default priority is 1.
    priority = 1

    #: The earliest version of calibre this plugin requires
    minimum_calibre_version = (0, 4, 118)

    #: If False, the user will not be able to disable this plugin. Use with
    #: care.
    can_be_disabled = True

    #: The type of this plugin. Used for categorizing plugins in the
    #: GUI
    type = 'Base'

    def __init__(self, plugin_path):
        self.plugin_path        = plugin_path
        self.site_customization = None

    def initialize(self):
        '''
        Called once when calibre plugins are initialized. Plugins are re-initialized
        every time a new plugin is added.

        Perform any plugin specific initialization here, such as extracting
        resources from the plugin zip file. The path to the zip file is
        available as ``self.plugin_path``.

        Note that ``self.site_customization`` is **not** available at this point.
        '''
        pass

    def config_widget(self):
        '''
        Implement this method and :meth:`save_settings` in your plugin to
        use a custom configuration dialog, rather then relying on the simple
        string based default customization.

        This method, if implemented, must return a QWidget. The widget can have
        an optional method validate() that takes no arguments and is called
        immediately after the user clicks OK. Changes are applied if and only
        if the method returns True.

        If for some reason you cannot perform the configuration at this time,
        return a tuple of two strings (message, details), these will be
        displayed as a warning dialog to the user and the process will be
        aborted.
        '''
        raise NotImplementedError()

    def save_settings(self, config_widget):
        '''
        Save the settings specified by the user with config_widget.

        :param config_widget: The widget returned by :meth:`config_widget`.

        '''
        raise NotImplementedError()

    def do_user_config(self, parent=None):
        pass

    def load_resources(self, names):
        pass


    def customization_help(self, gui=False):
        '''
        Return a string giving help on how to customize this plugin.
        By default raise a :class:`NotImplementedError`, which indicates that
        the plugin does not require customization.

        If you re-implement this method in your subclass, the user will
        be asked to enter a string as customization for this plugin.
        The customization string will be available as
        ``self.site_customization``.

        Site customization could be anything, for example, the path to
        a needed binary on the user's computer.

        :param gui: If True return HTML help, otherwise return plain text help.

        '''
        raise NotImplementedError

    #def temporary_file(self, suffix):
        '''
        Return a file-like object that is a temporary file on the file system.
        This file will remain available even after being closed and will only
        be removed on interpreter shutdown. Use the ``name`` member of the
        returned object to access the full path to the created temporary file.

        :param suffix: The suffix that the temporary file will have.
        '''
        #return PersistentTemporaryFile(suffix)

    def is_customizable(self):
        try:
            self.customization_help()
            return True
        except NotImplementedError:
            return False

    def __enter__(self, *args):
        pass


    def __exit__(self, *args):
        pass

    def cli_main(self, args):
        '''
        This method is the main entry point for your plugins command line
        interface. It is called when the user does: calibre-debug -r "Plugin
        Name". Any arguments passed are present in the args variable.
        '''
        raise NotImplementedError('The %s plugin has no command line interface'
                                  %self.name)

# }}}

class FileTypePlugin(Plugin): # {{{
    '''
    A plugin that is associated with a particular set of file types.
    '''

    #: Set of file types for which this plugin should be run
    #: For example: ``set(['lit', 'mobi', 'prc'])``
    file_types     = set([])

    #: If True, this plugin is run when books are added
    #: to the database
    on_import      = False

    #: If True, this plugin is run after books are added
    #: to the database
    on_postimport  = False

    #: If True, this plugin is run just before a conversion
    on_preprocess  = False

    #: If True, this plugin is run after conversion
    #: on the final file produced by the conversion output plugin.
    on_postprocess = False

    type = 'File type'

    def run(self, path_to_ebook):
        '''
        Run the plugin. Must be implemented in subclasses.
        It should perform whatever modifications are required
        on the ebook and return the absolute path to the
        modified ebook. If no modifications are needed, it should
        return the path to the original ebook. If an error is encountered
        it should raise an Exception. The default implementation
        simply return the path to the original ebook.

        The modified ebook file should be created with the
        :meth:`temporary_file` method.

        :param path_to_ebook: Absolute path to the ebook.

        :return: Absolute path to the modified ebook.
        '''
        # Default implementation does nothing
        return path_to_ebook

    def postimport(self, book_id, book_format, db):
        '''
        Called post import, i.e., after the book file has been added to the database.

        :param book_id: Database id of the added book.
        :param book_format: The file type of the book that was added.
		:param db: Library database.
        '''
        pass # Default implementation does nothing
