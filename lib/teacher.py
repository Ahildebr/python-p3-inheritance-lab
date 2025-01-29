#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    # self.first_name = my_teacher.first_name
    # self.last_name = my_teacher.last_name
    knowledge = ["math", "science", "history", "english"]

    def teach(self):
        return self.knowledge[0]