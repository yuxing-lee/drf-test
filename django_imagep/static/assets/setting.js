let settings = {
    "BGR2Gray": {
        "name": "灰階",
        "group": "Converter",
        "default": {}
    },
    "Binary": {
        "name": "二值化",
        "group": "Converter",
        "default": {
            "threshold": 127
        },
        "range": {
            "threshold": [0, 255, 5]
        }
    },
    "Reverse": {
        "name": "反向",
        "group": "Converter",
        "default": {}
    },
    "Sobel": {
        "name": "Sobel",
        "group": "Edge",
        "default": {
            "ksize": 3,
        },
        "range": {
            "ksize": [1, 31, 2]
        }
    },
    "Canny": {
        "name": "Canny",
        "group": "Edge",
        "default": {
            "threshold1": 100,
            "threshold2": 200
        },
        "range": {
            "threshold1": [0, 255, 5],
            "threshold2": [0, 255, 5]
        }
    },
    "Laplacian": {
        "name": "Laplacian",
        "group": "Edge",
        "default": {
            "ksize": 3
        },
        "range": {
            "ksize": [1, 31, 2]
        }
    },
    "GaussianBlur": {
        "name": "GaussianBlur",
        "group": "Filter",
        "default": {
            "ksize": 3
        },
        "range": {
            "ksize": [1, 31, 2]
        }
    },
    "MedianBlur": {
        "name": "MedianBlur",
        "group": "Filter",
        "default": {
            "ksize": 3
        },
        "range": {
            "ksize": [1, 31, 2]
        }
    },
    "BilateralFilter": {
        "name": "BilateralFilter",
        "group": "Filter",
        "default": {
            "d": 9,
            "sigmaColor": 75,
            "sigmaSpace": 75
        },
        "range": {
            "d": [1, 31, 2],
            "sigmaColor": [1, 255, 5],
            "sigmaSpace": [1, 255, 5]
        }
    },
    "Erosion": {
        "name": "Erosion",
        "group": "Morphology",
        "default": {
            "ksize": 3,
            "iterations": 1
        },
        "range": {
            "ksize": [1, 31, 2],
            "iterations": [1, 10, 1]
        }
    },
    "Dilation": {
        "name": "Dilation",
        "group": "Morphology",
        "default": {
            "ksize": 3,
            "iterations": 1
        },
        "range": {
            "ksize": [1, 31, 2],
            "iterations": [1, 10, 1]
        }
    },
    "Opening": {
        "name": "Opening",
        "group": "Morphology",
        "default": {
            "ksize": 3,
            "iterations": 1
        },
        "range": {
            "ksize": [1, 31, 2],
            "iterations": [1, 10, 1]
        }
    },
    "Closing": {
        "name": "Closing",
        "group": "Morphology",
        "default": {
            "ksize": 3,
            "iterations": 1
        },
        "range": {
            "ksize": [1, 31, 2],
            "iterations": [1, 10, 1]
        }
    }
}
