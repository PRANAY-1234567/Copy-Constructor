class Sample:
    def __init__(self, x=None, y=None, z=None):
        if isinstance(x, Sample):
            t = x
            self.x = t.x + 5
            self.y = t.y + 5
            self.z = t.z + 5

        else:
            self.x = x
            self.y = y
            self.z = z

    def display(self):
        print(f"xx = {self.x}\ty = {self.y}\tz = {self.z}")

s1 = Sample(53, 66, 68)
s2 = Sample(s1)   # copy constructor
s3 = Sample(s2)   

s1.display()
s2.display()
s3.display()
