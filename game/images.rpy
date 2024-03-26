# transform splinters_talking:
#     "splinters talking.png"
#     pause 0.1
#     "splinters neutral.png"
#     pause 0.1
#     repeat 2

# image splinters = TalkingDisplayable("unlucky", splinters_talking, "splinters neutral.png")

# init python:
#     def TalkingDisplayable(speaker, talking, neutral):
#         def func(st, at):
#             d = talking if _last_say_who == speaker else neutral
#             return d, None
#         return DynamicDisplayable(func)

image bg cafe silver:
    "bg cafe"
    matrixcolor SaturationMatrix(0.2) * BrightnessMatrix(0.2)

define flashback = SepiaMatrix()
