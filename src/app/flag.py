class Flag:
    def __init__(self, fn: callable, is_active:bool):
        self.fn = fn
        self.is_active = is_active
        self.is_used = False