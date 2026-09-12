def replay(actions:list[dict], state:dict|None=None)->dict:
 state=dict(state or {})
 for action in actions:
  if action['kind']=='set': state[action['key']]=action['value']
  if action['kind']=='increment': state[action['key']]=state.get(action['key'],0)+action['value']
 return state
