transform particle(d, delay, speed, endingX, endingY):
    d
    pause delay
    subpixel True
    linear speed xpos endingX ypos endingY

init python:
    class ParticleBurst(renpy.Displayable):
        def __init__(self, displayable, interval=(0.02, 0.0), speed=(0.1, 0.11), angle=(0, 360), radius=(74, 75), **kwargs):
            """Creates a burst of displayable...
            
            @params:
            - displayable: Anything that can be shown in Ren'Py (expects a single displayable or a container of displayable to randomly draw from).
            - interval: Time between bursts in seconds (expects a tuple with two floats to get randoms between them).
            - speed: Speed of the particle (same rule as above).
            - angle: Area delimiter (expects a tuple with two integers to get randoms between them) with full circle burst by default. (0, 180) for example will limit the burst only upwards creating sort of a fountain.
            - radius: Distance delimiter (same rule as above).
            - around: Position of the displayable (expects a tuple with x/y integers). Burst will be focused around this position.
            - particles: Amount of particle to go through, endless by default.
            
            This is far better customizable than the original ParticleBurst and is much easier to expand further if an required..
            """
            super(ParticleBurst, self).__init__(**kwargs)
            self.d = [renpy.easy.displayable(d) for d in displayable] if isinstance(displayable, (set, list, tuple)) else [renpy.easy.displayable(displayable)]
            self.interval = interval
            self.speed = speed
            self.angle = angle
            self.radius = radius
            self.particles = 300
        
        def render(self, width, height, st, at):
                
            rp = store.renpy
                
            if not st:
                self.next = 0
                self.particle = 0
                self.shown = {}
                
            render = rp.Render(width, height)
            
            if not (self.particles and self.particle >= self.particles) and self.next <= st:
                speed = rp.random.uniform(self.speed[0], self.speed[1])
                angle = rp.random.randrange(self.angle[0], self.angle[1])
                radius = rp.random.randrange(self.radius[0], self.radius[1])
                # self.shown[st + speed] = particle(rp.random.choice(self.d), st, speed, angle, radius)
                self.shown[st + speed] = particle(rp.random.choice(self.d), st, speed, renpy.random.randint(-100, 100), renpy.random.randint(-100, 100))
                self.next = st + rp.random.uniform(self.interval[0], self.interval[1])
                if self.particles:
                    self.particle = self.particle + 1
            
            for d in self.shown.keys():
                if d < st:
                    del(self.shown[d])
                else:
                    d = self.shown[d]
                    render.blit(d.render(width, height, st, at), (d.xpos, d.ypos))
                    
            rp.redraw(self, 0)
            
            return render

        def visit(self):
            return self.d
            
           
