from renderers.animation import Animation

class PlayerAnimator:
    def __init__(self):
        self.left_animation = Animation([
                                         "images/player_left/player1_right2.png",
                                         "images/player_left/player1_right3.png",
                                         "images/player_left/player1_right4.png",
                                         "images/player_left/player1_right5.png",
                                         "images/player_left/player1_right6.png",
                                         "images/player_left/player1_right7.png",
                                        ],
                                        loop = True)
        self.right_animation = Animation([

                                        "images/player_right/player2.png",
                                        "images/player_right/player3.png",
                                        "images/player_right/player4.png",
                                        "images/player_right/player5.png",
                                        "images/player_right/player6.png",
                                        "images/player_right/player7.png",
                                            ], loop = True)



        self.straight_animation = Animation([  "images/player_right/player2.png",
                                                ], loop=True)

        self.down_animation = Animation([])

        self.current_animation = self.right_animation

    def render(self, canvas,x ,y):
        self.current_animation.render(canvas,x,y)

    def update(self, player_dx, player_dy):
        if player_dx > 0:
            if player_dy >= 0:
                self.current_animation = self.right_animation
            else`:
                self.current_animation = self.straight_animation

        elif player_dx < 0:
            if player_dy >= 0:
                self.current_animation = self.left_animation
            else:
                self.current_animation =Animation(["images/player_left/player1_right2.png"], loop = True)

        else:
            if player_dy >= 0:
                self.current_animation = self.right_animation
            else:
                self.current_animation = self.straight_animation



