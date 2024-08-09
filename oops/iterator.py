# Iterable --> range, list, str, tuple, dict, are containers which contains some element in which we can iterate through it
# Iterator --> (an object) with the help of iterator we can excess the element of the iterable type data or element one by one

# RemoteControl class of iterator which will iter a list elements one by one
class RemoteControl:
    def __init__(self):
        self.channels = ["pogo","Hungama","CN","9xm"]
        self.index = -1
        
    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
    
        return self.channels[self.index]
    

ob = RemoteControl()
it = iter(ob)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) if one more next(it) it will raise the exception of stopIteration becoz no channel left