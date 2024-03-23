from django_imagep.interface import IProcessingFactory
from imagep.factory import LibraryFactory


class Client:

    def __init__(self, library):
        self.plib: IProcessingFactory = LibraryFactory().openLibrary(library)
