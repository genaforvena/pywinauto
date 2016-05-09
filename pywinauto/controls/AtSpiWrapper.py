from ..base_wrapper import BaseWrapper
from .. import backend


class AtSpiWrapper(BaseWrapper):
    #-----------------------------------------------------------
    # TODO: can't inherit __new__ function from BaseWrapper?
    def __new__(cls, element):
        # only use the meta class to find the wrapper for HwndWrapper
        # so allow users to force the wrapper if they want
        # thanks to Raghav for finding this.
        if cls != AtSpiWrapper:
            obj = object.__new__(cls)
            obj.__init__(element)
            return obj

        new_class = cls.find_wrapper(element)

        obj = object.__new__(new_class)
        obj.__init__(element)

        return obj

    def __init__(self, element_info):
        BaseWrapper.__init__(self, element_info, backend.registry.backends['atspi'])

    def top_level_parent(self):
        return super().top_level_parent()

    def element_info(self):
        return super().element_info()

    def type_keys(self, keys, pause=None, with_spaces=False, with_tabs=False, with_newlines=False,
                  turn_off_numlock=True, set_foreground=True):
        return super().type_keys(keys, pause, with_spaces, with_tabs, with_newlines, turn_off_numlock, set_foreground)

    def release_mouse_input(self, button="left", coords=(None, None), pressed="", absolute=False, key_down=True,
                            key_up=True):
        super().release_mouse_input(button, coords, pressed, absolute, key_down, key_up)

    def is_visible(self):
        return super().is_visible()

    def window_text(self):
        return super().window_text()

    def right_click_input(self, coords=(None, None)):
        super().right_click_input(coords)

    def is_child(self, parent):
        return super().is_child(parent)

    def texts(self):
        return super().texts()

    def drag_mouse_input(self, button="left", press_coords=(0, 0), release_coords=(0, 0), pressed="", absolute=False):
        return super().drag_mouse_input(button, press_coords, release_coords, pressed, absolute)

    def click_input(self, button="left", coords=(None, None), button_down=True, button_up=True, double=False,
                    wheel_dist=0, use_log=True, pressed="", absolute=False, key_down=True, key_up=True):
        super().click_input(button, coords, button_down, button_up, double, wheel_dist, use_log, pressed, absolute,
                            key_down, key_up)

    def control_id(self):
        return super().control_id()

    def capture_as_image(self, rect=None):
        return super().capture_as_image(rect)

    def process_id(self):
        return super().process_id()

    def press_mouse_input(self, button="left", coords=(None, None), pressed="", absolute=False, key_down=True,
                          key_up=True):
        super().press_mouse_input(button, coords, pressed, absolute, key_down, key_up)

    def is_enabled(self):
        return super().is_enabled()

    def set_focus(self):
        super().set_focus()

    def root(self):
        return super().root()

    def client_to_screen(self, client_point):
        return super().client_to_screen(client_point)

    def rectangle(self):
        return super().rectangle()

    def class_name(self):
        return super().class_name()

    def verify_actionable(self):
        super().verify_actionable()

    def descendants(self):
        return super().descendants()

    def verify_enabled(self):
        return super().verify_enabled()

    def is_dialog(self):
        return super().is_dialog()

    def _needs_image_prop(self):
        return super()._needs_image_prop()

    def control_count(self):
        return super().control_count()

    def double_click_input(self, button="left", coords=(None, None)):
        super().double_click_input(button, coords)

    def writable_props(self):
        return super().writable_props()

    def verify_visible(self):
        return super().verify_visible()

    def get_properties(self):
        return super().get_properties()

    def move_mouse_input(self, coords=(0, 0), pressed="", absolute=False):
        return super().move_mouse_input(coords, pressed, absolute)

    def draw_outline(self, colour='green', thickness=2, fill=win32defines.BS_NULL, rect=None):
        super().draw_outline(colour, thickness, fill, rect)

    def friendly_class_name(self):
        return super().friendly_class_name()

    def wheel_mouse_input(self, coords=(None, None), wheel_dist=1, pressed=""):
        return super().wheel_mouse_input(coords, wheel_dist, pressed)

    def children(self, class_name=None):
        return super().children(class_name)

    def parent(self):
        return super().parent()

    def __eq__(self, other):
        return super().__eq__(other)

    def __ne__(self, other):
        return super().__ne__(other)


backend.register('atspi', None, AtSpiWrapper)