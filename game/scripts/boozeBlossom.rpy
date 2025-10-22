init -5 python:
    import pygame

    #fun, drunk, bladder
    drinkVals = {
        "Beer":[2,1,3],
        "Cocktail":[2,3,1],
        "Wine":[2,2,2]
        }
    class BoozeBlossomFactory(renpy.python.NoRollback):

        def __setstate__(self, state):
            self.start = 0
            vars(self).update(state)
            self.init()

        def __init__(self, image, count, xspeed, yspeed, border, start, fast):
            self.image = renpy.easy.displayable(image)
            self.count = count
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.start = start
            self.fast = fast
            self.init()

        def init(self):
            self.starts = [ random.uniform(0, self.start) for _i in xrange(0, self.count) ]  # W0201
            self.starts.append(self.start)
            self.starts.sort()

        def create(self, particles, st):

            def ranged(n):
                if isinstance(n, tuple):
                    return random.uniform(n[0], n[1])
                else:
                    return n

            if (st == 0) and not particles and self.fast:
                rv = [ ]

                for _i in xrange(0, self.count):
                    rv.append(BoozeBlossomParticle(self.image,
                                                ranged(self.xspeed),
                                                ranged(self.yspeed),
                                                self.border,
                                                st,
                                                random.uniform(0, 100),
                                                fast=False))
                return rv

            if particles is None or len(particles) < self.count:

                # Check to see if we have a particle ready to start. If not,
                # don't start it.
                if particles and st < self.starts[len(particles)]:
                    return None

                return [ BoozeBlossomParticle(self.image,
                                            ranged(self.xspeed),
                                            ranged(self.yspeed),
                                            self.border,
                                            st,
                                            random.uniform(0, 100),
                                            fast=False) ]

        def predict(self):
            return [ self.image ]

    class BoozeBlossomParticle(renpy.python.NoRollback):

        def __init__(self, image, xspeed, yspeed, border, start, offset, fast):

            # safety.
            if yspeed == 0:
                yspeed = 1

            self.image = image
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.start = start
            self.offset = offset
            self.proced=False

            sh = renpy.config.screen_height
            sw = renpy.config.screen_width

            if self.yspeed > 0:
                self.ystart = -border
            else:
                self.ystart = sh + border

            travel_time = (2.0 * border + sh) / abs(yspeed)

            xdist = xspeed * travel_time

            x0 = min(-xdist, 0)
            x1 = max(sw + xdist, sw)

            self.xstart = random.uniform(x0, x1)

            if fast:
                self.ystart = random.uniform(-border, sh + border)
                self.xstart = random.uniform(0, sw)
    
        def update(self, st):
            to = st - self.start
            xpos = self.xstart + to * self.xspeed
            ypos = self.ystart + to * self.yspeed
            sh = renpy.config.screen_height

            self.image.xpos = int(xpos)
            self.image.ypos = int(ypos)

            if ypos > sh + self.border:
                return None

            if ypos < -self.border:
                return None
            if xpos>800 or xpos<-5:
                return None

            dx =dy=0
            if drunkotron.mouthSprite.x != None and xpos!=0:
                dx = round(abs(xpos +40 - drunkotron.mouthSprite.x/1.75))
                dy = round(abs(ypos +140 - drunkotron.mouthSprite.y))

            if dx <60 and dy < 60 and drunkotron.active:
                if drunkotron.Fucked:
                    drunkotron.Fucked=False
                    return int(xpos), int(ypos), to + self.offset, self.image
                    
                #collided    
                multiplier=1
                if drunkotron.lastDrinkType!=self.image.drinkType and drunkotron.lastDrinkType!='None':
                    multiplier=3
                print("{}, {}, {}".format(self.image.drinkType,drunkotron.lastDrinkType,multiplier))
                drunkotron.UpdateLastDrinkType(self.image.drinkType)
                ypos=-10
                drunkotron.funLevel += drinkVals[self.image.drinkType][0] 
                drunkotron.drunkLevel += drinkVals[self.image.drinkType][1]*multiplier
                drunkotron.bladderLevel += drinkVals[self.image.drinkType][2]*multiplier
                return None
            #     drunkotron.UpdateLastDrinkType(self.image.rect)
            #     # Reposition to the top

            return int(xpos), int(ypos), to + self.offset, self.image


    def BoozeBlossom(d,
                    count=10,
                    border=10,
                    xspeed=(20, 50),
                    yspeed=(100, 200),
                    start=0,
                    fast=False):

        return Particles(BoozeBlossomFactory(image=d,
                                            count=count,
                                            border=border,
                                            xspeed=xspeed,
                                            yspeed=yspeed,
                                            start=start,
                                            fast=fast))


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    class DrunkotronBeverageDisplayable(renpy.Displayable):
        def __init__(self, disp, **kwargs):
            super(DrunkotronBeverageDisplayable, self).__init__(**kwargs)
            self.disp = disp
            self.xpos = 0
            self.ypos = 0
            self.rect = pygame.Rect(0, 0, 0, 0)
            self.drinkType = ''
            self.funScore = 0
            self.drunkScore = 0
            self.bladderScore = 0
        
        def visit(self):
            return [self.disp]

        def render(self, width, height, st, at):
            returnRender = renpy.Render(width, height)
            childRender = renpy.render(self.disp, width, height, st, at)

            childWidth, childHeight = childRender.get_size()

            self.rect = pygame.Rect(self.xpos, self.ypos, childWidth, childHeight)

            returnRender.blit(childRender, (self.xpos, self.ypos), True)


            return returnRender

        def event(self, ev, x, y, st):
            # self.xpos = x
            # self.ypos = y
            renpy.redraw(self, 0)
        
        def hasBeenConsumed(self):
            return True
            # return self.rect.colliderect(drunkotron.mouthSprite.Rectangle())

    class DrunkotronBeerDisplayable(DrunkotronBeverageDisplayable):
        def __init__(self):
            super(DrunkotronBeerDisplayable, self).__init__(renpy.displayable('media/v06/Routes/Vicky/Drunkotron/Beer.webp'))
            self.funScore = 2
            self.drunkScore = 1
            self.bladderScore = 3
            self.drinkType = 'Beer'

    class DrunkotronWineDisplayable(DrunkotronBeverageDisplayable):
        def __init__(self):
            super(DrunkotronWineDisplayable, self).__init__(renpy.displayable('media/v06/Routes/Vicky/Drunkotron/Wine.webp'))
            self.funScore = 2
            self.drunkScore = 2
            self.bladderScore = 2
            self.drinkType = 'Wine'

    class DrunkotronCocktailDisplayable(DrunkotronBeverageDisplayable):
        def __init__(self):
            super(DrunkotronCocktailDisplayable, self).__init__(renpy.displayable('media/v06/Routes/Vicky/Drunkotron/Cocktail.webp'))
            self.funScore = 2
            self.drunkScore = 3
            self.bladderScore = 1
            self.drinkType = 'Cocktail'
