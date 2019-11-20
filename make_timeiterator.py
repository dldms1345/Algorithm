class TimeIterator:
    def __secondtohour(self, crr_time):
        second = int(crr_time) % 60
        minute = ((int(crr_time) - second) // 60) % 60
        hour = ((int(crr_time) - second - minute*60) // 3600) % 24
        return '{:0>2}:{:0>2}:{:0>2}'.format(hour, minute, second)

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.crr = start

    def __next__(self):
        if self.crr < self.stop:
            tmp = self.crr
            self.crr += 1
            return self.__secondtohour(tmp)
        else:
            raise StopIteration

    def __iter__(self):
        return self
    
    def __getitem__(self, index):
        if index < self.stop - self.start:
            return self.__secondtohour(index+self.start)
        else:
            raise IndexError

start, stop, index = map(int, input().split())
 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')