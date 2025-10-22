init python:
    dayChangeIndex = -1

    def dayChangeAnimation(st, at):
        dayChangeIndex += 1
        redrawTimer = 0
        dayChangeImage = "media/v06/Common/Art/DayChange/spr_morning_%d.webp".replace("%d", str(dayChangeIndex))
        dumpToText(dayChangeImage)
        if(dayChangeIndex < 43):
            redrawTimer = 0.1
        return dayChangeImage, redrawTimer

    # class EnumeratedImagesAnimation(renpy.Displayable):
    #     def __init__(self, basePath, count, loop, **kwargs):
    #         super(EnumeratedImagesAnimation, self).__init__(**kwargs)
    #         self.images = list()
    #         imageIndexes = list(range(count))
    #         for imageIndex in imageIndexes:
    #             nextImagePath = basePath.replace("XX", str(imageIndex))
    #             self.images.append(renpy.easy.displayable(nextImagePath))
    #         self.loop = loop
    #         self.index = 0

    #     def render(self, width, height, st, at):
    #         if not st:
    #             self.index = 0
                
    #         # We just need to animate once over the list, no need for any calculations:
    #         try:
    #             t = self.images[self.index]
    #             child_render = t.render(width, height, st, at)
                
    #             w, h = child_render.get_size()
                
    #             render = renpy.Render(w, h)
    #             render.blit(child_render, (0, 0))
    #             renpy.redraw(self.images[self.index], 0.1)
                
    #             self.index = self.index + 1
    #             if self.loop:
    #                 if self.index > len(self.images) - 1:
    #                     self.index = 0
    #             return render
    #         except IndexError:
    #             return renpy.Render(0, 0)
            
    #     def visit(self):
    #         return self.images
