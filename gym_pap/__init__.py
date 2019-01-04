from gym.envs.registration import register

register(
    id='pap-v0',
    entry_point='gym_pap.envs:PapEnv',
)
