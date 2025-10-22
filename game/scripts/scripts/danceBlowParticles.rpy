init -5 python:
    import math
    import random

    class ParticleWithMovementData(object):
        def __init__(self, particle, xSpeed, ySpeed):
            self.particle = particle
            self.xSpeed = xSpeed
            self.ySpeed = ySpeed

    class DanceBlowParticleGenerator(object):
        def __init__(self):
            self.sm = SpriteManager(update=self.update)
            self.particles = [ ]
            self.lifespan = 0.5
            self.gravity = 240
            if persistent.danceblowParticleCount is not None:
                self.setParticleCount(persistent.danceblowParticleCount)
            else:
                # Start with one to minimize initial resource usage
                self.particleCount = 1
            self.recharge()
        
        def setParticleCount(self, particleCount):
            self.particleCount = particleCount

        def add(self, displayable):
            particle = self.sm.create(displayable)
            baseSpeed = random.random()
            angle = random.random() * 3.14159 * 2
            xSpeed = baseSpeed * math.cos(angle) * 3
            ySpeed = baseSpeed * math.sin(angle) * 3
            particle.x = xSpeed * 24
            particle.y = ySpeed * 24
            self.particles.append(ParticleWithMovementData(particle, ySpeed, xSpeed))
        
        def update(self, st):
            particleIndex=0
            for p in self.particles:
                if (st < self.lifespan):
                    p.particle.x = p.xSpeed * 120 * (st + .20)
                    p.particle.y = (p.ySpeed * 120 * (st + .20) + (self.gravity * st * st))
                else:
                    p.particle.destroy()
                    self.particles.pop(particleIndex)
                particleIndex += 1
            return 0

        def recharge(self):
            for i in range(self.particleCount):
                randomValueForColor = lambda: random.randint(0,255)
                self.add(Solid('#%02X%02X%02X' % (randomValueForColor(), randomValueForColor(), randomValueForColor()), xsize=3, ysize=3))
