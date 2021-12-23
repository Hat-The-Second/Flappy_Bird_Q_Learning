# Flappy_Bird_Q_Learning

This repository is a q-learning agent for flappyBird.
I also made an Enviroment for this agent that is based on Flappybird.io accessed with selenium. 


Q-learning is performed based upon the states [x0, y0, vel, y1], where x0 and y0 are the player distances to the next lower pipe, vel is the agent y velocity, and y1 is the y distance between the lower pipes. x0, y0, y1 are calculated from the playerx, playery, and the array of lower pipes
States are added to the Q-table as they are encountered rather than initialising a sparse Q-table. The initial state is initialised to [0, 0, 0] where the array represents [Q of no action, Q of flap action, Times experienced this state]
Alpha (learning date) decay is added to prevent overfitting and reduce the chance of catastrophic forgetting as training continues
An epsilon greedy policy to give a chance to explore has been added but commented out. It was found that exploration is not efficient or required for this agent (only 2 possible states, flap or no flap) and environment (repeating)
Improved performance by adding functions to reduce the number of moves in memory for updating the Q-table, and to update the Q-table and end the episode if the maximum score is reached (default 10 million)
flappy_rl.py

Removed sounds, welcome animation, and game over screen to improve performance
Added the ability to perform runs without game rendering, greatly improving runtime
Added the ability to resume the game from 70 frames (distance between pipes) before death
For visibility, the current score the agent has reached is printed and updated every score interval of 10,000 This enables the agent to learn to overcome scenarios not often encountered. Once the agent has overcome this scenario, upon its next death it restarts training from the beginning to avoid the maximum score reached from continuously increasing

# Result Run
![Test Run after 150000 Epochs](/FlappyBird Pygame/results/recording_gif.gif)

Forked From FlapPyBird
