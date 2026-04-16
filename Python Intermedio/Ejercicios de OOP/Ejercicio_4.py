class Head:
    def __init__(self, eyes, nose, mouth):
        self.eyes = eyes
        self.nose = nose
        self.mouth = mouth


class Hand:
    def __init__(self, fingers):
        self.fingers = fingers


class Arm:
    def __init__(self, hand):
        self.hand = hand


class Feet:
    def __init__(self, toes):
        self.toes = toes


class Leg:
    def __init__(self, foot):
        self.foot = foot


class Torso:
    def __init__(self, head, right_arm, left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm


class Human:
    def __init__(self, torso, right_leg, left_leg):
        self.torso = torso
        self.right_leg = right_leg
        self.left_leg = left_leg