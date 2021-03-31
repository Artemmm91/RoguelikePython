from game_files.abstract_process import Process
from setting_files import settings
from map.map_generator import generate_map
from display.display import Display, swipe_animation, shake_screen_animation


class MainGame(Process):
    """ Process of main game with dungeons and level"""
    def __init__(self):
        super().__init__()
        self.window_close = False
        self.display = Display(self.interface)
        self.map = None
        self.hero_acted = False
        self.sprites = self.interface.GroupSprite()
        self.level = 0
        self.last_level = 2
        self.animations = []

    def new_level(self):
        """ Creating a new level - dungeon with new monsters """
        self.level += 1
        self.map = generate_map(self.level)
        self.map.spawn()
        self.map.render_map()

        self.sprites.clear()
        self.sprites.add(self.map.exit)
        for monster in self.map.mobs.values():
            self.sprites.add(monster)

        self.map.hero.center_camera(self.display)

    def main_loop(self):
        """ Main loop of program - processing each tick/frame of game """
        self.new_level()
        while not self.window_close:
            self.process_events()
            self.game_logic()
            self.draw()
            self.display.update()
            self.interface.wait(settings.frame_wait)

    def is_animation(self):
        """ Checks is there any animation proceeding """
        if self.map.hero.animation:
            return True
        for m in self.map.mobs.values():
            if m.animation:
                return True
        if len(self.animations) > 0:
            return True
        return False

    def process_events(self):
        """ Processing all events - clicking buttons - and respectively moving objects by commands """
        events = self.interface.Event.get_event()
        for event in events:
            event_type = self.interface.Event.get_event_type(event)
            if event_type == settings.quit_flag:
                self.window_close = True
            if event_type == settings.keydown_flag:
                event_key = self.interface.Event.get_key(event)
                if event_key == settings.escape_key:
                    self.display.fullscreen()
                if not self.is_animation():
                    self.hero_acted = self.map.hero.act(event_key, self.map)

    def game_logic(self):
        """ Automatic move of objects/units/monsters, checking collisions, and other game logic """
        if self.is_animation():
            return
        if isinstance(self.hero_acted, list):
            self.animations.append(swipe_animation(self.display, self.hero_acted))
            self.animations.append(shake_screen_animation(self.display))
        if self.hero_acted:
            self.monsters_turn()
            self.hero_acted = False
        self.map.exit.react(self.map)
        self.check_new_level()
        self.kill_mobs()

    def draw(self):
        """ Drawing all objects to the window """
        self.display.screen_fill(settings.colors["BLACK"])

        self.sprites.update(self.display)
        self.map.update(self.display)

        self.map.draw(self.display)
        self.sprites.draw(self.display)

        self.do_animations()

    def monsters_turn(self):
        """ Do the monsters turn - all of them acting """
        current_monsters = list(self.map.mobs.values())
        for monster in current_monsters:
            if monster != self.map.hero:
                monster.act(self.map)

    def check_new_level(self):
        """ Check if hero reached exit on current level """
        if self.map.is_reached_exit():
            if self.last_level == self.level:
                self.window_close = True
                return
            self.display.fade(False)
            self.new_level()
            self.draw()
            self.display.fade(True)

    def kill_mobs(self):
        """ Kills all mobs with hp less then 0 """
        now_mobs = list(self.map.mobs.values())
        for mob in now_mobs:
            if not mob.is_alive():
                self.sprites.erase(mob)
                self.map.erase_mob(mob)

    def do_animations(self):
        for anim in self.animations:
            try:
                next(anim)
            except StopIteration:
                self.animations.remove(anim)
