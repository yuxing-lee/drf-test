from django_imagep.interface import ILibraryFactory, IProcessingFactory
from imagep.process import opencv


class OpenCVFactory(IProcessingFactory):

    def createProcessing(self, function: str):
        if function == "BGR2Gray":
            return opencv.BGR2Gray()
        elif function == "Binary":
            return opencv.Binary()
        elif function == "Reverse":
            return opencv.Reverse()
        elif function == "Sobel":
            return opencv.Sobel()
        elif function == "Canny":
            return opencv.Canny()
        elif function == "Laplacian":
            return opencv.Laplacian()
        elif function == "GaussianBlur":
            return opencv.GaussianBlur()
        elif function == "MedianBlur":
            return opencv.MedianBlur()
        elif function == "BilateralFilter":
            return opencv.BilateralFilter()
        elif function == "Erosion":
            return opencv.Erosion()
        elif function == "Dilation":
            return opencv.Dilation()
        elif function == "Opening":
            return opencv.Opening()
        elif function == "Closing":
            return opencv.Closing()
        else:
            return None


class LibraryFactory(ILibraryFactory):

    def openLibrary(self, library: str):
        if library == "opencv":
            return OpenCVFactory()
        else:
            return None
