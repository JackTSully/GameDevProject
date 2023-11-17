import pygame



class EntityBase():
    def __init__(self, conf):
        self.direction = 'down'
        self.animation_list = conf.animation

        # dims
        self.x = conf.x
        self.y = conf.y
        self.width = conf.width
        self.height = conf.height

        # sprite offset          check
        self.offset_x = conf.offset_x or 0
        self.offset_y = conf.offset_y or 0

        self.health = conf.health

        #timer for turning transparency (flash)
        self.is_dead = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.state_machine = None
        self.curr_animation = None


    def CreateAnimations(self):
        pass

    def ChangeCoord(self, x=None, y=None):
        if x is not None:
            self.x = x
            self.rect.x = self.x

        if y is not None:
            self.y=y
            self.rect.y = self.y

    def MoveX(self, x):
        self.x += x
        self.rect.x = self.x

    def MoveY(self, y):
        self.y += y
        self.rect.y = self.y

    def ChangeState(self, name):
        self.state_machine.Change(name)

    def ChangeAnimation(self, name):
        self.curr_animation = self.animation_list[name]

    def update(self, dt, events):
        self.state_machine.update(dt, events)

        if self.curr_animation:
            self.curr_animation.update(dt)

    def render(self, adjacent_offset_x=0, adjacent_offset_y=0):
        if self.curr_animation.idleSprite is not None:
            self.curr_animation.idleSprite.set_alpha(64)
        self.curr_animation.image.set_alpha(64)

        self.x = self.x + adjacent_offset_x
        self.y = self.y + adjacent_offset_y
        self.state_machine.render()
        if self.curr_animation.idleSprite is not None:
            self.curr_animation.idleSprite.set_alpha(255)
        self.curr_animation.image.set_alpha(255)

