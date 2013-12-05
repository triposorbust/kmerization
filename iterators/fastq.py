class FastQ():
    def __init__(self, fd):
        self.__fd = fd
    def __iter__(self):
        return self
    def next(self):
        try: return FastQRead([self.__fd.readline() for _ in xrange(4)])
        except: raise StopIteration()

class FastQRead():
    def __init__(self, specs):
        if any([s.strip() == "" for s in specs]) or len(specs) != 4:
            raise Exception("Could not instantiate FastQ Read object.")
        self.name = specs[0].split()[0]
        self.sequence = specs[1].strip()
