from ai.tools.vision.ocr_element import OCRElement

element = OCRElement(

    text="ChatGPT",

    confidence=0.98,

    bbox=[

        [100, 50],

        [200, 50],

        [200, 90],

        [100, 90],

    ],

)

print(element)

print("Left:", element.left)

print("Right:", element.right)

print("Top:", element.top)

print("Bottom:", element.bottom)

print("Width:", element.width)

print("Height:", element.height)

print("Center:", element.center)

print("Area:", element.area)

print("Contains (150,70):", element.contains(150, 70))

print("Contains (20,20):", element.contains(20, 20))